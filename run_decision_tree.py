import pandas as pd
import output.decision_tree_output as decision_tree_output
import pickle



def run(data):

    archer_level = data[0]
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

    print("Equipment Decision tree results:", equip_prediction_array)
    form_predictions = [1,2]

    output = decision_tree_output.decision_tree_output(equip_prediction_array, form_predictions)

    # Print the predictions
    return output
