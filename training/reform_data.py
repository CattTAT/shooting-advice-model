import pandas as pd

# Load the CSV file
input_file = 'c:/Users/chinc/FYP/shooting-advice-model/data/validate_equip_decision_tree.csv'
output_file = 'c:/Users/chinc/FYP/shooting-advice-model/data/validate_equip_decision_tree_modified.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Drop the specified columns
columns_to_remove = ['Grouping1 size', 'Grouping2 size', 'Grouping3 size']
df = df.drop(columns=columns_to_remove)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Modified CSV saved to: {output_file}")