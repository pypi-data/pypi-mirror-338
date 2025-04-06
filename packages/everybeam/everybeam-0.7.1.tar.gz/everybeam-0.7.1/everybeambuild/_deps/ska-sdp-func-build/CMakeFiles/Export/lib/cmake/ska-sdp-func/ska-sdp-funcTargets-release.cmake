#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ska-sdp-func::ska_sdp_func" for configuration "Release"
set_property(TARGET ska-sdp-func::ska_sdp_func APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ska-sdp-func::ska_sdp_func PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libska_sdp_func.so"
  IMPORTED_SONAME_RELEASE "libska_sdp_func.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS ska-sdp-func::ska_sdp_func )
list(APPEND _IMPORT_CHECK_FILES_FOR_ska-sdp-func::ska_sdp_func "${_IMPORT_PREFIX}/lib/libska_sdp_func.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
