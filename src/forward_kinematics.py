import math


class TwoLinkRobotArm:
    def __init__(self, link_1_length, link_2_length):
        self.link_1_length = link_1_length
        self.link_2_length = link_2_length

    def calculate_joint_positions(self, theta_1_degrees, theta_2_degrees):
        theta_1 = math.radians(theta_1_degrees)
        theta_2 = math.radians(theta_2_degrees)

        base = (0, 0)

        joint_1_x = self.link_1_length * math.cos(theta_1)
        joint_1_y = self.link_1_length * math.sin(theta_1)
        joint_1 = (joint_1_x, joint_1_y)

        end_effector_x = joint_1_x + self.link_2_length * math.cos(theta_1 + theta_2)
        end_effector_y = joint_1_y + self.link_2_length * math.sin(theta_1 + theta_2)
        end_effector = (end_effector_x, end_effector_y)

        return base, joint_1, end_effector
