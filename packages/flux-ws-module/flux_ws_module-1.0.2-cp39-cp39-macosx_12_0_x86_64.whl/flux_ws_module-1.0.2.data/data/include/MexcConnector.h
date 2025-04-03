#ifndef MEXC_CONNECTOR_H
#define MEXC_CONNECTOR_H

#pragma once

#include <websocketpp/config/asio_client.hpp>
#include <websocketpp/client.hpp>
#include <BaseExchangeConnector.h>

#include <algorithm>
#include <optional>
#include <map>

#include <queue>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <thread>

#include <string>
#include <nlohmann/json.hpp>
#include <CryptoExtensions.h>
#include <map>
#include <iomanip>

using websocketpp::lib::placeholders::_1;
using websocketpp::lib::placeholders::_2;
using websocketpp::lib::bind;

typedef websocketpp::client<websocketpp::config::asio_tls_client> client;
typedef websocketpp::config::asio_tls_client::message_type::ptr message_ptr;
typedef std::shared_ptr<boost::asio::ssl::context> context_ptr;

class MexcConnector : public BaseExchangeConnector{
public:
    MexcConnector(const std::string API_url,
                   const std::string API_key,
                   const std::string API_secret);
    MexcConnector();
    ~MexcConnector();

    void connect(const std::string& url) override;
    void disconnect() override;

    void subscribe(const std::map<std::string, std::string>& kwargs) override;
    void unsubscribe(const std::map<std::string, std::string>& kwargs) override;

    void place_order(const std::map<std::string, std::string>& kwargs) override;
    void cancel_order(const std::map<std::string, std::string>& kwargs) override;

private:
    client m_client;
    std::thread m_client_thread;
    std::thread m_client_thread_ping;
    std::thread m_client_thread_refresh;

    std::atomic<bool> m_connected{false};
    
    websocketpp::connection_hdl m_hdl;
    
    std::vector<std::string> m_subscriptions_private;
    std::vector<std::tuple<std::string, std::string, std::string>> m_subscriptions_public;
    
    CryptoExtensions cryptoExtensions;
    
    context_ptr on_tls_init();

    std::string _API_url;
    std::string _API_key;
    std::string _API_secret;
    std::string _listenKey;
    std::map<std::string, std::string> _payload;

    bool is_private_connection = false;
    // Event handlers
    void on_open_private(websocketpp::connection_hdl hdl);
    void on_open_public(websocketpp::connection_hdl hdl);
    void on_close(websocketpp::connection_hdl hdl);
    void on_message(websocketpp::connection_hdl hdl, message_ptr msg);
    void send_message(const nlohmann::json& msg);

    // Order helpers
    void place_order(const std::string& ord_id, const std::string& inst_id, 
                     const std::string& side, 
                     const std::string& px, const std::string& sz, 
                     const std::string& tdMode, 
                     const std::string& ccy);
    void cancel_order(const std::string& msg_id, const std::string& ord_id, const std::string& inst_id);

    // Subscribe helpers
    void subscribe_pending();
    void subscribe_public(const std::string& host ,const std::string& symbol, const std::string& level);
    void subscribe_private(const std::string& channel);

    void unsubscribe_public(const std::string& host ,const std::string& symbol, const std::string& level);
    void unsubscribe_private(const std::string& channel);

    // Utility functions
    std::string rest_request(const std::string& type_of_request,
                             const std::string& host, 
                             const std::string& target, 
                             const std::string& api_key, const std::string& secret,
                             std::map<std::string, std::string> payload);
    std::string url_encode(const std::string &value);
    std::string map_to_url_params(const std::map<std::string, std::string>& params);
    std::string generate_signature(const std::string& secret, const std::string& message);
    void refresh_listenKey();
    void ping();
};


#endif // MEXC_CONNECTOR_H
