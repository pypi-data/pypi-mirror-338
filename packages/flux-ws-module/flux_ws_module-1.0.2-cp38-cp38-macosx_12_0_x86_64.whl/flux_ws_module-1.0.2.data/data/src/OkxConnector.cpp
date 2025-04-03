#include "OkxConnector.h"
#include "CryptoExtensions.h"
#include <chrono>
#include <sstream>
#include <iostream>
#include <future>
#include <iomanip>
#include <memory>
#include <stdexcept>

#ifdef WITH_PYTHON  // Defined when building Python bindings
#include <pybind11/pybind11.h>
namespace py = pybind11;
#endif

using json = nlohmann::json;


// -------------------------
// Public Connection Constructor
// -------------------------
OkxConnector::OkxConnector() : is_private_connection(false){
    m_client.clear_access_channels(websocketpp::log::alevel::all);
    m_client.init_asio();
    
    m_client.set_open_handler(bind(&OkxConnector::on_open_public, this, ::_1));
    m_client.set_close_handler(bind(&OkxConnector::on_close, this, ::_1));

    m_client.set_message_handler(bind(&OkxConnector::on_message, this, ::_1, ::_2));

    m_client.set_tls_init_handler(bind(&OkxConnector::on_tls_init, this));

    m_client.set_fail_handler([this](websocketpp::connection_hdl) {
        std::cout << "Connection failed" << std::endl;
    });

    cryptoExtensions = CryptoExtensions();
}


// -------------------------
// Private Connection Constructor (with API credentials)
// -------------------------
OkxConnector::OkxConnector(const std::string API_key,
                           const std::string API_secret,
                           const std::string API_pass) 
    : _API_key(API_key), _API_secret(API_secret),_API_pass(API_pass), is_private_connection(true) {
    m_client.clear_access_channels(websocketpp::log::alevel::all);
    m_client.init_asio();
    
    m_client.set_open_handler(bind(&OkxConnector::on_open_private, this, ::_1));
    m_client.set_close_handler(bind(&OkxConnector::on_close, this, ::_1));

    m_client.set_message_handler(bind(&OkxConnector::on_message, this, ::_1, ::_2));

    m_client.set_tls_init_handler(bind(&OkxConnector::on_tls_init, this));

    m_client.set_fail_handler([this](websocketpp::connection_hdl) {
        std::cout << "Connection failed" << std::endl;
    });

    cryptoExtensions = CryptoExtensions();
}

OkxConnector::~OkxConnector() {
    disconnect();
}

// -------------------------
// TLS Initialization
// -------------------------
context_ptr OkxConnector::on_tls_init() {
    auto ctx = std::make_shared<boost::asio::ssl::context>(boost::asio::ssl::context::sslv23);
    try {
        ctx->set_options(boost::asio::ssl::context::default_workarounds |
                         boost::asio::ssl::context::no_sslv2 |
                         boost::asio::ssl::context::no_sslv3 |
                         boost::asio::ssl::context::single_dh_use);
    } catch (std::exception& e) {
        throw std::runtime_error("TLS init failed: " + std::string(e.what()));
    }
    return ctx;
}

//----------------------------------
// CONNECT AFTER ALL SUBS MADE
//----------------------------------
void OkxConnector::connect(const std::string& uri) {
    websocketpp::lib::error_code ec;
    auto con = m_client.get_connection(uri, ec);
    
    if (ec || !con) {
        throw std::runtime_error("Connection failed: " + ec.message());
    }

    m_client.connect(con);
    m_running = true;
    m_client_thread = std::thread([this]() {
        try {
            m_client.run();
        } catch (const std::exception& e) {
            std::cerr << "WebSocket error: " << e.what() << std::endl;
            m_running = false;
            if (m_running) {
                std::cerr << "WebSocket error: " << e.what() << std::endl;
            }
        }
    });
}

//----------------------------------------
// DISCONNECT WITH THREAD KILL
//----------------------------------------
// TBD: add unsubscribe if disconnected gracefully?
void OkxConnector::disconnect() {
    if (m_running.exchange(false)) {
        m_client.stop();
        m_cv.notify_all();
        if (m_client_thread.joinable()) {
            m_client_thread.join();
        }
    }
}

// -----------------------------
// ON EVENT HANDLERS
// -----------------------------
void OkxConnector::on_open_private(websocketpp::connection_hdl hdl) {
    m_hdl = hdl;
    m_connected = true;
    login(_API_key, _API_secret, _API_pass);
}

void OkxConnector::on_open_public(websocketpp::connection_hdl hdl) {
    m_hdl = hdl;
    m_connected = true;
    
    {
        std::lock_guard<std::mutex> lock(m_mutex);
        if (!m_subscriptions_public.empty()) {
            json msg;
            msg["op"] = "subscribe";
            auto& args = msg["args"] = json::array();
            for (const auto& sub : m_subscriptions_public) {
                args.push_back({ {"channel", sub.first}, {"instId", sub.second} });
            }

            // std::cout << msg << std::endl;
            send_message(msg);
        }
    }
}

void OkxConnector::on_close(websocketpp::connection_hdl hdl) {
    m_connected = false;
    is_logged = false;
    m_cv.notify_all();
}

