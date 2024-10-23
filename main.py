import heapq

# A* Algorithm Class
class AStar:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start = start
        self.end = end
        self.open_list = []
        heapq.heappush(self.open_list, (0, start))  # (priority, node)
        self.came_from = {}
        self.g_score = {node: float('inf') for row in grid for node in row}
        self.g_score[start] = 0
        self.f_score = {node: float('inf') for row in grid for node in row}
        self.f_score[start] = self.heuristic(start, end)

    def heuristic(self, a, b):
        # Manhattan distance heuristic
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def neighbors(self, node):
        neighbors = []
        (x, y) = node
        if x > 0 and self.grid[x - 1][y] == 0:  # Up
            neighbors.append((x - 1, y))
        if x < len(self.grid) - 1 and self.grid[x + 1][y] == 0:  # Down
            neighbors.append((x + 1, y))
        if y > 0 and self.grid[x][y - 1] == 0:  # Left
            neighbors.append((x, y - 1))
        if y < len(self.grid[0]) - 1 and self.grid[x][y + 1] == 0:  # Right
            neighbors.append((x, y + 1))
        return neighbors

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Return reversed path

    def run(self):
        while self.open_list:
            # Get the node with the lowest f_score
            current = heapq.heappop(self.open_list)[1]

            # If the end is reached, reconstruct the path
            if current == self.end:
                return self.reconstruct_path(current)

            for neighbor in self.neighbors(current):
                tentative_g_score = self.g_score[current] + 1

                if tentative_g_score < self.g_score[neighbor]:
                    # This path is the best so far
                    self.came_from[neighbor] = current
                    self.g_score[neighbor] = tentative_g_score
                    self.f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.end)
                    if neighbor not in [i[1] for i in self.open_list]:
                        heapq.heappush(self.open_list, (self.f_score[neighbor], neighbor))

        return None  # No path found

# Helper function to display the grid with the path
def print_grid(grid, path=None):
    if path:
        for (x, y) in path:
            if (x, y) != start and (x, y) != end:
                grid[x][y] = "*"
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Define a 5x5 grid (0 = free, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Start and End Points
start = (0, 0)  # Top-left corner
end = (4, 4)    # Bottom-right corner

# Create an instance of AStar and run the algorithm
astar = AStar(grid, start, end)
path = astar.run()

# Print the grid and path
if path:
    print("Path found!")
    print_grid(grid, path)
else:
    print("No path found.")
