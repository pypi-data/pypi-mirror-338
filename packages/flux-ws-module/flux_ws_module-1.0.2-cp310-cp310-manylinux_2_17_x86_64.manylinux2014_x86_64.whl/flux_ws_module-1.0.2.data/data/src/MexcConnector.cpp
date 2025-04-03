#include "MexcConnector.h"
#include "CryptoExtensions.h"
#include "BaseExchangeConnector.h"

#include <chrono>
#include <sstream>

#include <queue>
#include <future>

#include <time.h>
#include <stdio.h>
#include <sstream>
#include <iomanip>
#include <memory>
#include <mutex>
#include <queue>
#include <condition_variable>
#include <thread>
#include <future>

#include <openssl/hmac.h>
#include <openssl/sha.h>


#include <boost/beast/core.hpp>
#include <boost/beast/http.hpp>
#include <boost/beast/ssl.hpp>
#include <boost/asio/connect.hpp>
#include <boost/asio/ip/tcp.hpp>
#include <boost/asio/ssl.hpp>


using json = nlohmann::json;

#ifdef WITH_PYTHON  // Defined when building Python bindings
#include <pybind11/pybind11.h>
namespace py = pybind11;
#endif

// -------------------------
// Private Connection Constructor (with API credentials)
// -------------------------
MexcConnector::MexcConnector(const std::string API_url,
                                const std::string API_key,
                                const std::string API_secret){
    m_client.clear_access_channels(websocketpp::log::alevel::all);
    m_client.init_asio();

    m_client.set_open_handler(bind(&MexcConnector::on_open_private, this, ::_1));
    m_client.set_close_handler(bind(&MexcConnector::on_close, this, ::_1));

    m_client.set_message_handler(bind(&MexcConnector::on_message, this, ::_1, ::_2));

    m_client.set_tls_init_handler(bind(&MexcConnector::on_tls_init, this));
    m_client.set_fail_handler([this](websocketpp::connection_hdl) {
        std::cout << "Connection failed" << std::endl;
    });

    _API_url = API_url;
    _API_key = API_key;
    _API_secret = API_secret;
    is_private_connection = true;
}

// -------------------------
// Public Connection Constructor
// -------------------------
MexcConnector::MexcConnector(){
    m_client.clear_access_channels(websocketpp::log::alevel::all);
    m_client.init_asio();

    m_client.set_open_handler(bind(&MexcConnector::on_open_public, this, ::_1));
    m_client.set_close_handler(bind(&MexcConnector::on_close, this, ::_1));

    m_client.set_message_handler(bind(&MexcConnector::on_message, this, ::_1, ::_2));

    m_client.set_tls_init_handler(bind(&MexcConnector::on_tls_init, this));
    m_client.set_fail_handler([this](websocketpp::connection_hdl) {
        std::cout << "Connection failed" << std::endl;
    });

    is_private_connection = false;
}

MexcConnector::~MexcConnector() {
    disconnect();
}

