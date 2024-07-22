---
layout: default # page
title: "cs237a project"
# permalink: /URL-PATH
---
# Autonomous Wheeled Robot Navigation and Mapping in Simulation

## Overview
Developed a wheeled robot capable of autonomously navigating a simulated environment decorated with images of animals and stop signs. The robot accurately mapped the area, obeyed traffic signs, and visited designated locations.

## Completed Mission

1. Explored 3D environment and generated map within 30 seconds.
2. Robot identified and interacted with specific animals and stop signs.
3. Successfully navigated to the finish line, adhering to set constraints.

## Technologies & Methods Used:

Communication: Utilized ROS publisher-subscriber model for inter-node communications.
**Path Planning**: Employed A* algorithm for efficient navigation.
**Control Systems**: Implemented pose stabilization and trajectory tracking controllers.
**Localization & Mapping**:
- 2D grid mapping for navigational decisions.
- 3D mapping with point clouds using ROS's PointCloud2 message type.
**Visualization**: Integrated with RViz for real-time visualization of environment perception, robot's internal map, point of view, motor speeds, and planned trajectory.