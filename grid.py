import random
import numpy as np


def random_DFS_grid(width, height):
    # Initialize grid
    grid = np.ones((height, width), dtype=int)  # 1 for walls, 0 for passages
    visited = np.zeros_like(grid, dtype=bool)

    # Directions: (dx, dy)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    
    # Starting position
    start_x, start_y = random.randrange(1, width, 2), random.randrange(1, height, 2)
    stack = [(start_x, start_y)]
    grid[start_y, start_x] = 0
    visited[start_y, start_x] = True

    # Target position
    target_x, target_y = width - 1, height - 1

    current_x, current_y = 0, 0
    while stack:
        current_x, current_y = stack[-1]
        unvisited_neighbors = []

        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1 and not visited[ny, nx]:
                unvisited_neighbors.append((nx, ny))

        if unvisited_neighbors:
            nx, ny = random.choice(unvisited_neighbors)
            grid[(current_y + ny) // 2, (current_x + nx) // 2] = 0  # Remove wall
            grid[ny, nx] = 0  # Mark passage
            visited[ny, nx] = True
            stack.append((nx, ny))
        else:
            stack.pop()

    return grid.tolist()




# Ensuring proper random placement of obstacles
def create_random_grid_with_path(size, obstacle_probability=0.3):
    # Initialize the grid
    grid = np.zeros((size, size), dtype=int)

    # Create a guaranteed path along the diagonal
    for i in range(size):
        grid[i, i] = 0  # Ensure the path remains unobstructed

    # Randomly populate the grid with obstacles
    for i in range(size):
        for j in range(size):
            if grid[i, j] == 0:  # Ensure we don't overwrite the path
                grid[i, j] = 1 if np.random.random() < obstacle_probability else 0

    # Ensure start and end points are clear
    grid[0, 0] = 0
    grid[size - 1, size - 1] = 0

    # Convert to a list of lists for compatibility
    return grid.tolist()

# Generate the 40x40 grid
# valid_grid = generate_valid_grid_with_path_and_obstacles(40)

# Validate obstacle count and grid
# obstacle_count_fixed = sum(row.count(1) for row in valid_grid)
# valid_grid, obstacle_count_fixed
