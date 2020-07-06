Program that will take an input file that describes the terrain map, landing site, target sites, and characteristics of the robot. For each target site, the script will find the optimal (shortest) safe path from the landing site to that target. A path is composed of a sequence of elementary moves. Each elementary move consists of moving the rover to one of its 8 neighbors. To find the solution, the script uses the following algorithms:
- Breadth-first search (BFS)
- Uniform-cost search (UCS)
- A* search (A-star)
</b>
Return an optimal path, that is, with shortest possible operational path length. If an optimal path cannot be found, the script will return “FAIL”.