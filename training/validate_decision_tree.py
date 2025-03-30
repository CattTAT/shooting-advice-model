import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

# Load the trained model and MultiLabelBinarizer from the .pkl files
with open('decision_tree_model.pkl', 'rb') as file:
    clf = pickle.load(file)
with open('multi_label_binarizer.pkl', 'rb') as file:
    mlb = pickle.load(file)

# Function to preprocess and predict new data
def predict_new_data(new_data):
    new_data_df = pd.DataFrame(new_data)
    prediction = clf.predict(new_data_df)
    prediction_labels = mlb.inverse_transform(prediction)
    return prediction_labels

# Load the test data from a CSV file
test_file = './data/validate_equip_decision_tree_modified.csv'
test_df = pd.read_csv(test_file)

# Split the test data into features and target
X_test = test_df.iloc[:, :-1]  # All columns except the last one
y_test = test_df.iloc[:, -1]   # The last column

# Convert the target column to a list of sets
y_test = y_test.apply(lambda x: tuple(map(int, x.split(','))))

# Use the trained model to predict the outputs for the test data
y_pred_transformed = clf.predict(X_test)
y_pred = mlb.inverse_transform(y_pred_transformed)

# Calculate the accuracy rate
# Convert y_test and y_pred to sets for comparison
y_test_sets = [set(label) for label in y_test]
y_pred_sets = [set(label) for label in y_pred]

# Calculate accuracy as the percentage of exact matches
correct_predictions = sum(1 for true, pred in zip(y_test_sets, y_pred_sets) if true == pred)
accuracy_rate = correct_predictions / len(y_test_sets) * 100

# Write the results to a text file
output_file = './data/validation_results.txt'
with open(output_file, 'w') as f:
    f.write(f"Accuracy rate: {accuracy_rate:.2f}%\n\n")
    f.write("Predictions for each test sample:\n")
    for i, (true, pred) in enumerate(zip(y_test_sets, y_pred_sets)):
        f.write(f"Test sample {i + 1}: True={true}, Predicted={pred}\n")

print(f"Results saved to '{output_file}'.")