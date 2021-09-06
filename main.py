# import libraries
import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('stocks.csv')
# Set the tickers as the index
df = df.set_index('Tickers')
# Print data
print(df)

# Calculate & show the mean P/E Ratio
PE_Ratio_Mean = df.PE_Ratio.mean()

# Calculate and show fair market value

df['Fair_Market_Value'] = PE_Ratio_Mean * df['Earnings_Per_Share']

# Calculate company value ratio to determine if company is over valued or under valued
df['Over_Under_Ratio'] = df['Current_Price'] / df['Fair_Market_Value']

# Create a new column to store and show a label of under valued and over valued stocks.
df['Value_Label'] = np.where(df['Over_Under_Ratio'] < 1.0, 'Under Valued', 'Fair or Over Valued')

# Show the percentage that the stock is over or unde valued
df['Value_Percentage'] = abs(df['Over_Under_Ratio'] - 1) * 100
print(df)