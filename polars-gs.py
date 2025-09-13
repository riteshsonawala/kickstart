import polars as pl

# Create a DataFrame
df = pl.DataFrame({
    "name": ["Alice", "Bob", "Cathy"],
    "age": [25, 30, 22],
    "score": [85.5, 92.3, 88.0]
})

# Select specific columns
selected_df = df.select(["name", "score"])

# Filter rows based on condition
filtered_df = df.filter(pl.col("age") > 23)

# Add a new column
df = df.with_columns((pl.col("score") * 1.1).alias("adjusted_score"))

# Group by and aggregate
aggregated_df = df.group_by("age").agg(pl.col("score").mean().alias("average_score"))

# Show results
print(selected_df)
print(filtered_df)
print(df)
print(aggregated_df)