# INITIAL SETTINGS
cmake_minimum_required(VERSION 3.15)

if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake" 
        CACHE STRING "Vcpkg toolchain file")
endif()

if(DEFINED ENV{VCPKG_INSTALLATION_ROOT})
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_INSTALLATION_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "Vcpkg toolchain file")
endif()

project(flux_ws_module LANGUAGES CXX)

# --------------- Compiler Settings ---------------
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)  # Global PIC for all targets

if(MSVC)
    add_compile_options(/std:c++20 /permissive-)
    add_compile_definitions(_WEBSOCKETPP_CPP11_RANDOM_DEVICE_)
    add_compile_options(/Zc:__cplusplus)  # Fix __cplusplus macro
    add_compile_options(/bigobj)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()


# --------------- Python Configuration ---------------
# cmake_policy(SET CMP0094 NEW)
# set(Python_FIND_VIRTUALENV FIRST)
# set(Python_FIND_STRATEGY LOCATION)
if(POLICY CMP0148)
  cmake_policy(SET CMP0148 NEW)
endif()

# ------------------------------------------------------
# FIND TOOLS
include(GNUInstallDirs)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
message(STATUS "TOOL: ${CMAKE_TOOLCHAIN_FILE}")
# set(PYBIND11_FINDPYTHON ON) 

# ------------------------------------------------------
# FIND DEPENDENCIES
# find_package(Python REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)

find_package(Boost REQUIRED COMPONENTS 
     system 
     date_time 
     serialization
     algorithm
     beast
)
find_package(websocketpp REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(OpenSSL REQUIRED)

# ------------------------------------------------------
# PROJECT

add_library(flux_core STATIC  # <-- FIX: Create core library first
    ${CMAKE_CURRENT_SOURCE_DIR}/src/BaseExchangeConnector.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/OkxConnector.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/CryptoExtensions.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/MexcConnector.cpp
)

target_include_directories(flux_core PUBLIC  # <-- FIX: Public includes
    ${PROJECT_SOURCE_DIR}/include
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

target_link_libraries(flux_core PUBLIC  # <-- FIX: Core dependencies
    Boost::system 
    Boost::date_time
    Boost::serialization
    Boost::algorithm
    Boost::beast
    OpenSSL::SSL 
    OpenSSL::Crypto
    websocketpp::websocketpp
    nlohmann_json::nlohmann_json
    pybind11::module
)

# -------------------------------------
# CREATE PYTHON BINDINGS MODULE
pybind11_add_module(flux_ws_module
    ${CMAKE_CURRENT_SOURCE_DIR}/python_bindings/websocket_bindings.cpp  # <-- FIX: Only bindings here
)

target_link_libraries(flux_ws_module PRIVATE
    flux_core  # <-- FIX: Link to core library
    pybind11::module
)

# Handle Python library linking based on type
if(TARGET Python::Python)
    target_link_libraries(flux_ws_module PRIVATE Python::Python)
else()
    target_link_libraries(flux_ws_module PRIVATE ${Python_LIBRARIES})
    target_include_directories(flux_ws_module PRIVATE ${Python_INCLUDE_DIRS})
endif()

# -------------------------------------
# TARGET FINAL SETTINGS
set_target_properties(flux_ws_module PROPERTIES
    POSITION_INDEPENDENT_CODE ON  # Optional but recommended
    SUFFIX ""               # Remove default extension
    OUTPUT_NAME "_flux_ws_module"  # Set base name
)

# Platform-specific extensions (CMake will handle automatically)
if(WIN32)
    set_target_properties(flux_ws_module PROPERTIES SUFFIX ".pyd")
else()
    set_target_properties(flux_ws_module PROPERTIES SUFFIX ".so")
endif()

# ------------------------------------------------------------------
# Installation rules
#
# This install() command is required by scikit-build so that
# pip install . -v can run an "install" target.

install(TARGETS flux_ws_module
    LIBRARY DESTINATION flux_ws_module
    ARCHIVE DESTINATION flux_ws_module
    RUNTIME DESTINATION flux_ws_module
)

# -------------------------
# TEST FILES
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    file(GLOB TEST_SOURCES "lib_tests/*.cpp")

    foreach(test_source ${TEST_SOURCES})
        get_filename_component(test_name ${test_source} NAME_WE)
        add_executable(${test_name} ${test_source})
        
        target_link_libraries(${test_name} PRIVATE 
            flux_core
            pybind11::module
            pybind11::embed
        )
    endforeach()
endif()