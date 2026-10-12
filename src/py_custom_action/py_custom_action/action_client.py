import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from custom_interfaces.action import MoveRobot

class MoveRobotActionClient(Node):
    def __init__(self):
        super().__init__('move_robot_action_client')
        self._action_client = ActionClient(self, MoveRobot, 'move_robot')
        self.goal_handle = None

    def send_goal(self, distance, speed):
        goal_msg = MoveRobot.Goal()
        goal_msg.distance = distance
        goal_msg.speed = speed

        self.get_logger().info(f'Sending goal: distance = {distance} m, speed = {speed} m/s')
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Current position: {feedback.current_position} m')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected.')
            return

        self.get_logger().info('Goal accepted.')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Final position: {result.final_position} m')

    def cancel_goal(self):
        if self.goal_handle:
            self.get_logger().info('Canceling goal...')
            cancel_future = self.goal_handle.cancel_goal_async()
            cancel_future.add_done_callback(self.cancel_response_callback)

    def cancel_done_callback(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Goal canceled successfully.')
        else:
            self.get_logger().info('Goal cancelation failed or no goal to cancel.')

def main(args=None):
    rclpy.init(args=args)
    client = MoveRobotActionClient()
    client.send_goal(distance=5.0, speed=0.5)
    rclpy.spin(client)
    client.destroy_node()
    rclpy.shutdown()