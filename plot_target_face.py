import numpy as np
import matplotlib.pyplot as plt

# Load the target face image
target_face = plt.imread('a1457853dcf807706ca2f1300d7f4fb2.png')

# Create a figure and axes
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the target face image
ax.imshow(target_face)

# Initialize the data points list
data_points = []

def save_data_points_to_csv(data_points):
    data_arr = np.array(data_points)
    with open('data_points.csv', 'a') as f:
        np.savetxt(f, data_arr, delimiter=',')
    print("Data points saved to 'data_points.csv'.")

# Function to handle mouse click events
def on_click(event):
    global data_points
    if len(data_points) < 6:
        data_points.append((event.xdata, event.ydata))
        ax.scatter(event.xdata, event.ydata, c='grey', s=50)
        print(f"Data point {len(data_points)} added: ({event.xdata:.2f}, {event.ydata:.2f})")
        if len(data_points) == 6:
            print("Set of 6 data points complete.")
            # Save the data points to a CSV file
            save_data_points_to_csv(data_points)
            # Reset the data points list
            data_points = []
            # Clear the plot
            ax.clear()
            # Plot the target face image
            ax.imshow(target_face)
            
    fig.canvas.draw()

# Connect the mouse click event handler
cid = fig.canvas.mpl_connect('button_press_event', on_click)

# Show the plot and wait for user input
plt.show()

