cmake_minimum_required(VERSION 3.5)
project(custom_interfaces)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/AddThreeInts.srv"
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()