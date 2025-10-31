cmake_minimum_required(VERSION 3.10)
project(miifu VERSION 0.0.2 DESCRIPTION "Core Mii Implementation")

add_library(miifu SHARED
	gen/FFLResource.cpp
	gen/Ver3StoreData.cpp
)

set_target_properties(miifu PROPERTIES VERSION ${PROJECT_VERSION})
set_target_properties(miifu PROPERTIES PUBLIC_HEADER
	"include/miifu.hpp"
)

target_compile_features(miifu PRIVATE cxx_std_20)

include(GNUInstallDirs)

install(TARGETS miifu
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)
