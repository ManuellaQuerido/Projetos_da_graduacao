file(GLOB_RECURSE RADIOLIB_SOURCES
    "${CMAKE_CURRENT_LIST_DIR}/../managed_components/jgromes__radiolib/src/*.cpp"
)
list(FILTER RADIOLIB_SOURCES EXCLUDE REGEX ".*/hal/.*\\.cpp$")

idf_component_register(
    SRCS
        "app_main.cpp"
        "lorawan.cpp"
        ${RADIOLIB_SOURCES}
    INCLUDE_DIRS
        "."
        "../managed_components/jgromes__radiolib"
        "../managed_components/jgromes__radiolib/src"
    REQUIRES
        esp_timer
        driver
)
