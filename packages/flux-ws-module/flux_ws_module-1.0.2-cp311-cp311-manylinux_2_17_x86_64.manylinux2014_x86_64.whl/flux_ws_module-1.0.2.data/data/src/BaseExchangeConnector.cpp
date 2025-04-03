#include "BaseExchangeConnector.h"
#include <string>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <thread>
#include <string>
#include <vector>

#ifdef WITH_PYTHON  // Defined when building Python bindings
#include <pybind11/pybind11.h>
namespace py = pybind11;
#endif


// Iterator implementation
WebSocketIterator::WebSocketIterator(BaseExchangeConnector& ws) : m_ws(ws) {}

std::string WebSocketIterator::next() {
    #ifdef WITH_PYTHON
        py::gil_scoped_release release;  // Release GIL only in Python mode
    #endif

    std::unique_lock<std::mutex> lock(m_ws.m_mutex);
    m_ws.m_cv.wait(lock, [this] {
        return !m_ws.m_messages.empty() || !m_ws.m_running.load();
    });

    if (!m_ws.m_running.load() && m_ws.m_messages.empty()) {
        #ifdef WITH_PYTHON
            throw py::stop_iteration();  // Python-specific exception
        #else
            throw std::runtime_error("No more messages");  // C++ exception
        #endif
    }

    auto msg = m_ws.m_messages.front();
    m_ws.m_messages.pop();
    return msg;
}