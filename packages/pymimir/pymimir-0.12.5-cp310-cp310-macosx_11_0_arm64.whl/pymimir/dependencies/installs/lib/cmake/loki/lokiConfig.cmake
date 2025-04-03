
####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was Config.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

####################################################################################

include(CMakeFindDependencyMacro)


##############################################################
# Debug prints
##############################################################

message("CMAKE_PREFIX_PATH: ${CMAKE_PREFIX_PATH}")


##############################################################
# CMake modules and macro files
##############################################################

include("${CMAKE_CURRENT_LIST_DIR}/cmake/configure_boost.cmake")


##############################################################
# Dependency Handling
##############################################################

# Boost
# Find Boost headers only according to https://cmake.org/cmake/help/latest/module/FindBoost.html
configure_boost()
find_dependency(Boost ${BOOST_MIN_VERSION} REQUIRED PATHS ${CMAKE_PREFIX_PATH} NO_DEFAULT_PATH)
if(Boost_FOUND)
  include_directories(${Boost_INCLUDE_DIRS})
  message(STATUS "Found Boost: ${Boost_DIR} (found version ${Boost_VERSION})")
endif()


# -----------
# abseil
# -----------

find_dependency(absl CONFIG REQUIRED PATHS ${CMAKE_PREFIX_PATH} NO_DEFAULT_PATH)
if(absl_FOUND)
  include_directories(${absl_INCLUDE_DIRS})
  message(STATUS "Found absl: ${absl_DIR} (found version ${absl_VERSION})")
endif()


############
# Components
############

set(_loki_supported_components parsers)

foreach(_comp ${loki_FIND_COMPONENTS})
  if (NOT _comp IN_LIST _loki_supported_components)
    set(loki_FOUND False)
    set(loki_NOT_FOUND_MESSAGE "Unsupported component: ${_comp}")
  endif()
  include("${CMAKE_CURRENT_LIST_DIR}/loki${_comp}Targets.cmake")
endforeach()

get_filename_component(LOKI_CONFIG_DIR ${CMAKE_CURRENT_LIST_FILE} PATH)
message(STATUS "Found loki: ${loki_DIR} (found version ${loki_VERSION})")
