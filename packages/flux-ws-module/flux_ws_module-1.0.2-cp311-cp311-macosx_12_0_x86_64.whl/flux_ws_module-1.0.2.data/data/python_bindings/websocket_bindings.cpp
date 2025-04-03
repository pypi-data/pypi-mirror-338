#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "BaseExchangeConnector.h"
#include "CryptoExtensions.h"
#include "OkxConnector.h"
#include "MexcConnector.h"

namespace py = pybind11;

// Reusable function to convert py::kwargs to std::map<std::string, std::string>
std::map<std::string, std::string> kwargs_to_string_map(const py::kwargs& kwargs) {
    std::map<std::string, std::string> result;
    
    for (auto item : kwargs) {
        std::string key = py::cast<std::string>(item.first);
        py::handle value = item.second;
        
        if (value.is_none()) continue;
        
        try {
            if (py::isinstance<py::str>(value)) {
                result[key] = py::cast<std::string>(value);
            } else if (py::isinstance<py::int_>(value)) {
                long num = py::cast<long>(value);
                result[key] = std::to_string(num);
            } else if (py::isinstance<py::float_>(value)) {
                double num = py::cast<double>(value);
                result[key] = std::to_string(num);
            } else {
                throw py::type_error("Unsupported type for argument '" + key + "'");
            }
        } catch (const py::cast_error&) {
            throw py::type_error("Invalid type for argument '" + key + "'");
        }
    }
    
    return result;
}

void bind_WebSocketClass(py::module_ &m) {
    // Bind BaseExchangeConnector with a module-level docstring.
    py::class_<BaseExchangeConnector>(m, "BaseExchangeConnector",
        R"pbdoc(
            BaseExchangeConnector

            A base class that provides common WebSocket connection functionality.
        )pbdoc")

        .def("connect", &BaseExchangeConnector::connect,
            R"pbdoc(
                Connect to the WebSocket server.

                Parameters:
                    url (str): The URL of the WebSocket server.

                Returns:
                    A status or result of the connection attempt.
            )pbdoc", py::arg("url"))

        .def("disconnect", &BaseExchangeConnector::disconnect,
            R"pbdoc(
                Disconnect from the WebSocket server.
            )pbdoc")

        .def("subscribe", [](BaseExchangeConnector& self, const py::kwargs& kwargs) {
            self.subscribe(kwargs_to_string_map(kwargs));
        })
        
        .def("unsubscribe", [](BaseExchangeConnector& self, const py::kwargs& kwargs) {
            self.unsubscribe(kwargs_to_string_map(kwargs));
        })

        .def("place_order", [](BaseExchangeConnector& self, const py::kwargs& kwargs) {
            self.place_order(kwargs_to_string_map(kwargs));
        })

        .def("cancel_order", [](BaseExchangeConnector& self, const py::kwargs& kwargs) {
            self.cancel_order(kwargs_to_string_map(kwargs));
        })

        .def("wsrun", [](BaseExchangeConnector &self) {
            return WebSocketIterator(self);
        }, py::keep_alive<0, 1>());

    // Bind OkxConnector as the WebSocket class derived from BaseExchangeConnector.
    py::class_<OkxConnector, BaseExchangeConnector>(m, "OkxConnector",
        R"pbdoc(
            WebSocket

            A specialized connector for OKX exchanges, inheriting from BaseExchangeConnector.
        )pbdoc")

        .def(py::init<>(),
            R"pbdoc(
                Constructor for public WebSocket.
            )pbdoc")

        .def(py::init<const std::string&, const std::string&, const std::string&>(),
            R"pbdoc(
                Constructor for private WebSocket.

                Parameters:
                    API_key (str)
                    API_secret (str)
                    API_pass (str)
            )pbdoc");

    py::class_<MexcConnector, BaseExchangeConnector>(m, "MexcConnector",
        R"pbdoc(
            WebSocket

            A specialized connector for MEXC exchanges, inheriting from BaseExchangeConnector.
        )pbdoc")

        .def(py::init<>(),
            R"pbdoc(
                Constructor for public WebSocket.
            )pbdoc")
        .def(py::init<const std::string&, const std::string&, const std::string&>(),
            R"pbdoc(
                Constructor for private WebSocket.

                Parameters:
                    API_key (str)
                    API_secret (str)
                    API_pass (str)
            )pbdoc");

    py::class_<WebSocketIterator>(m, "WebSocketIterator")
        .def("__iter__", [](WebSocketIterator &it) -> WebSocketIterator& { return it; })
        .def("__next__", &WebSocketIterator::next);
}


void bind_CryptoExtensions(py::module_ &m) {
    py::class_<CryptoExtensions>(m, "CryptoExtensions")
        .def("encode64", &CryptoExtensions::encode64)
        .def("CalcHmacSHA256", &CryptoExtensions::CalcHmacSHA256);
}

PYBIND11_MODULE(_flux_ws_module, m) {
    m.doc() = R"pbdoc(
        flux_ws_module
        -------------------
        A C++ library that provides WebSocket connections to different exchanges with same interface.

        This module allows connection to WebSocket servers, subscription to channels,
        placing and cancelling orders, and includes cryptographic functions for data encoding and hashing.
    )pbdoc";

    bind_WebSocketClass(m);
    bind_CryptoExtensions(m);
}

