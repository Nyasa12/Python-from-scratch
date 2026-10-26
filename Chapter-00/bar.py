import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create a bar plot
plt.bar(categories, values, color='pink')

# Add title and labels
plt.title('Basic Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show grid
plt.grid(axis='y', linestyle='--', alpha = 0.7 )

# Display the plot
plt.show()







#vertical bar
import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create a bar plot
plt.barh(categories, values, color='pink')

# Add title and labels
plt.title('Basic Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show grid
plt.grid(axis='x', linestyle='--', alpha = 0.7 )

# Display the plot
plt.show()
