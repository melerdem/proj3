cmake_minimum_required(VERSION 3.10)
project(imgui_sfml_gui)

set(CMAKE_CXX_STANDARD 17)

find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)
add_subdirectory(vendor/imgui-sfml)

add_executable(imgui_sfml_gui main.cpp)
target_link_libraries(imgui_sfml_gui PRIVATE imgui-sfml sfml-graphics sfml-window sfml-system)
