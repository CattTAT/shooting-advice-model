import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the data points from the CSV file
data_points = []
with open('data_points.csv', 'r') as f:
    for line in f:
        x, y = line.strip().split(',')
        data_points.append((float(x), float(y)))

# Convert the data points to a NumPy array
data_arr = np.array(data_points)

# Perform DBSCAN clustering on the data points in sets of 6
for i in range(0, len(data_arr), 6):
    subset = data_arr[i:i+6]
    eps = 4 # 4 cm for advanced/ intermediate archers
    min_samples = 2
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(subset)

    # Print the clustering results
    print(f"Clustering results for data points {i+1} to {min(i+6, len(data_arr))}:")
    unique_labels = set(labels)
    num_clusters = len(unique_labels) - (1 if -1 in labels else 0)
    print(f"Number of clusters: {num_clusters}")
    for label in unique_labels:
        if label == -1:
            print(f"Noise points: {sum(labels == label)}")
        else:
            print(f"Cluster {label}: {sum(labels == label)} points")

    # Plot the clustered data points
    target_face = plt.imread('a1457853dcf807706ca2f1300d7f4fb2.png')

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the target face image
    ax.imshow(target_face, extent=[0, 48, 0, 48])
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    for label, color in zip(unique_labels, colors):
        if label == -1:
            color = [0, 0, 0, 1]
        class_member_mask = (labels == label)
        xy = subset[class_member_mask]
        ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(color), markeredgecolor='k', markersize=14)
    ax.set_title(f"Clustered Data Points (eps={eps}, min_samples={min_samples})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.show()