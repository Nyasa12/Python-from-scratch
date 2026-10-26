import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4,5])
y = np.array([10, 20, 25, 30, 35])

# Create a line plot
plt.plot(x, y, marker='o', color='r')

# Add title and labels
plt.title('Basic Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Show grid
plt.grid(True)

# Display the plot
plt.show()