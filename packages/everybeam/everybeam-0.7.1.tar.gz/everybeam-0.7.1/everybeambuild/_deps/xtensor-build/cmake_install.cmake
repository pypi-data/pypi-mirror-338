# Install script for directory: /var/scratch/dijkema/everybeambuild/_deps/xtensor-src

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/xtensor" TYPE FILE FILES
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xaccessible.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xaccumulator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xadapt.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xarray.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xassign.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xaxis_iterator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xaxis_slice_iterator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xblockwise_reducer.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xblockwise_reducer_functors.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xbroadcast.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xbuffer_adaptor.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xbuilder.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xchunked_array.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xchunked_assign.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xchunked_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xcomplex.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xcontainer.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xcsv.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xdynamic_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xeval.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xexception.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xexpression.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xexpression_holder.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xexpression_traits.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xfixed.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xfunction.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xfunctor_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xgenerator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xhistogram.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xindex_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xinfo.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xio.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xiterable.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xiterator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xjson.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xlayout.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xmanipulation.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xmasked_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xmath.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xmime.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xmultiindex_iterator.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xnoalias.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xnorm.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xnpy.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xoffset_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xoperation.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xoptional.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xoptional_assembly.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xoptional_assembly_base.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xoptional_assembly_storage.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xpad.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xrandom.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xreducer.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xrepeat.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xscalar.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xsemantic.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xset_operation.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xshape.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xslice.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xsort.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xstorage.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xstrided_view.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xstrided_view_base.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xstrides.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xtensor.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xtensor_config.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xtensor_forward.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xtensor_simd.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xutils.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xvectorize.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xview.hpp"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-src/include/xtensor/xview_utils.hpp"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/cmake/xtensor" TYPE FILE FILES
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-build/xtensorConfig.cmake"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-build/xtensorConfigVersion.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/xtensor/xtensorTargets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/xtensor/xtensorTargets.cmake"
         "/var/scratch/dijkema/everybeambuild/_deps/xtensor-build/CMakeFiles/Export/lib64/cmake/xtensor/xtensorTargets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/xtensor/xtensorTargets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib64/cmake/xtensor/xtensorTargets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/cmake/xtensor" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/_deps/xtensor-build/CMakeFiles/Export/lib64/cmake/xtensor/xtensorTargets.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib64/pkgconfig" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/_deps/xtensor-build/xtensor.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES "/var/scratch/dijkema/everybeambuild/xtensor.hpp")
endif()

