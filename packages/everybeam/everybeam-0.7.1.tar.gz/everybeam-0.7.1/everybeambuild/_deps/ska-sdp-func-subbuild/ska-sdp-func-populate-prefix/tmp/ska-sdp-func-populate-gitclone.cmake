
if(NOT "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-subbuild/ska-sdp-func-populate-prefix/src/ska-sdp-func-populate-stamp/ska-sdp-func-populate-gitinfo.txt" IS_NEWER_THAN "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-subbuild/ska-sdp-func-populate-prefix/src/ska-sdp-func-populate-stamp/ska-sdp-func-populate-gitclone-lastrun.txt")
  message(STATUS "Avoiding repeated git clone, stamp file is up to date: '/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-subbuild/ska-sdp-func-populate-prefix/src/ska-sdp-func-populate-stamp/ska-sdp-func-populate-gitclone-lastrun.txt'")
  return()
endif()

execute_process(
  COMMAND ${CMAKE_COMMAND} -E rm -rf "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-src"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to remove directory: '/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-src'")
endif()

# try the clone 3 times in case there is an odd git clone issue
set(error_code 1)
set(number_of_tries 0)
while(error_code AND number_of_tries LESS 3)
  execute_process(
    COMMAND "/usr/bin/git"  clone --no-checkout --config "advice.detachedHead=false" "https://github.com/ska-telescope/ska-sdp-func.git" "ska-sdp-func-src"
    WORKING_DIRECTORY "/var/scratch/dijkema/everybeambuild/_deps"
    RESULT_VARIABLE error_code
    )
  math(EXPR number_of_tries "${number_of_tries} + 1")
endwhile()
if(number_of_tries GREATER 1)
  message(STATUS "Had to git clone more than once:
          ${number_of_tries} times.")
endif()
if(error_code)
  message(FATAL_ERROR "Failed to clone repository: 'https://github.com/ska-telescope/ska-sdp-func.git'")
endif()

execute_process(
  COMMAND "/usr/bin/git"  checkout de91714da1e4bad78ba96cc05173ec8835a879dc --
  WORKING_DIRECTORY "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-src"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to checkout tag: 'de91714da1e4bad78ba96cc05173ec8835a879dc'")
endif()

set(init_submodules TRUE)
if(init_submodules)
  execute_process(
    COMMAND "/usr/bin/git"  submodule update --recursive --init 
    WORKING_DIRECTORY "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-src"
    RESULT_VARIABLE error_code
    )
endif()
if(error_code)
  message(FATAL_ERROR "Failed to update submodules in: '/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-src'")
endif()

# Complete success, update the script-last-run stamp file:
#
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy
    "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-subbuild/ska-sdp-func-populate-prefix/src/ska-sdp-func-populate-stamp/ska-sdp-func-populate-gitinfo.txt"
    "/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-subbuild/ska-sdp-func-populate-prefix/src/ska-sdp-func-populate-stamp/ska-sdp-func-populate-gitclone-lastrun.txt"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to copy script-last-run stamp file: '/var/scratch/dijkema/everybeambuild/_deps/ska-sdp-func-subbuild/ska-sdp-func-populate-prefix/src/ska-sdp-func-populate-stamp/ska-sdp-func-populate-gitclone-lastrun.txt'")
endif()

