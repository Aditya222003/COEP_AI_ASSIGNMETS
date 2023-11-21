import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
# Create a figure and axis
fig, ax = plt.subplots()

# Scatter plot of sepal_length against sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])

# Set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

# Display the plot
plt.show()

# Load the Iris dataset
iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Create a color dictionary
colors = {
    'Iris-setosa': 'red',
    'Iris-versicolor': 'green',
    'Iris-virginica': 'blue'
}

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each data point with a specified color
for i in range(len(iris['sepal_length'])):
    ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i], color=colors[iris['species'][i]])

# Set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')

# Display the plot
plt.show()
