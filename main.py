import heapq
from collections import deque
from grid import *

# Base Class for pathfinding algorithms
class Pathfinding:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0])

    def neighbors(self, node):
        x, y = node
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0:
                result.append((nx, ny))
        return result

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]

# A* Algorithm
class AStar(Pathfinding):
    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance

    def run(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {}
        g_score = {node: float('inf') for row in range(self.rows) for node in [(row, col) for col in range(self.cols)]}
        g_score[self.start] = 0
        f_score = {node: float('inf') for row in range(self.rows) for node in [(row, col) for col in range(self.cols)]}
        f_score[self.start] = self.heuristic(self.start, self.end)

        while open_list:
            current = heapq.heappop(open_list)[1]

            if current == self.end:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.end)
                    if neighbor not in [i[1] for i in open_list]:
                        heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return None

# Breadth-First Search (BFS)
class BFS(Pathfinding):
    def run(self):
        queue = deque([self.start])
        came_from = {}
        visited = {self.start}

        while queue:
            current = queue.popleft()

            if current == self.end:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

        return None

# Depth-First Search (DFS)
class DFS(Pathfinding):
    def run(self):
        stack = [self.start]
        came_from = {}
        visited = {self.start}

        while stack:
            current = stack.pop()

            if current == self.end:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    stack.append(neighbor)

        return None

# Dijkstra's Algorithm (similar to A*, but without a heuristic)
class Dijkstra(Pathfinding):
    def run(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {}
        g_score = {node: float('inf') for row in range(self.rows) for node in [(row, col) for col in range(self.cols)]}
        g_score[self.start] = 0

        while open_list:
            current = heapq.heappop(open_list)[1]

            if current == self.end:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.neighbors(current):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    if neighbor not in [i[1] for i in open_list]:
                        heapq.heappush(open_list, (g_score[neighbor], neighbor))

        return None

# Helper function to display the grid with the path
def print_grid(grid, path=None):
    temp_grid = [row[:] for row in grid]
    if path:
        for (x, y) in path:
            if (x, y) != start and (x, y) != end:
                temp_grid[x][y] = '*'
    for row in temp_grid:
        print(" ".join(str(cell) for cell in row))

# Define a 5x5 grid (0 = free, 1 = obstacle)
'''
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
'''

# You can also make a sample sized grid with the `create_grid_with_path()`
grid = create_random_grid_with_path(40)

# Start and End Points
start = (0, 0)
end = (len(grid)-1, len(grid[0])-1)

# Pathfinding options
algorithms = {
    "A*": AStar,
    "BFS": BFS,
    "DFS": DFS,
    "Dijkstra": Dijkstra
}

# Run each algorithm and display the result
for name, AlgorithmClass in algorithms.items():
    print(f"\nRunning {name} Algorithm:")
    algo = AlgorithmClass(grid, start, end)
    path = algo.run()
    if path:
        print("Path found:")
        print_grid(grid, path)
    else:
        print("No path found.")
