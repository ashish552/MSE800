from sklearn.datasets import load_iris

iris = load_iris()

flower_names = iris.target_names

print("Flower names in the Iris dataset:")
for name in flower_names:
    print("-", name)
