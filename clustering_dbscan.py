import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# Load the data points from the CSV file
data_points = []
archer_level = []
archer_eye = []
with open('./data/data_collection.csv', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        archer_level.append(data[0])
        archer_eye.append(data[1])
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
    
def  save_data_to_csv(data):
    print(data)
    with open('./data/to_build_decision_tree.csv', 'a') as f:
        np.savetxt(f, [data], fmt='%s', delimiter=',')
    print("Data points saved to 'to_build_decision_tree.csv'.")


# Perform DBSCAN clustering on the data points in sets of 6
for i in range(0, len(data_arr), 6):
    subset = data_arr[i:i+6]
    level = archer_level[int(i/6)]
    eye = archer_eye[int(i/6)]
    eps = get_eps_by_archer_level(level) # Get the epsilon value based on the archer level
    min_samples = 2
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(subset)

    # Print the clustering results
    print(f"Clustering results for data points {i+1} to {min(i+6, len(data_arr))}:")
    unique_labels = set(labels)
    num_clusters = len(unique_labels) - (1 if -1 in labels else 0)
    print(f"Number of clusters: {num_clusters}")
    distance_vector = [None, None, None]
    result_center = [None, None, None]
    grouping_size = [None, None, None]
    target_center = np.array([24.0, 24.0])
    for label in unique_labels:
        if label == -1:
            print(f"Noise points: {sum(labels == label)}")
        else:
            result = subset[labels == label]
            result_center[label] = np.mean(result, axis=0)
            distance = result_center[label] - target_center
            distance_vector[label] = distance
            grouping_size[label] = sum(labels == label)
            print(f"Cluster {label} center: {result_center}")
            print(f"Cluster {label} distance: {distance}")
            print(f"Cluster {label}: {sum(labels == label)} points")

    def to_string(arr):
        if arr is None:
            return None
        else:
            result = "\"" + str(arr[0]) + "," + str(arr[1]) + "\""
            return result

    # Save the clustering results to a CSV file
    data = [level, eye, num_clusters, grouping_size[0], to_string(distance_vector[0]),grouping_size[1], to_string(distance_vector[1]),grouping_size[2], to_string(distance_vector[2])]
    save_data_to_csv(data)

    # Plot the clustered data points
    target_face = plt.imread('80cm_6rings_target_face.png')

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the target face image
    ax.imshow(target_face, extent=[0, 48, 0, 48])
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    ax.scatter(target_center[0],target_center[1], color='r', marker='x', s=50, label='target center', zorder=10)
    for label, color in zip(unique_labels, colors):
        if label == -1:
            color = [0, 0, 0, 1]
        class_member_mask = (labels == label)
        xy = subset[class_member_mask]
        ax.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(color), markeredgecolor='k', markersize=14)

        #Plot the distance vector from the reference point to the cluster center
        ax.arrow(target_center[0],target_center[1],
                distance_vector[label][0], distance_vector[label][1],
                color='r', length_includes_head=True, head_width=1, head_length=0.5, linewidth=2, zorder=10, overhang=0.5)
    ax.set_title(f"Clustered Data Points by {level} archer (eps={eps}, min_samples={min_samples})")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Save the plot
    plt.savefig(f'clustered_data_points_{int(i/6)}.png')
    plt.close(fig)
    # plt.show()