void OkxConnector::on_message(websocketpp::connection_hdl, message_ptr msg) {    
    if (is_private_connection) {
        if(!is_logged) {
            auto json_msg = json::parse(msg->get_payload());
            std::cout << json_msg << std::endl;
            
            // Check if the message corresponds to a login response
            if (json_msg.contains("event") && json_msg["event"] == "login" &&
                json_msg.contains("code") && json_msg["code"] == "0") {
                    subscribe_pending();
            }
            is_logged = true;
        }
    }
    // std::cout << msg->get_payload() << std::endl;
    std::lock_guard<std::mutex> lock(m_mutex);
    m_messages.push(msg->get_payload());
    m_cv.notify_one();
}

void OkxConnector::subscribe_pending() {
    // std::lock_guard<std::mutex> lock(m_mutex);
    if (!m_subscriptions_private.empty()) {
        json msg;
        msg["op"] = "subscribe";
        auto& args = msg["args"] = json::array();
        
        for (const auto& channel : m_subscriptions_private) {
            args.push_back({{"channel", channel}});
        }
        // std::cout << msg << std::endl;
        send_message(msg);
    }
    else {
        throw std::runtime_error("No subscriptions found");
    }
}

//---------------------------------
// LOGIN
//---------------------------------
std::string OkxConnector::generate_sign(const std::string& secret,
                                          const std::string& timestamp) {
    // Construct the signature payload
    const std::string method = "GET";
    const std::string endpoint = "/users/self/verify";
    const std::string sign_payload = timestamp + method + endpoint;

    // Calculate HMAC-SHA256 (returns binary string)
    std::string hmac_digest = cryptoExtensions.CalcHmacSHA256(secret, sign_payload);

    // Base64 encode the binary result
    return cryptoExtensions.encode64(hmac_digest);
}

void OkxConnector::login(const std::string& api_key,
                         const std::string& secret,
                         const std::string& passphrase) {
    // Generate timestamp in seconds
    const auto now = std::chrono::system_clock::now();
    const std::string timestamp = std::to_string(
        std::chrono::duration_cast<std::chrono::seconds>(
            now.time_since_epoch()).count());

    // Generate cryptographic signature
    const std::string signature = generate_sign(secret, timestamp);

    // Construct JSON message
    json msg;
    msg["op"] = "login";
    msg["args"] = json::array({
        {
            {"apiKey", api_key},
            {"passphrase", passphrase},
            {"timestamp", timestamp},
            {"sign", signature}
        }
    });

    send_message(msg);
}

// --------------------------------
// SUBSCRIBE UNSUBSCRIBE ACTIONS
// --------------------------------
// Unified Subscribe Method
void OkxConnector::subscribe(const std::map<std::string, std::string>& kwargs) {
    if (is_private_connection) {
        validate_required(kwargs, {"channel"});
        const std::string channel = kwargs.at("channel");

        subscribe_private(channel);
    } else {
        validate_required(kwargs, {"channel", "inst_id"});
        const std::string channel = kwargs.at("channel");
        const std::string inst_id = kwargs.at("inst_id");

        subscribe_public(channel, inst_id);
    }
}

void OkxConnector::subscribe_public(const std::string& channel, const std::string& inst_id) {
    std::lock_guard<std::mutex> lock(m_mutex);
    
    if (m_connected) {
        // Send immediate subscription
        json msg;
        msg["op"] = "subscribe";
        msg["args"] = json::array({
            {{"channel", channel}, {"instId", inst_id}}
        });
        send_message(msg);
    }
    
    // Add to subscription list for reconnect scenarios
    m_subscriptions_public.emplace_back(channel, inst_id);
    for (const auto& sub : m_subscriptions_public) {
        std::cout << "Channel: " << sub.first << ", inst_id: " << sub.second << std::endl;
    }

}

void OkxConnector::subscribe_private(const std::string& channel) {
    std::lock_guard<std::mutex> lock(m_mutex);
    
    if (m_connected) {
        // Send immediate subscription
        json msg;
        msg["op"] = "subscribe";
        msg["args"] = json::array({
            {{"channel", channel}}
        });
        send_message(msg);
    }
    
    // Add to subscription list for reconnect scenarios
    m_subscriptions_private.emplace_back(channel);
    for (const auto& sub : m_subscriptions_private) {
        std::cout << "Channel: " << sub << std::endl;
    }
}

// Unified Unsubscribe Method
void OkxConnector::unsubscribe(const std::map<std::string, std::string>& kwargs) {
    if (is_private_connection) {
        validate_required(kwargs, {"channel"});
        const std::string channel = kwargs.at("channel");

        unsubscribe_private(channel);
    } else {
        validate_required(kwargs, {"channel", "inst_id"});
        const std::string channel = kwargs.at("channel");
        const std::string inst_id = kwargs.at("inst_id");

        unsubscribe_public(channel, inst_id);
    }
}

