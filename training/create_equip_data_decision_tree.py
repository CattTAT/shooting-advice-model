import numpy as np
import matplotlib.pyplot as plt

# Load the target face image
target_face = plt.imread('zoned_80cm6rings_target_face.png')

# Initialize the data points list
num_of_grouping = 1 
data = []
arrow_recorded = 0

def init_data():
    global data
    grouping_size = [6, None, None]
    equip_results = '\"4,9\"'
    data = [num_of_grouping, grouping_size[0], None, None, grouping_size[1], None, None, grouping_size[2], None, None, equip_results]

def save_data_points_to_csv(data):
    print(data)
    with open('./data/train_equip_decision_tree.csv', 'a') as f:
        np.savetxt(f, [data], fmt='%s', delimiter=',')
    print("Data points saved to 'data_points.csv'.")

def to_string(arr):
    if arr is None:
        return None
    else:
        result = "\"" + str(arr[0]) + "," + str(arr[1]) + "\""
        return result

# Function to handle mouse click events
def on_click(event):
    global arrow_recorded
    global data
    if arrow_recorded < num_of_grouping:
        data[2] = event.xdata
        data[3] = event.ydata
        ax.scatter(event.xdata, event.ydata, c='grey', s=50)
        arrow_recorded += 1
        print(f"Data point {arrow_recorded} added: ({event.xdata:.2f}, {event.ydata:.2f})")
        fig.canvas.draw()  # Update the plot immediately
        if arrow_recorded == num_of_grouping:
            print("data recorded")
            # Save the data points to a CSV file
            save_data_points_to_csv(data)
            # Reset the data points list
            arrow_recorded = 0
            init_data()

# Function to create and show the plot
def create_plot():
    plt.close('all')
    global fig, ax
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(target_face, extent=[0, 48, 0, 48])
    ax.set_xlim(0, 48)
    ax.set_ylim(0, 48)

def plot_prev():
    global fig, ax
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(target_face, extent=[0, 48, 0, 48])
    ax.set_xlim(0, 48)
    ax.set_ylim(0, 48)

    # plot recorded data
    prev_data = []
    with open('./data/train_equip_decision_tree.csv', 'r') as f:
        next(f)
        for line in f:
            temp = line.strip().split(',')
            x = float(temp[2])
            y = float(temp[3])
            prev_data.append((x, y))

    print(prev_data)

    if len(prev_data) > 0:
        for x, y in prev_data:
            ax.scatter(x, y, c='black', s=50)

init_data()
plot_prev()
fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()


