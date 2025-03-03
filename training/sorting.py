import pandas as pd

# Load the CSV file into a DataFrame
input_file = 'c:/Users/chinc/FYP/shooting-advice-model/data/data_collection_0226.csv'
output_file = 'c:/Users/chinc/FYP/shooting-advice-model/data/sorted_data_collection_0226.csv'

df = pd.read_csv(input_file, header=None)

# Sort the DataFrame by the first and second columns
df_sorted = df.sort_values(by=[0, 1])

# Save the sorted DataFrame to a new CSV file
df_sorted.to_csv(output_file, index=False, header=False)

print(f"Sorted data saved to '{output_file}'.")