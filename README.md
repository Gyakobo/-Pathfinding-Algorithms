# Pathfinding Algorithms 

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

>[!NOTE]
>In this project we'll basically try to traverse a labyrinth. 

## Introduction

This project implements and compares several fundamental pathfinding algorithms in a 2D grid environment using Python. The task is to navigate from a designated start point to an endpoint on a grid where certain cells represent obstacles. The implemented algorithms are:

1. A Algorithm (A-Star)*
1. Breadth-First Search (BFS)
1. Depth-First Search (DFS)
1. Dijkstra’s Algorithm

Each algorithm has different characteristics in terms of efficiency, pathfinding strategy, and suitability for various types of problems. By simulating their performance on the same grid, we gain insights into their behaviors and differences.

### Algorithm Oversview:

The grid is represented as a matrix where `0` denotes a free cell and `1` an obstacle. The goal is to find the shortest path from the starting cell to the target cell while avoiding obstacles. The algorithms differ in how they explore the grid and how they decide the next step.

## Methodology

### [A algorithm (A-star)*](https://en.wikipedia.org/wiki/A*_search_algorithm)

Description: The A* algorithm is a popular and efficient pathfinding algorithm that combines the advantages of Dijkstra's algorithm and a heuristic approach. It uses a priority queue to always expand the node with the lowest estimated total cost.

#### How It Works:

* A* maintains two scores: g_score, which is the cost to reach a particular node, and f_score, which is the estimated total cost from the start node to the goal through that node.
* The heuristic function in A* estimates the cost from a node to the goal, typically using the Manhattan distance in grid-based environments.
* A* balances exploration and exploitation by considering both the current cost (g_score) and the heuristic (f_score), ensuring it finds an optimal path in most scenarios

#### Advantages:

* Guarantees the shortest path if a proper heuristic is used.
* Efficient and fast in most cases when compared to uninformed search algorithms.

#### Disadvantages:

* Can be slower in very complex grids with a high number of obstacles.

---

### [Breadth-First Search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search)

Description: BFS is an uninformed search algorithm that explores the grid level by level. It begins from the start node and systematically visits all neighbors of a node before moving deeper into the grid.

#### How It Works:

* BFS uses a queue data structure and visits all nodes at the same distance from the start node before proceeding to the next layer.
* Since all edges have the same weight (1 per move), BFS guarantees finding the shortest path in an unweighted grid.

#### Advantages:

* Simple to implement and guarantees the shortest path in unweighted grids.
* Efficient for small or moderately sized grids.

#### Disadvantages

* Inefficient in terms of memory usage on large grids since it needs to store a large number of nodes in memory.
* Explores many unnecessary nodes compared to algorithms like A* that use heuristics to focus on promising paths.

---

### [Depth-First Search (DFS)](https://en.wikipedia.org/wiki/Depth-first_search)

Description: DFS is another uninformed search algorithm that explores as deeply as possible before backtracking. It uses a stack data structure (often implemented recursively or via an explicit stack) to traverse the grid.

#### How It Works:
 
* DFS starts at the root (start node) and explores as far as it can along a branch (neighboring nodes) before backtracking.
* DFS does not guarantee the shortest path in most cases as it does not systematically explore nodes based on distance.

#### Advantages:

* DFS is useful in cases where memory usage is critical because it typically requires less memory than BFS.
* It can be adapted to explore large depth-limited grids or mazes.

#### Disadvantages:

* DFS may explore long, inefficient paths and may miss shorter, more direct paths, especially in cases where the grid has a high branching factor.
* It can get stuck in deep irrelevant paths before finding a solution. 

---

### [Dijkstra's Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

Description: Dijkstra's algorithm is a weighted graph search algorithm that systematically finds the shortest path from the start node to all other nodes in the grid. In unweighted grids, Dijkstra behaves similarly to BFS but uses a priority queue to expand nodes.

#### How It Works:

* Dijkstra’s algorithm uses a priority queue to expand the node with the lowest current known distance `g_score`.
* All nodes start with an infinite distance except the start node, which starts with zero. The algorithm keeps expanding the node with the smallest distance until it reaches the target node.

#### Advantages:

* Guarantees the shortest path in all types of graphs (weighted and unweighted).
* Efficient for unweighted grids, though BFS may perform similarly in these cases.

#### Disadvantages:

* In a grid where all edges have equal weights, Dijkstra’s algorithm doesn’t outperform BFS but is more computationally expensive due to priority queue operations.
* Slower than A* in many cases, as it doesn’t use a heuristic to prioritize exploration.

## Results

The following is an example of the [main.py](https://github.com/Gyakobo/Pathfinding-Algorithms/blob/main/main.py) in action

```bash
# Running A* Algorithm:
# Path found:
0 1 0 0 0
* 1 0 1 0
* 0 0 1 0
* 1 1 0 0
* * * * 0

# Running BFS Algorithm:
# Path found:
0 1 0 0 0
* 1 0 1 0
* 0 0 1 0
* 1 1 0 0
* * * * 0

# Running DFS Algorithm:
# Path found:
0 1 0 0 0
* 1 0 1 0
* 0 0 1 0
* 1 1 0 0
* * * * 0

# Running Dijkstra Algorithm:
# Path found:
0 1 0 0 0
* 1 0 1 0
* 0 0 1 0
* 1 1 0 0
* * * * 0
```

## Conclusion

Each algorithm approaches the pathfinding problem with different strategies, leading to varying levels of efficiency and effectiveness:

* A* Algorithm is the most efficient for finding the shortest path in most practical grid scenarios due to its use of both distance and heuristic measures. It finds the shortest path quickly by balancing cost and future estimates.
* BFS guarantees finding the shortest path in unweighted grids, though it can be inefficient for large grids.
* DFS is not suitable for finding the shortest path in most cases, as it often explores irrelevant paths. However, it uses less memory compared to BFS.
* Dijkstra's Algorithm is thorough and guarantees the shortest path, but in the context of unweighted grids, it doesn’t offer significant advantages over BFS and is slower than A*.

By comparing the algorithms, we see that the choice of algorithm depends on the grid structure and the requirements for efficiency, memory usage, and optimality of the solution. In scenarios where a heuristic can be defined (as in grid-based pathfinding), A* is typically the best choice. However, BFS is useful for simpler grids, and DFS is useful in memory-constrained environments.

## License
MIT
