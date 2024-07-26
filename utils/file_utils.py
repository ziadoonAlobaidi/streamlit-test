
import pandas as pd

# Load the Excel file
filepath = '/.xlsx'
df = pd.read_excel(filepath)

# Display the first few rows of the DataFrame
print(df.head())
