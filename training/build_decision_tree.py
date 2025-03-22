from matplotlib import pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.preprocessing import MultiLabelBinarizer

# Load the CSV file into a DataFrame
input_file = 'c:/Users/chinc/FYP/shooting-advice-model/data/train_equip_decision_tree.csv'
df = pd.read_csv(input_file)

# Split the data into features and target
X = df.iloc[:, :-1]  # All columns except the last one
y = df.iloc[:, -1]   # The last column

# Convert the target column to a list of sets
y = y.apply(lambda x: tuple(map(int, x.split(','))))

# Use MultiLabelBinarizer to transform the target variable
mlb = MultiLabelBinarizer()
y_transformed = mlb.fit_transform(y)

# Initialize and train the decision tree classifier
clf = DecisionTreeClassifier()
plt.figure()
clf.fit(X, y_transformed)

plot_tree(clf, filled=True)
plt.title("Decision tree ")
plt.show()

# Export the decision tree rules
tree_rules = export_text(clf, feature_names=X.columns.tolist())
print(tree_rules)

# Save the decision tree rules to a text file
with open('decision_tree_rules.txt', 'w') as f:
    f.write(tree_rules)

print("Decision tree rules saved to 'decision_tree_rules.txt'.")

def predict_new_data(new_data):
    new_data_df = pd.DataFrame([new_data], columns=X.columns)
    prediction = clf.predict(new_data_df)
    prediction_labels = mlb.inverse_transform(prediction)
    return prediction_labels

# Example new data for testing
new_data = {
    'GroupingNum': 1,
    'Grouping1 size': 6,
    'Grouping1 to center_x': 4.207792207792208,
    'Grouping1 to center_y': 44.103896103896105,
    'Grouping2 size': None,
    'Grouping2 to center_x': None,
    'Grouping2 to center_y': None,
    'Grouping3 size': None,
    'Grouping3 to center_x': None,
    'Grouping3 to center_y': None
}

# Replace None with appropriate values (e.g., 0) for prediction
for key in new_data:
    if new_data[key] is None:
        new_data[key] = 0

# Predict the output for the new data
predicted_output = predict_new_data(new_data)
print(f"Predicted output for the new data: {predicted_output}")