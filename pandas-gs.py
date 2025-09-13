import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic operations with pandas
print("\nDescriptive Statistics:")
print(df.describe())

print("\nFilter Rows where Age > 30:")
print(df[df['Age'] > 30])

print("\nSorting DataFrame by Name:")
print(df.sort_values(by='Name'))