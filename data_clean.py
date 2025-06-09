import pandas as pd

# Load raw cutoff data
df = pd.read_csv("predicted_cutoffs_lstm.csv")

# Replace placeholder cutoff indicators with NaN
df.replace(["***", "*", ""], pd.NA, inplace=True)

# Drop rows where OC or BC is missing (we assume OC must be present)
df.dropna(subset=["OC"], inplace=True)

# Convert OC to numeric for sorting
df["OC"] = pd.to_numeric(df["OC"], errors="coerce")
df.dropna(subset=["OC"], inplace=True)

# Sort by OC cutoff descending (most competitive first)
df_sorted = df.sort_values(by="OC", ascending=False)

# Save cleaned + sorted data
df_sorted.to_csv("predicted_cutoffs_cleaned_sorted.csv", index=False)
print("✅ Cleaned and sorted CSV saved as 'tnea_cutoff_data_2022_cleaned_sorted.csv'")
