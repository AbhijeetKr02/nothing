import matplotlib.pyplot as plt

# Create some data
x = ['A','B','C','D','E']
y = [1,2,3,4,5]

# Create the bar chart
plt.bar(x, y)

# Add labels and title
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Bar Chart Example')

# Show the plot
plt.show()
