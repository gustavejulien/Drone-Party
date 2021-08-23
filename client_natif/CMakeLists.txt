#################
# PREREQUISITES #
#################

cmake_minimum_required(VERSION 3.0)

project(PartyDroneControlPanel LANGUAGES CXX)
if (CMAKE_BUILD_TYPE MATCHES DEBUG)
	set(DEBUG "On")
endif (CMAKE_BUILD_TYPE MATCHES DEBUG)

#if (NOT DEFINED ${PROJECT_ROOT})
#	set(PROJECT_ROOT ${PROJECT_SOURCE_DIR})
#endif(NOT DEFINED ${PROJECT_ROOT})

## checking if GTKMM is present
find_package(PkgConfig)
pkg_check_modules(GTKMM gtkmm-3.0)

#############
#	BUILD   #
#############

set(TARGET_NAME PartyDroneControlPanel)
set(SRC
	${PROJECT_SOURCE_DIR}/src/main.cpp
	${PROJECT_SOURCE_DIR}/src/APIService.cpp
	${PROJECT_SOURCE_DIR}/src/GamePadService.cpp
	${PROJECT_SOURCE_DIR}/src/PDCPApp.cpp
	${PROJECT_SOURCE_DIR}/include/PDCPMacros.hpp
	${PROJECT_SOURCE_DIR}/include/APIService.hpp
	${PROJECT_SOURCE_DIR}/include/GamePadService.hpp
	${PROJECT_SOURCE_DIR}/include/PDCPApp.hpp
)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g3 -ggdb")

## linking GTKMM
link_directories(${GTKMM_LIBRARY_DIRS})
link_libraries(${GTKMM_LIBRARIES})

# pointing headers
include_directories(
	${GTKMM_INCLUDE_DIRS}
	${PROJECT_SOURCE_DIR}/include
)
	
# defining TARGET_NAME as executable to obtain
add_executable(${TARGET_NAME} ${SRC})
	