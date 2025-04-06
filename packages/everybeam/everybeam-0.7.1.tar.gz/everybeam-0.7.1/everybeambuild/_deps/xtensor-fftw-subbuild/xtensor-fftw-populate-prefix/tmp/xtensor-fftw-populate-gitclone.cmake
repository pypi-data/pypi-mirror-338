
if(NOT "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-subbuild/xtensor-fftw-populate-prefix/src/xtensor-fftw-populate-stamp/xtensor-fftw-populate-gitinfo.txt" IS_NEWER_THAN "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-subbuild/xtensor-fftw-populate-prefix/src/xtensor-fftw-populate-stamp/xtensor-fftw-populate-gitclone-lastrun.txt")
  message(STATUS "Avoiding repeated git clone, stamp file is up to date: '/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-subbuild/xtensor-fftw-populate-prefix/src/xtensor-fftw-populate-stamp/xtensor-fftw-populate-gitclone-lastrun.txt'")
  return()
endif()

execute_process(
  COMMAND ${CMAKE_COMMAND} -E rm -rf "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-src"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to remove directory: '/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-src'")
endif()

# try the clone 3 times in case there is an odd git clone issue
set(error_code 1)
set(number_of_tries 0)
while(error_code AND number_of_tries LESS 3)
  execute_process(
    COMMAND "/usr/bin/git"  clone --no-checkout --config "advice.detachedHead=false" "https://github.com/xtensor-stack/xtensor-fftw.git" "xtensor-fftw-src"
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
  message(FATAL_ERROR "Failed to clone repository: 'https://github.com/xtensor-stack/xtensor-fftw.git'")
endif()

execute_process(
  COMMAND "/usr/bin/git"  checkout e6be85a376624da10629b6525c81759e02020308 --
  WORKING_DIRECTORY "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-src"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to checkout tag: 'e6be85a376624da10629b6525c81759e02020308'")
endif()

set(init_submodules TRUE)
if(init_submodules)
  execute_process(
    COMMAND "/usr/bin/git"  submodule update --recursive --init 
    WORKING_DIRECTORY "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-src"
    RESULT_VARIABLE error_code
    )
endif()
if(error_code)
  message(FATAL_ERROR "Failed to update submodules in: '/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-src'")
endif()

# Complete success, update the script-last-run stamp file:
#
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-subbuild/xtensor-fftw-populate-prefix/src/xtensor-fftw-populate-stamp/xtensor-fftw-populate-gitinfo.txt"
    "/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-subbuild/xtensor-fftw-populate-prefix/src/xtensor-fftw-populate-stamp/xtensor-fftw-populate-gitclone-lastrun.txt"
  RESULT_VARIABLE error_code
  )
if(error_code)
  message(FATAL_ERROR "Failed to copy script-last-run stamp file: '/var/scratch/dijkema/everybeambuild/_deps/xtensor-fftw-subbuild/xtensor-fftw-populate-prefix/src/xtensor-fftw-populate-stamp/xtensor-fftw-populate-gitclone-lastrun.txt'")
endif()

