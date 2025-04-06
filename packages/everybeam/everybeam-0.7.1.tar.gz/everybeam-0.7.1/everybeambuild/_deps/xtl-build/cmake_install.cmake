# Install script for directory: /var/scratch/dijkema/everybeambuild/_deps/xtl-src

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/xtl" TYPE FILE FILES
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xany.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xbasic_fixed_string.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xbase64.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xclosure.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xcompare.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xcomplex.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xcomplex_sequence.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xspan.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xspan_impl.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xdynamic_bitset.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xfunctional.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xhalf_float.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xhalf_float_impl.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xhash.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xhierarchy_generator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xiterator_base.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xjson.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xmasked_value_meta.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xmasked_value.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xmeta_utils.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xmultimethods.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xoptional_meta.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xoptional.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xoptional_sequence.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xplatform.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xproxy_wrapper.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xsequence.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xsystem.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xtl_config.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xtype_traits.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xvariant.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xvariant_impl.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-src/include/xtl/xvisitor.hpp"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/xtl" TYPE FILE FILES
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-build/xtlConfig.cmake"
    "/var/scratch/dijkema/everybeambuild/_deps/xtl-build/xtlConfigVersion.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/xtl/xtlTargets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/xtl/xtlTargets.cmake"
         "/var/scratch/dijkema/everybeambuild/_deps/xtl-build/CMakeFiles/Export/share/cmake/xtl/xtlTargets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/xtl/xtlTargets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/xtl/xtlTargets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/xtl" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/_deps/xtl-build/CMakeFiles/Export/share/cmake/xtl/xtlTargets.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pkgconfig" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/_deps/xtl-build/xtl.pc")
endif()

