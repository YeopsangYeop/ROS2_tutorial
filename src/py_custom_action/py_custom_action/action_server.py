import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from custom_interfaces.action import MoveRobot
import time

class MoveRobotActionServer(Node):
    def __init__(self):
        super().__init__('move_robot_action_server')
        self._action_server = ActionServer(
            self,
            MoveRobot,
            'move_robot',
            self.excute_callback)
        self.get_logger().info('MoveRobot Action Server ready.')

    async def excute_callback(self, goal_handle):
        self.get_logger().info(
            f'Received goal: distance = {goal_handle.request.distance} m, speed = {goal_handle.request.speed} m/s')
        feedback_msg = MoveRobot.Feedback()
        current_position = 0.0
        target_distance = goal_handle.request.distance
        speed = goal_handle.request.speed

        while current_position < target_distance:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled.')
                return MoveRobot.Result()

            current_position += speed * 0.5
            feedback_msg.current_position = current_position
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.5)

        goal_handle.succeed()
        result = MoveRobot.Result()
        result.final_position = current_position
        self.get_logger().info(f'Goal succeeded: final position = {result.final_position} m')
        return result