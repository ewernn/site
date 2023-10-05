---
layout: default # page
title: "cs237a project"
# permalink: /URL-PATH
---
*Designed and trained autonomous wheeled robot*
**Wheeled robot mapped and navigated in simulation, stopping at stop signs and visiting specific objects using computer vision. Wrote A* for path planning, controllers for pose stabilization and trajectory tracking, and used grid mapping and point clouds for 2D and 3D SLAM.**
#### tasks
1. complete mission
	1. build a map (30seconds end to end) in simulation with pics of animals on walls, and stop signs at a couple places. The robot explored the map, returned to start, and completed a mission (go to finish line, while stopping at stop signs and visiting {list_animals})
2. visualize w/ RViz

stuff used:
- pub sub 
- A* path planning
- controllers
	- (when to do pose stabilizer vs do trajectory tracking)
- SLAM
	- 2D gmapping for A* to use
	- 3D point clouds (ROS msg_type.PointCloud2)
- RViz
	true env, robot's map of env, POV, motor speeds, planned path