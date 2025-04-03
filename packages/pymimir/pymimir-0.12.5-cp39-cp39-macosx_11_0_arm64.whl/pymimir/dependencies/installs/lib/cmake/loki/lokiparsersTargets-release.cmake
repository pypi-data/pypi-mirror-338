#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "loki::parsers" for configuration "Release"
set_property(TARGET loki::parsers APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(loki::parsers PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libloki_parsers.a"
  )

list(APPEND _cmake_import_check_targets loki::parsers )
list(APPEND _cmake_import_check_files_for_loki::parsers "${_IMPORT_PREFIX}/lib/libloki_parsers.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
