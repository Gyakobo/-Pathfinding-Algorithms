import heapq

# A* Algorithm Class
class AStar:
    def __init__(self, grid, start, end):
        # Grid 
        self.grid = grid

        # Positions
        self.start  = start
        self.end    = end

        self.open_list = []
        heapq.heappush(self.open_list, (0, start)) # (priority, node)

def print_grid(grid, path=None):
    if path:
        for (x, y) in path:
            if (x, y) != start and (x, y) != end:
                grid[x][y] = "*"
        for row in grid:
            print(" ".join(str(cell)) for cell in row)

# Define a 5x5 grid (0 = false, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
start = (4, 4)


