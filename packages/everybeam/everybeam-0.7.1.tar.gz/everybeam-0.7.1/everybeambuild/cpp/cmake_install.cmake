# Install script for directory: /home/dijkema/opt/everybeam/EveryBeam/cpp

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

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibrariesx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so"
         RPATH "/home/dijkema/opt/everybeam/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/casacore-3.4.0-d27cwqno64dyrpjp6v3wu652jkmoz7b4/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/cfitsio-3.49-oim4gsfpaxlyfauz3p6cwyglgyrdntvo/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/openblas-0.3.24-4gysi6pgs43u63olhaqltlislalgkyos/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/hdf5-1.10.7-yz644r6ded2k47gpzc2g245mq3zmb77e/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/fftw-3.3.10-i7ayzqg24e5nm7booudmxf2rds4m4bpr/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/var/scratch/dijkema/everybeambuild/cpp/libeverybeam.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so"
         OLD_RPATH "/var/scratch/dijkema/everybeambuild/cpp/hamaker:/var/scratch/dijkema/everybeambuild/cpp/oskar:/var/scratch/dijkema/everybeambuild/cpp/skamidbeam:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/casacore-3.4.0-d27cwqno64dyrpjp6v3wu652jkmoz7b4/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/cfitsio-3.49-oim4gsfpaxlyfauz3p6cwyglgyrdntvo/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/openblas-0.3.24-4gysi6pgs43u63olhaqltlislalgkyos/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/hdf5-1.10.7-yz644r6ded2k47gpzc2g245mq3zmb77e/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/fftw-3.3.10-i7ayzqg24e5nm7booudmxf2rds4m4bpr/lib:/var/scratch/dijkema/everybeambuild/cpp:/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-build:"
         NEW_RPATH "/home/dijkema/opt/everybeam/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/casacore-3.4.0-d27cwqno64dyrpjp6v3wu652jkmoz7b4/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/cfitsio-3.49-oim4gsfpaxlyfauz3p6cwyglgyrdntvo/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/openblas-0.3.24-4gysi6pgs43u63olhaqltlislalgkyos/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/hdf5-1.10.7-yz644r6ded2k47gpzc2g245mq3zmb77e/lib:/var/software/spack/opt/spack/linux-rocky8-zen2/gcc-9.4.0/fftw-3.3.10-i7ayzqg24e5nm7booudmxf2rds4m4bpr/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibrariesx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibrariesx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so"
         RPATH "/home/dijkema/opt/everybeam/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/var/scratch/dijkema/everybeambuild/cpp/libeverybeam-core.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so"
         OLD_RPATH ":::::::::::::::::::::::::::::::"
         NEW_RPATH "/home/dijkema/opt/everybeam/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libeverybeam-core.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibrariesx" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/EveryBeam" TYPE FILE FILES
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/antenna.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/beamformer.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/beamformeridenticalantennas.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/beammode.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/beamnormalisationmode.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/correctionmode.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/element.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/elementhamaker.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/elementresponse.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/msreadutils.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/station.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/load.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/options.h"
    "/home/dijkema/opt/everybeam/EveryBeam/cpp/phasedarrayresponse.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/everybeam/EveryBeamTargets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/everybeam/EveryBeamTargets.cmake"
         "/var/scratch/dijkema/everybeambuild/cpp/CMakeFiles/Export/lib/everybeam/EveryBeamTargets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/everybeam/EveryBeamTargets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/everybeam/EveryBeamTargets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/everybeam" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/cpp/CMakeFiles/Export/lib/everybeam/EveryBeamTargets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/everybeam" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/cpp/CMakeFiles/Export/lib/everybeam/EveryBeamTargets-release.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/everybeam" TYPE FILE FILES
    "/var/scratch/dijkema/everybeambuild/CMakeFiles/EveryBeamConfig.cmake"
    "/var/scratch/dijkema/everybeambuild/CMakeFiles/EveryBeamConfigVersion.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/aterms/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/circularsymmetric/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/common/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/coords/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/griddedresponse/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/hamaker/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/lobes/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/lwa/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/oskar/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/pointresponse/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/skamidbeam/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/var/scratch/dijkema/everybeambuild/cpp/telescope/cmake_install.cmake")
endif()

