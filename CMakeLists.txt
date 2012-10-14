# http://qt-project.org/quarterly/view/using_cmake_to_build_qt_projects
# http://qt-quarterly.developpez.com/qq-34/cmake/

cmake_minimum_required(VERSION 2.6.0)

project(Visu)

#add_subdirectory(Box2D_v2.2.1)
#include_directories(${Box2D_SOURCE_DIR})

set(LIBRARY_OUTPUT_PATH lib/${CMAKE_BUILD_TYPE})




file(GLOB sources "*.cpp")
file(GLOB cmd_sources "cmd/*.cpp")

include_directories(${CMAKE_CURRENT_BINARY_DIR})
include_directories(.)

add_library(cmdvisu
    SHARED
    ${sources}
    ${cmd_sources}
)

add_executable(visuTest
    ${sources}
    ${cmd_sources}
)

set(CMAKE_CXX_FLAGS "-g -Wall -ggdb")
