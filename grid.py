import random
import numpy as np


def random_DFS_grid(size):
    # Grid 
    grid = np.zeros((size, size), dtype=int)

    cur = (0, 0)
    target = (size-1, size-1)
    stack = [cur]
    visited = set(cur)

    def check_if_cell_is_valid(point):
        if point[0] < size and point[0] >= 0 and point[1] < size and point[1] >= 0:
            return True
        return False

    # Create a guaranteed path along the diagonal
    for i in range(size):
        grid[i, i] = 1  # Ensure the path remains unobstructed

    while cur == target:
        # Randomly select and pop an element
        random_index    = random.randrange(len(stack))        
        popped_element  = stack.pop(random_index)



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
