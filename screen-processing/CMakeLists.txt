cmake_minimum_required(VERSION 2.8) 
PROJECT (averagecolor)
find_package(OpenCV REQUIRED )
set( AVERAGECOLOR_SRC
    src/average-color.cpp    
)

set( AVERAGECOLOR_HEADERS       
     lib/core.hpp
     lib/highgui.hpp
     lib/imgproc.hpp
     lib/opencv.hpp
)

INCLUDE_DIRECTORIES( ${CMAKE_CURRENT_SOURCE_DIR}/lib )
link_directories( ${CMAKE_BINARY_DIR}/bin)
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
add_executable( averagecolor ${AVERAGECOLOR_SRC} ${AVERAGECOLOR_HEADERS} )

target_link_libraries(averagecolor ${OpenCV_LIBS})
