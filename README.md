1. 토픽 튜토리얼 코드 작성
2. 서비스 튜토리얼 코드 작성
---------------------------------------------
패키지 생성 방법
- ros2 pkg create --build-type ament_python py_custom_service
- ros2 pkg create --build-type ament_cmake custom_interfaces

패키지 빌드 방법
- colcon build --packages-select custom_interfaces py_custom_service
- source install/setup.bash

패키지 실행 방법
- ros2 run 패키지명 작성한 코드 명

코드를 수정하면 항상 빌드를 삭제해주고 다시 재빌드
- rm -rf build/ install/ rog/
  
