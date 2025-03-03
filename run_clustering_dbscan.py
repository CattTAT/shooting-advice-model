import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import output.dbscan_ouput as dbscan_ouput

def get_eps_by_archer_level(archer_level):
    if archer_level == 'novice':
        return 8
    elif archer_level == 'elementary':
        return 7
    elif archer_level == 'intermediate':
        return 5
    elif archer_level == 'advance':
        return 4
    
# Load the data points from the CSV file
def run(archer_level, archer_eye, arrow_locations):
    # Convert the data points to a NumPy array
    data_arr = np.array(arrow_locations)

    # Perform DBSCAN clustering on the data points in sets of 6
    for i in range(0, len(data_arr), 6):
        subset = data_arr[i:i+6]
        level = archer_level
        eye = archer_eye
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

        # Save the clustering results to a CSV file
        output = dbscan_ouput.dbscan_output(level, eye, num_clusters, grouping_size[0], result_center[0] ,grouping_size[1], result_center[1],grouping_size[2], result_center[2])
        return output