void OkxConnector::unsubscribe_public(const std::string& channel, const std::string& inst_id) {
    std::lock_guard<std::mutex> lock(m_mutex);
    
    // Remove from subscriptions
    m_subscriptions_public.erase(
        std::remove_if(m_subscriptions_public.begin(), m_subscriptions_public.end(),
            [&](const auto& sub) {
                return sub.first == channel && sub.second == inst_id;
            }),
        m_subscriptions_public.end()
    );
    
    if (m_connected) {
        // Send unsubscribe request
        json msg;
        msg["op"] = "unsubscribe";
        msg["args"] = json::array({
            {{"channel", channel}, {"instId", inst_id}}
        });
        send_message(msg);
    }
}

void OkxConnector::unsubscribe_private(const std::string& channel) {
    std::lock_guard<std::mutex> lock(m_mutex);
    
    // Remove from subscriptions
    m_subscriptions_private.erase(
        std::remove(m_subscriptions_private.begin(), m_subscriptions_private.end(), channel),
        m_subscriptions_private.end()
    );
    
    if (m_connected) {
        // Send unsubscribe request
        json msg;
        msg["op"] = "unsubscribe";
        msg["args"] = json::array({
            {{"channel", channel}}
        });
        send_message(msg);
    }
}

//---------------------------
// SEND
// --------------------------
void OkxConnector::send_message(const json& msg) {
    websocketpp::lib::error_code ec;
    m_client.send(m_hdl, msg.dump(), websocketpp::frame::opcode::text, ec);
    if (ec) {
        throw std::runtime_error("Send failed: " + ec.message());
    }
}

//--------------------------
// ORDERS
//--------------------------
void OkxConnector::place_order(const std::map<std::string, std::string>& kwargs) {
    validate_required(kwargs, {"ord_id", "inst_id", "side", "px", "sz"});
    
    const std::string ord_id = kwargs.at("ord_id");
    const std::string inst_id = kwargs.at("inst_id");
    const std::string side = kwargs.at("side");
    const std::string px = kwargs.at("px");
    const std::string sz = kwargs.at("sz");

    const std::string tdMode = get_optional(kwargs, std::string("tdMode"), std::string(""));
    const std::string ccy = get_optional(kwargs, std::string("ccy"), std::string(""));
    const std::string ordType = get_optional(kwargs, std::string("ordType"), std::string("market"));

    place_order(ord_id, inst_id, side, px, sz, tdMode, ccy, ordType);
    
}

void OkxConnector::place_order(const std::string& ord_id, const std::string& inst_id,
                               const std::string& side, 
                               const std::string &px, const std::string& sz,
                               const std::string& tdMode,
                               const std::string& ccy, 
                               const std::string& ordType) {
    json msg;
    msg["id"] = ord_id;
    msg["op"] = "order";
    msg["args"] = json::array({
        {
            {"side", side},
            {"instId", inst_id},
            {"tdMode", tdMode},
            {"ccy", ccy},
            {"ordType", ordType},
            {"pxUsd", px},
            {"sz", sz}
        }
        });
    send_message(msg);
}

//void OkxConnector::place_multiple_order(std::vector <const std::string>& ord_id,
//    std::vector<const std::string>& inst_id,
//    std::vector<const std::string>& side,
//    std::vector<const std::string>& px,
//    std::vector<const std::string>& sz,
//    std::vector<const std::string>& tdMode,
//    std::vector<const std::string>& ccy) {
//    json msg;
//    msg["id"] = ord_id;
//    msg["op"] = "batch-orders";
//
//    auto t = json::array({});
//    for (int i = 0; i < px.size(); i++)
//    {
//        t.push_back({
//            {"side", side[i]},
//            {"instId", inst_id[i]},
//            {"tdMode", tdMode[i]},
//            {"ccy", ccy[i]},
//            {"ordType", "limit"},
//            {"pxUsd", px[i]},
//            {"sz", sz[i]}
//            });
//    }
//
//    send_message(msg);
//}
void OkxConnector::cancel_order(const std::map<std::string, std::string>& kwargs) {
    validate_required(kwargs, {"msg_id", "ord_id", "inst_id"});

    const std::string msg_id = kwargs.at("msg_id"); //?
    const std::string ord_id = kwargs.at("ord_id");
    const std::string inst_id = kwargs.at("inst_id");

    cancel_order(msg_id, ord_id, inst_id);
}
void OkxConnector::cancel_order(const std::string& msg_id, const std::string& ord_id, const std::string& inst_id) {
    json msg;
    msg["id"] = msg_id;
    msg["op"] = "cancel-order";
    msg["args"] = json::array({
        {
            {"ordId", ord_id},
            {"instId", inst_id}
        }
    });
    send_message(msg);
}

//void OkxConnector::cancel_multiple_orders(const std::string& msg_id, std::vector<const std::string>& ord_id, const std::string& inst_id) {
//    json msg;
//    msg["id"] = msg_id;
//    msg["op"] = "batch-cancel-orders";
//    auto t = json::array({});
//    for (int i = 0; i < ord_id.size(); i++)
//    {
//        t.push_back({
//            {"ordId", ord_id[i]},
//            {"instId", inst_id[i]}
//        });
//    }
//    msg["args"] = t;
//    send_message(msg);
//}

// void OkxConnector::change_order()