context_ptr MexcConnector::on_tls_init() {
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
void MexcConnector::connect(const std::string& uri) {
    websocketpp::lib::error_code ec;
    client::connection_ptr con = { 0 };

    if(is_private_connection){
        auto j = json::parse(rest_request("POST",
                                          "api.mexc.com",
                                          "/api/v3/userDataStream",
                                          _API_key,_API_secret,_payload));
        _listenKey = j["listenKey"];
        con = m_client.get_connection(uri + "?listenKey=" + _listenKey, ec);
        std::cout << "Connected MEXC private" << std::endl;
    }
    else
    {
        con = m_client.get_connection(uri, ec);
    }
    if (ec || !con) {
        throw std::runtime_error("Connection failed: " + ec.message());
    }
    m_client.connect(con);
    m_running = true;
    m_client_thread = std::thread([this]() {
        try {
            m_client.run();
        } catch (const std::exception& e) {
            if (m_running) {
                std::cerr << "WebSocket error: " << e.what() << std::endl;
            }
        }
    });
    m_client_thread = std::thread([this]() {
        try {
            ping();
        } catch (const std::exception& e) {
            if (m_running) {
                std::cerr << "WebSocket error: " << e.what() << std::endl;
            }
        }
    });
}

void MexcConnector::disconnect() {
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
void MexcConnector::on_open_public(websocketpp::connection_hdl hdl) {
    m_hdl = hdl;
    m_connected = true;

    //TODO добавить пинг после успешной подписки если нет входящего потока данных
    std::lock_guard<std::mutex> lock(m_mutex);
    if (!m_subscriptions_public.empty()) {
        json msg;
        msg["method"] = "SUBSCRIPTION";
        msg["params"] = json::array();
        
        for (const auto& [host, symbol, level] : m_subscriptions_public) {
            msg["params"].push_back(
                host + "@" + symbol + "@" + level
            );
        }
        send_message(msg);
    }
}

void MexcConnector::on_open_private(websocketpp::connection_hdl hdl) {
    m_hdl = hdl;
    m_connected = true;
    //TODO добавить пинг после успешной подписки если нет входящего потока данных
    if (is_private_connection) {
        if(_listenKey!="") {
            subscribe_pending();
            m_client_thread_refresh = std::thread([this]() {
                try {
                    refresh_listenKey();
                } catch (const std::exception& e) {
                    if (m_running) {
                        std::cerr << "WebSocket error: " << e.what() << std::endl;
                    }
                }
            });
        }
    }
}

void MexcConnector::on_close(websocketpp::connection_hdl hdl) {
    std::cout << "Connection MEXC closed" << std::endl;
    m_connected = false;
    m_cv.notify_all();
}

void MexcConnector::on_message(websocketpp::connection_hdl, message_ptr msg) {
    std::lock_guard<std::mutex> lock(m_mutex);
    m_messages.push(msg->get_payload()); 
    m_cv.notify_one();
}


void MexcConnector::send_message(const nlohmann::json& msg) {
    websocketpp::lib::error_code ec;
    m_client.send(m_hdl, msg.dump(), websocketpp::frame::opcode::text, ec);
    if (ec) {
        throw std::runtime_error("Send failed: " + ec.message());
    }
}

void MexcConnector::subscribe_pending() {
    // std::lock_guard<std::mutex> lock(m_mutex);
    if (!m_subscriptions_private.empty()) {
        json msg;
        msg["method"] = "SUBSCRIPTION";
        msg["params"] = json::array();
        
        for (const auto& host : m_subscriptions_private) {
            msg["params"].push_back(host);
        }
        send_message(msg);
    }
}

// --------------------------------
// SUBSCRIBE UNSUBSCRIBE ACTIONS
// --------------------------------
// Unified Subscribe Method
void MexcConnector::subscribe(const std::map<std::string, std::string>& kwargs) {
    if (is_private_connection) {
        validate_required(kwargs, {"channel"});

        const std::string channel = kwargs.at("channel");

        subscribe_private(channel);
    } else {
        validate_required(kwargs, {"host", "symbol"});

        const std::string host = kwargs.at("host");
        const std::string symbol = kwargs.at("symbol");

        const std::string level = get_optional(kwargs, std::string("level"), std::string(""));

        subscribe_public(host, symbol, level);
    }
}

void MexcConnector::subscribe_private(const std::string& channel) {
    std::lock_guard<std::mutex> lock(m_mutex);
    if (m_connected) {
        // Send immediate subscription
        json msg;
        msg["method"] = "SUBSCRIPTION";
        msg["params"] = json::array();
        msg["params"].push_back(channel);
        
        send_message(msg);
    }
    m_subscriptions_private.emplace_back(channel);
}

// Добавляем в публичные подписки
void MexcConnector::subscribe_public(const std::string& host ,const std::string& symbol, const std::string& level) {
    std::lock_guard<std::mutex> lock(m_mutex);
    if (m_connected) {
        // Send immediate subscription
        json msg;
        msg["method"] = "SUBSCRIPTION";
        msg["params"] = json::array();
        msg["params"].push_back(host + "@" + symbol + "@" + level);
        send_message(msg);
    }
    
    // Add to subscription list for reconnect scenarios
    m_subscriptions_public.emplace_back(host, symbol, level);
}

void MexcConnector::unsubscribe(const std::map<std::string, std::string>& kwargs) {
    if (is_private_connection) {
        validate_required(kwargs, {"channel"});
        const std::string channel = kwargs.at("channel");

        unsubscribe_private(channel);
    } else {
        validate_required(kwargs, {"host", "symbol"});
        const std::string host = kwargs.at("host");
        const std::string symbol = kwargs.at("symbol");

        const std::string level = get_optional(kwargs, std::string("level"), std::string(""));
        unsubscribe_public(host, symbol, level);
    }
}
void MexcConnector::unsubscribe_private(const std::string& channel) {
    std::lock_guard<std::mutex> lock(m_mutex);
    
    // Remove from subscriptions
    auto it = std::find(m_subscriptions_private.begin(), m_subscriptions_private.end(), channel);
    if (it != m_subscriptions_private.end()) {
        m_subscriptions_private.erase(it);
    }

    if (m_connected) {
        // Send unsubscribe request
        json msg;
        msg["method"] = "UNSUBSCRIPTION";
        msg["params"] ={{channel}};
        send_message(msg);
    }
}

void MexcConnector::unsubscribe_public(const std::string& host ,const std::string& symbol, const std::string& level) {
    std::lock_guard<std::mutex> lock(m_mutex);
    
    // Remove from subscriptions
    m_subscriptions_public.erase(
        std::remove_if(m_subscriptions_public.begin(), m_subscriptions_public.end(),
            [&](const auto& tuple) {
                return std::get<0>(tuple) == host &&
                       std::get<1>(tuple) == symbol &&
                       std::get<2>(tuple) == level;
            }),
        m_subscriptions_public.end());

    if (m_connected) {
        // Send unsubscribe request
        json msg;
        msg["method"] = "UNSUBSCRIPTION";
        msg["params"] ={{host + "@" + symbol + "@" + level}};
        send_message(msg);
    }
}

void MexcConnector::place_order(const std::map<std::string, std::string>& kwargs) {
    validate_required(kwargs, {"ord_id", "inst_id", "side", "sz"});

    const std::string ord_id = kwargs.at("ord_id");
    const std::string inst_id = kwargs.at("inst_id");
    const std::string side = kwargs.at("side");
    const std::string sz = kwargs.at("sz");

    const std::string px = get_optional(kwargs, std::string("px"), std::string(""));
    const std::string tdMode = get_optional(kwargs, std::string("tdMode"), std::string(""));
    const std::string ccy = get_optional(kwargs, std::string("ccy"), std::string(""));
    
    // const std::string ordType = get_optional(kwargs, "ordType", std::string("market"));
    
    place_order(ord_id, inst_id, side, px, sz, tdMode, ccy);
    
}

void MexcConnector::place_order(const std::string& ord_id,
    const std::string& inst_id,
    const std::string& side,
    const std::string& px,
    const std::string& sz,
    const std::string& tdMode,
    const std::string& ccy) {
        _payload.clear();
        _payload = {
            {"symbol", inst_id},
            {"side", side},
            {"type", tdMode}, //?
            {"quantity", sz},
            {"price", px}
        };
        // ccy, ordType?
        rest_request("POST","api.mexc.com", "/api/v3/order",
            _API_key,_API_secret,_payload);
}

void MexcConnector::cancel_order(const std::map<std::string, std::string>& kwargs) {
    validate_required(kwargs, {"msg_id", "ord_id", "inst_id"});
    
    const std::string msg_id =kwargs.at("msg_id"); //?
    const std::string ord_id =kwargs.at("ord_id");
    const std::string inst_id =kwargs.at("inst_id");

    cancel_order(msg_id, ord_id, inst_id);
}

void MexcConnector::cancel_order(const std::string& msg_id, const std::string& ord_id, const std::string& inst_id) {
    _payload.clear();
    _payload = {
        {"symbol",inst_id},
        {"orderId",ord_id}
    };
    rest_request("DELETE","api.mexc.com", "/api/v3/order",
        _API_key,_API_secret,_payload);
}

// ЗДЕСЬ ПРОИСХОДИТ ОТПРАВКА REST ЗАПРОСА 
std::string MexcConnector::rest_request(const std::string& type_of_request,const std::string& host, const std::string& target,
                                        const std::string& api_key,const std::string& secret,std::map<std::string, std::string> payload) {

    try {
        // Контекст I/O
        boost::asio::io_context ioc;

        // SSL-контекст
        boost::asio::ssl::context ctx(boost::asio::ssl::context::tlsv12_client);
        ctx.set_default_verify_paths();

        // Разрешение доменного имени
        boost::asio::ip::tcp::resolver resolver(ioc);
        auto const results = resolver.resolve(host, "443");

        // Создание SSL-соединения
        boost::beast::ssl_stream<boost::beast::tcp_stream> stream(ioc, ctx);
        boost::beast::get_lowest_layer(stream).connect(results);

        // SSL handshake
        stream.handshake(boost::asio::ssl::stream_base::client);

        // Подготовка запроса
        if(type_of_request == "POST"){
            boost::beast::http::request<boost::beast::http::string_body> req{boost::beast::http::verb::post, target, 11};
        } else if(type_of_request == "GET"){
            boost::beast::http::request<boost::beast::http::string_body> req{boost::beast::http::verb::get, target, 11};
        } else if(type_of_request == "PUT"){
            boost::beast::http::request<boost::beast::http::string_body> req{boost::beast::http::verb::put, target, 11};
        } else if(type_of_request == "DELETE"){
            boost::beast::http::request<boost::beast::http::string_body> req{boost::beast::http::verb::delete_, target, 11};
        } else{
            boost::beast::error_code ec;
            stream.shutdown(ec);
        }
        boost::beast::http::request<boost::beast::http::string_body> req{boost::beast::http::verb::post, target, 11};
        req.set(boost::beast::http::field::host, host);
        req.set(boost::beast::http::field::user_agent, "Boost.Beast");
        req.set("X-MEXC-APIKEY", api_key);
        req.set(boost::beast::http::field::content_type, "application/json");

        //Текущее время
        const auto now = std::chrono::system_clock::now();
        const std::string timestamp = std::to_string(
            std::chrono::duration_cast<std::chrono::milliseconds>(
                now.time_since_epoch()).count());
       payload["timestamp"] = timestamp;
       
        
        //URL-кодирование параметров
        std::string sign = map_to_url_params(payload);
        
        //Генерация HMAC-SHA256 подписи
        std::string signature = generate_signature(secret, sign);
        payload["signature"] = signature;


        req.body() = map_to_url_params(payload); 
        req.prepare_payload();

        // Отправка запроса
        boost::beast::http::write(stream, req);

        // Получение ответа
        boost::beast::flat_buffer buffer;
        boost::beast::http::response<boost::beast::http::string_body> res;
        boost::beast::http::read(stream, buffer, res);

        // Закрытие соединения
        boost::beast::error_code ec;
        stream.shutdown(ec); // Игнорируем ошибки при shutdown

        return res.body();
    }
    catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return "";
    }
}

// ФУНКЦИИ ДЛЯ ПОДПИСИ
std::string MexcConnector::url_encode(const std::string &value) {
    std::ostringstream escaped;
    escaped.fill('0');
    escaped << std::hex;

    for (char c : value) {
        if (isalnum(c) || c == '-' || c == '_' || c == '.' || c == '~') {
            escaped << c;
        } else {
            escaped << '%' << std::setw(2) << int(static_cast<unsigned char>(c));
        }
    }

    return escaped.str();
}

std::string MexcConnector::map_to_url_params(const std::map<std::string, std::string>& params) {
    std::ostringstream result;
    bool first = true;

    for (const auto& [key, value] : params) {
        if (!first) {
            result << "&";
        }
        first = false;
        
        result << url_encode(key) << "=" << url_encode(value);
    }

    return result.str();
}

std::string MexcConnector::generate_signature(const std::string& secret, const std::string& message) {

    unsigned char digest[HMAC_MAX_MD_CBLOCK];
    unsigned int len;
    
    // Создаем контекст HMAC
    HMAC_CTX* ctx = HMAC_CTX_new();
    
    // Инициализируем HMAC с секретным ключом и алгоритмом SHA256
    HMAC_Init_ex(ctx, secret.data(), secret.length(), EVP_sha256(), nullptr);
    
    // Добавляем данные для хеширования
    HMAC_Update(ctx, reinterpret_cast<const unsigned char*>(message.data()), message.length());
    
    // Получаем финальный хеш
    HMAC_Final(ctx, digest, &len);
    
    // Освобождаем контекст
    HMAC_CTX_free(ctx);
    
    // Конвертируем бинарный хеш в hex-строку
    std::ostringstream oss;
    for (unsigned int i = 0; i < len; i++) {
        oss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(digest[i]);
    }
    
    return oss.str();
}

void MexcConnector::refresh_listenKey(){
    std::this_thread::sleep_for(std::chrono::minutes(20));
    _payload.clear();
    auto j = rest_request("PUT","api.mexc.com", "/api/v3/userDataStream",
        _API_key,_API_secret,_payload);
}
void MexcConnector::ping(){
    json msg;
    msg["method"] = "PING";
    while (true) {
        std::cout << "Пингуем " << msg.dump() << std::endl;
        send_message(msg);
        std::this_thread::sleep_for(std::chrono::seconds(30));
    }
}