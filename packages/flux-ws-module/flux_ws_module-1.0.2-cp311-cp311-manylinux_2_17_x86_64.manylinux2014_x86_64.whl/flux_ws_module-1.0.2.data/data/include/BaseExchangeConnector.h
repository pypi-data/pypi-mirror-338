#pragma once

#include <string>
#include <map>
#include <any>
#include <stdexcept>
#include <vector>
#include <optional>  // for std::optional
#include <condition_variable>
#include <queue>
#include <mutex>
#include <atomic>

class BaseExchangeConnector
{
public:
    virtual ~BaseExchangeConnector() = default;

    virtual void connect(const std::string& url) = 0;
    
    virtual void disconnect() = 0;

    virtual void subscribe(const std::map<std::string, std::string>& kwargs) = 0;

    virtual void unsubscribe(const std::map<std::string, std::string>& kwargs) = 0;

    virtual void place_order(const std::map<std::string, std::string>& kwargs) = 0;

    virtual void cancel_order(const std::map<std::string, std::string>& kwargs) = 0;

protected:
    void validate_required(const std::map<std::string, std::string>& kwargs, 
                           const std::vector<std::string>& required) const {
        for (const auto& param : required) {
            if (!kwargs.count(param)) {
                throw std::invalid_argument("Missing required parameter: " + param);
            }
        }
    }

    template <typename T>
    T get_optional(const std::map<std::string, std::string>& kwargs,
                   const std::string& param, 
                   const T& default_value) const {
        return kwargs.count(param) ? kwargs.at(param) : default_value;
    }

    // Add any common members or methods that all derived classes might need
    std::atomic<bool> m_running{false};
    std::queue<std::string> m_messages;
    std::mutex m_mutex;
    std::condition_variable m_cv;

private:
    friend class WebSocketIterator;
};

class WebSocketIterator {
    public:
        explicit WebSocketIterator(BaseExchangeConnector& ws);
        std::string next();
    
    private:
        BaseExchangeConnector& m_ws;
};