import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddThreeInts

class ServiceServer(Node):
    def __init__(self):
        super().__init__('add_three_ints_server')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.callback)
        self.get_logger().info('...')

    def callback(self, request, response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info(f' : {request.a} + {request.b} + {request.c} = {response.sum}')
        return response

def main(args = None):
    rclpy.init(args=args)
    node = ServiceServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()