from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()

# Get the flower names (target names)
flower_names = iris.target_names

# Print flower names
print("Flower names in the Iris dataset:")
for name in flower_names:
    print("-", name)
