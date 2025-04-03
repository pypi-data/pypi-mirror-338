#pragma once

#include <websocketpp/config/asio_client.hpp>
#include <websocketpp/client.hpp>
#include <BaseExchangeConnector.h>

#include <queue>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <thread>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>
#include <CryptoExtensions.h>

#include <optional>  // for std::optional
#include <map>


using websocketpp::lib::placeholders::_1;
using websocketpp::lib::placeholders::_2;
using websocketpp::lib::bind;

typedef websocketpp::client<websocketpp::config::asio_tls_client> client;
typedef websocketpp::config::asio_tls_client::message_type::ptr message_ptr;
typedef std::shared_ptr<boost::asio::ssl::context> context_ptr;

class OkxConnector : public BaseExchangeConnector {
public: 
    // private constructor
    OkxConnector(const std::string API_key,
                 const std::string API_secret,
                 const std::string API_pass);
    // public constructor
    OkxConnector();
    ~OkxConnector();

    void connect(const std::string& url) override;
    void disconnect() override;
    
    // Unified subscribe method
    void subscribe(const std::map<std::string, std::string>& kwargs) override;

    // Unified unsubscribe method
    void unsubscribe(const std::map<std::string, std::string>& kwargs) override;

    void place_order(const std::map<std::string, std::string>& kwargs) override;

    void cancel_order(const std::map<std::string, std::string>& kwargs) override;

    // void change_order()
    // place multiple orders - задержка выставления ордера по таймингам
    // cancel all orders
    // spot feature option 

private:
    client m_client;
    std::thread m_client_thread;
    
    std::atomic<bool> m_connected{false};
    
    bool is_logged = false;

    websocketpp::connection_hdl m_hdl;
    
    CryptoExtensions cryptoExtensions;

    // API credentials (only used in private mode)
    std::string _API_key;
    std::string _API_secret;
    std::string _API_pass;

    // Flag to indicate if the connection is private
    bool is_private_connection = false;

    // Separate subscription containers for public and private modes
    std::vector<std::pair<std::string, std::string>> m_subscriptions_public;
    std::vector<std::string> m_subscriptions_private;

    context_ptr on_tls_init();
    
    // Event handlers
    void on_message(websocketpp::connection_hdl, message_ptr msg);
    void on_open_public(websocketpp::connection_hdl hdl);
    void on_open_private(websocketpp::connection_hdl hdl);
    void on_close(websocketpp::connection_hdl hdl);

    // Utility functions
    void send_message(const nlohmann::json& msg);

    std::string generate_sign(const std::string& secret, 
                              const std::string& timestamp);
    void login(const std::string& api_key,
               const std::string& secret,
               const std::string& passphrase);

    // Subscription helpers
    void subscribe_public(const std::string& channel, const std::string& inst_id);
    void subscribe_private(const std::string& channel);
    void subscribe_pending();
    void unsubscribe_public(const std::string& channel, const std::string& inst_id);
    void unsubscribe_private(const std::string& channel);

    // Order helpers
    void cancel_order(const std::string& msg_id, const std::string& ord_id, const std::string& inst_id);
    void place_order(const std::string& ord_id, const std::string& inst_id, 
                     const std::string& side, 
                     const std::string &px, const std::string& sz, 
                     const std::string& tdMode, 
                     const std::string& ccy, 
                     const std::string& ordType);
};
