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

