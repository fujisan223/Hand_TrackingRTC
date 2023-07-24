add_subdirectory(hand_tracking_checkTest)

MAP_ADD_STR(hdrs "${PROJECT_NAME}Test/" headers)
set(headers ${headers} PARENT_SCOPE)
