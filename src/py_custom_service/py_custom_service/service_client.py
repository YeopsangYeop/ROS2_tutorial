import sys
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddThreeInts

class ServiceClient(Node):
    def __init__(self):
        super().__init__('add_three_ints_client')
        self.client = self.create_client(AddThreeInts, 'add_three_ints')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('...')
            self.req = AddThreeInts.Request()

    def send_request(self, a, b, c):
        self.req.a = a
        self.req.b = b
        self.req.c = c
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    if len(sys.argv) != 4:
        print("사용법: ros2 run py_custom_service service_client a b c")
        return
    client = ServiceClient()
    result = client.send_request(int(sys.argv[1]), int(sys.argv[2]),
    int(sys.argv[3]))
    client.get_logger().info(f'결과: {result.sum}')
    client.destroy_node()
    rclpy.shutdown()
