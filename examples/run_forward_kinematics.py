import matplotlib.pyplot as plt

from src.forward_kinematics import TwoLinkRobotArm


def plot_robot_arm(base, joint_1, end_effector):
    x_values = [base[0], joint_1[0], end_effector[0]]
    y_values = [base[1], joint_1[1], end_effector[1]]

    plt.figure()
    plt.plot(x_values, y_values, marker="o", linewidth=3, label="Robot Arm")

    plt.scatter(base[0], base[1], s=150, label="Base")
    plt.scatter(joint_1[0], joint_1[1], s=150, label="Joint 1")
    plt.scatter(end_effector[0], end_effector[1], s=150, label="End Effector")

    plt.title("2-Link Robot Arm Forward Kinematics")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.show()


def main():
    arm = TwoLinkRobotArm(link_1_length=5, link_2_length=3)

    theta_1 = 45
    theta_2 = 30

    base, joint_1, end_effector = arm.calculate_joint_positions(theta_1, theta_2)

    print("Base:", base)
    print("Joint 1:", joint_1)
    print("End Effector:", end_effector)

    plot_robot_arm(base, joint_1, end_effector)


if __name__ == "__main__":
    main()
