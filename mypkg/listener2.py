import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


def cb(msg):
    global Node
    node.get_logger().info("Listen: %d" % msg)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "person", cb, 10)   
rclpy.spin(node)
