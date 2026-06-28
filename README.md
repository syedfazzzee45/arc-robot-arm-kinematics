# ARC Robot Arm Kinematics

ARC Robot Arm Kinematics is the robotic arm motion module for the ARC robotics stack.

This repository focuses on forward kinematics, joint angles, end-effector position, and trajectory visualization for simple robotic arm systems. It is designed to build the mechanical robotics layer of the larger ARC robotics ecosystem.

## Project Goals

- Build a 2D robotic arm simulation
- Calculate end-effector position using forward kinematics
- Visualize joint movement and arm position
- Experiment with different joint angles and link lengths
- Create a foundation for inverse kinematics and trajectory planning

## Why This Project Matters

Robotic arms are used in manufacturing, automation, assistive robotics, surgical robotics, warehouse systems, and industrial manipulation.

To control a robotic arm, the system needs to understand how joint angles affect the position of the end-effector. This project starts with forward kinematics, which is one of the core foundations of robotics and mechatronics.

## Planned Features

- 2-link robotic arm simulation
- Forward kinematics calculation
- End-effector position tracking
- Arm visualization using Matplotlib
- Joint angle experiments
- Future inverse kinematics module
- Future trajectory planning module

## Tech Stack

- Python
- NumPy
- Matplotlib
- Robotics kinematics concepts
- Mechanical systems simulation concepts

## Current Status

Initial repository created.

Next step: add a basic 2-link robotic arm forward kinematics simulation.


## How to Run

Install dependencies:

pip install -r requirements.txt

Run the forward kinematics simulation:

PYTHONPATH=. python3 examples/run_forward_kinematics.py

## Demo Output

2-Link Robot Arm Forward Kinematics

This simulation calculates the base, joint, and end-effector positions of a 2-link robotic arm using forward kinematics.

## Current Features

* 2-link robotic arm model
* Forward kinematics calculation
* Joint angle input
* End-effector position calculation
* Robot arm visualization using Matplotlib
