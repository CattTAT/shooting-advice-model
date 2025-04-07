import pandas as pd
import output.decision_tree_output as decision_tree_output
import pickle



def run(data):

    archer_eye = data[1]
    equip_data = []
    for i in range(2, len(data)):
        equip_data.append(data[i])

    new_equip_data = {
        'GroupingNum': [equip_data[0]],  # GroupingNum
        'Grouping1 to center_x': [equip_data[1]],
        'Grouping1 to center_y': [equip_data[2]],
        'Grouping2 to center_x': [equip_data[3]],
        'Grouping2 to center_y': [equip_data[4]],
        'Grouping3 to center_x': [equip_data[5]],  # Grouping3 to center_x
        'Grouping3 to center_y': [equip_data[6]]  # Grouping3 to center_y
    }
    print("To feed decision tree:", new_equip_data)

    # Load the saved model
    with open('equip_decision_tree_model.pkl', 'rb') as file:
        clf = pickle.load(file)
    with open('equip_multi_label_binarizer.pkl', 'rb') as file:
        mlb = pickle.load(file)

    new_data_df = pd.DataFrame(new_equip_data)
    equip_prediction = clf.predict(new_data_df)
    equip_prediction_labels = mlb.inverse_transform(equip_prediction)

    equip_prediction_array = [item for pred in equip_prediction_labels for item in pred]
    form_predictions = []


    if equip_data[0] != 1:
        form_predictions = [7]
    elif equip_data[0] == 1:
        if equip_prediction_array.count(0) > 0 or equip_prediction_array.count(1) > 0 or equip_prediction_array.count(2) > 0:
            if archer_eye == 'right':
                form_predictions.extend([1, 3, 4])  # Use extend to add multiple elements
            elif archer_eye == 'left':
                form_predictions.extend([0, 2])  # Use extend to add multiple elements

        if equip_prediction_array.count(3) > 0 or equip_prediction_array.count(4) > 0 or equip_prediction_array.count(5) > 0:
            if archer_eye == 'right':
                form_predictions.extend([0, 2])  # Use extend to add multiple elements
            elif archer_eye == 'left':
                form_predictions.extend([1, 3, 4])  # Use extend to add multiple elements

        if equip_prediction_array.count(6) > 0 or equip_prediction_array.count(7) > 0 or equip_prediction_array.count(8) > 0 or equip_prediction_array.count(9) > 0 or equip_prediction_array.count(10) > 0 or equip_prediction_array.count(11) > 0:
            form_predictions.extend([5, 6])  # Use extend to add multiple elements
            

    print("Equipment Decision tree results:", equip_prediction_array)
    print("Form Decision tree results:", form_predictions)

    output = decision_tree_output.decision_tree_output(equip_prediction_array, form_predictions)

    # Print the predictions
    return output
