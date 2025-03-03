import pandas as pd
import output.decision_tree_output as decision_tree_output


def run(data):
    # # Load the saved model
    # model = joblib.load('decision_tree_model.pkl')

    # # Make predictions
    # predictions = model.predict(data)
    equip_predictions = [3,9]
    form_predictions = [1,2]

    output = decision_tree_output.decision_tree_output(equip_predictions, form_predictions)

    # Print the predictions
    return output
