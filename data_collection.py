import numpy as np
import matplotlib.pyplot as plt

# Load the target face image
target_face = plt.imread('a1457853dcf807706ca2f1300d7f4fb2.png')

# Initialize the data points list
arrow_recorded = 0
data = []
ready_to_save = False


def save_data_points_to_csv(data):
    print(data)
    with open('./data/data_collection.csv', 'a') as f:
        np.savetxt(f, [data], fmt='%s', delimiter=',')
    print("Data points saved to 'data_points.csv'.")

# Function to handle mouse click events
def on_click(event):
    global arrow_recorded
    global data
    global ready_to_save
    if ready_to_save == False: return
    if arrow_recorded < 6:
        data.append(event.xdata)
        data.append(event.ydata)
        ax.scatter(event.xdata, event.ydata, c='grey', s=50)
        arrow_recorded += 1
        print(f"Data point {arrow_recorded} added: ({event.xdata:.2f}, {event.ydata:.2f})")
        fig.canvas.draw()  # Update the plot immediately
        if arrow_recorded == 6:
            print("Set of 6 data points complete.")
            # Save the data points to a CSV file
            save_data_points_to_csv(data)
            # Reset the data points list
            arrow_recorded = 0
            data = []
            ready_to_save = False
            # Ask for archer info
            save_archer_info_to_csv()
            # Reopen the plot
            create_plot()

# Function to create and show the plot
def create_plot():
    plt.close('all')
    global fig, ax
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(target_face, extent=[0, 48, 0, 48])
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

# Function to ask for archer info
def save_archer_info_to_csv():
    global ready_to_save
    while True:
        archer_level = input("Enter archer level (0 novice,1 elementary,2 intermediate,3 advance, exit to stop the prog): ")
        if archer_level == '0':
            archer_level = 'novice'
            break
        elif archer_level == '1':
            archer_level = 'elementary'
            break
        elif archer_level == '2':
            archer_level = 'intermediate'
            break
        elif archer_level == '3':
            archer_level = 'advance'
            break
        elif archer_level == 'exit':
            exit()
        else:
            print("Invalid archer level.")
    
    while True:
        archer_eye = input("Enter archer eye (0 left,1 right, exit to stop the prog): ")
        if archer_eye == '0':
            archer_eye = 'left'
            break
        elif archer_eye == '1':
            archer_eye = 'right'
            break
        elif archer_eye == 'exit':
            exit()
        else:
            print("Invalid archer eye.")
    
    data.append(archer_level)
    data.append(archer_eye)
    ready_to_save = True

# Show the plot and wait for user input
save_archer_info_to_csv()
create_plot()

