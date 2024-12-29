import random
import numpy as np

def create_grid_with_path(size):
    # Initialize the grid with zeros
    grid = [[0 for _ in range(size)] for _ in range(size)]
    
    # Create a guaranteed path from top-left to bottom-right
    for i in range(size):
        grid[i][i] = 0  # Set the diagonal path
    
    # Randomly add obstacles while preserving the guaranteed path
    for i in range(size):
        for j in range(size):
            if grid[i][j] != 0:  # Avoid placing obstacles on the guaranteed path
                grid[i][j] = random.choice([0, 1])  # Randomly assign 0 or 1
    
    # Set start and end points explicitly
    grid[0][0] = 0
    grid[size - 1][size - 1] = 0
    
    return grid

# Create a 40x40 grid with a guaranteed path
# sample_grid = create_grid_with_path(40)

# Display the sample grid
# sample_grid
