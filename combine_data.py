import pandas as pd

# Load each year's file and tag the year
df_2022 = pd.read_csv("tnea_cutoff_data_2022_cleaned_sorted.csv")
df_2022["Year"] = 2022

df_2023 = pd.read_csv("tnea_cutoff_data_2023_cleaned_sorted.csv")
df_2023["Year"] = 2023

df_2024 = pd.read_csv("tnea_cutoff_data_2024_cleaned_sorted.csv")
df_2024["Year"] = 2024

# Combine all into one dataframe
df = pd.concat([df_2022, df_2023, df_2024], ignore_index=True)

# Save for future reference
df.to_csv("tnea_cutoff_combined.csv", index=False)
print("✅ Combined dataset saved as 'tnea_cutoff_combined.csv'")

# Preview
df.head()
