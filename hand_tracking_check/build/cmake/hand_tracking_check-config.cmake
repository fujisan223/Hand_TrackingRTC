# hand_tracking_check CMake config file
#
# This file sets the following variables:
# hand_tracking_check_FOUND - Always TRUE.
# hand_tracking_check_INCLUDE_DIRS - Directories containing the hand_tracking_check include files.
# hand_tracking_check_IDL_DIRS - Directories containing the hand_tracking_check IDL files.
# hand_tracking_check_LIBRARIES - Libraries needed to use hand_tracking_check.
# hand_tracking_check_DEFINITIONS - Compiler flags for hand_tracking_check.
# hand_tracking_check_VERSION - The version of hand_tracking_check found.
# hand_tracking_check_VERSION_MAJOR - The major version of hand_tracking_check found.
# hand_tracking_check_VERSION_MINOR - The minor version of hand_tracking_check found.
# hand_tracking_check_VERSION_REVISION - The revision version of hand_tracking_check found.
# hand_tracking_check_VERSION_CANDIDATE - The candidate version of hand_tracking_check found.

message(STATUS "Found hand_tracking_check-1.0.0")
set(hand_tracking_check_FOUND TRUE)

find_package(<dependency> REQUIRED)

#set(hand_tracking_check_INCLUDE_DIRS
#    "C:/Program Files/OpenRTM-aist/2.0.1/cmake/../Components/c++/Category/include/hand_tracking_check-1"
#    ${<dependency>_INCLUDE_DIRS}
#    )
#
#set(hand_tracking_check_IDL_DIRS
#    "C:/Program Files/OpenRTM-aist/2.0.1/cmake/../Components/c++/Category/include/hand_tracking_check-1/idl")
set(hand_tracking_check_INCLUDE_DIRS
    "C:/Program Files/OpenRTM-aist/2.0.1/cmake/../Components/c++/Category/include/"
    ${<dependency>_INCLUDE_DIRS}
    )
set(hand_tracking_check_IDL_DIRS
    "C:/Program Files/OpenRTM-aist/2.0.1/cmake/../Components/c++/Category/include//idl")


if(WIN32)
    set(hand_tracking_check_LIBRARIES
        "C:/Program Files/OpenRTM-aist/2.0.1/cmake/../Components/c++/Category//hand_tracking_check.lib"
        ${<dependency>_LIBRARIES}
        )
else(WIN32)
    set(hand_tracking_check_LIBRARIES
        "C:/Program Files/OpenRTM-aist/2.0.1/cmake/../Components/c++/Category//hand_tracking_check.dll"
        ${<dependency>_LIBRARIES}
        )
endif(WIN32)

set(hand_tracking_check_DEFINITIONS ${<dependency>_DEFINITIONS})

set(hand_tracking_check_VERSION 1.0.0)
set(hand_tracking_check_VERSION_MAJOR 1)
set(hand_tracking_check_VERSION_MINOR 0)
set(hand_tracking_check_VERSION_REVISION 0)
set(hand_tracking_check_VERSION_CANDIDATE )

