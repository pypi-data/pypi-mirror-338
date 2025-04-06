# Install script for directory: /home/dijkema/opt/everybeam/EveryBeam/cpp/aterms

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/dijkema/opt/everybeam")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/EveryBeam/aterms" TYPE FILE FILES
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/atermconfig.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/parsetprovider.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/cache.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/atermbase.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/atermbeam.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/atermresampler.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/fitsatermbase.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/fitsaterm.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/everybeamaterm.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/dldmaterm.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/pafbeamterm.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/h5parmaterm.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/klfittingaterm.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/aterms/fourierfittingaterm.h"
    )
endif()

