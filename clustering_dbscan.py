import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the data points from the CSV file
data_points = []
archer_level = []
with open('./data/data_collection.csv', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        archer_level.append(data[0])
        for i in range(2, len(data), 2):
            x, y = data[i], data[i+1]
            data_points.append((float(x), float(y)))

# Convert the data points to a NumPy array
data_arr = np.array(data_points)

def get_eps_by_archer_level(archer_level):
    if archer_level == 'novice':
        return 8
    elif archer_level == 'elementary':
        return 6
    elif archer_level == 'intermediate':
        return 5
    elif archer_level == 'advance':
        return 4


# Perform DBSCAN clustering on the data points in sets of 6
for i in range(0, len(data_arr), 6):
    subset = data_arr[i:i+6]
    level = archer_level[int(i/6)]
    eps = get_eps_by_archer_level(level) # Get the epsilon value based on the archer level
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
    target_face = plt.imread('80cm_6rings_target_face.png')

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
    ax.set_title(f"Clustered Data Points by {level} archer (eps={eps}, min_samples={min_samples})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Save the plot
    plt.savefig(f'clustered_data_points_{int(i/6)}.png')
    plt.close(fig)
