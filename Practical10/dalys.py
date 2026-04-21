# =================================================================
###Task4 Working with dataframes###
# =================================================================
import pandas as pd
import os

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


# 1. check the data structure and statistics
print("--- Data preview (first 5 rows) ---")
print(dalys_data.head(5)) # 

print("\n--- Data structure information (info) ---")
dalys_data.info()

print("\n--- Numerical columns statistics (describe) ---")
stats = dalys_data.describe()
print(stats)

# max_dalys = stats.loc['max', 'DALYs']
# min_dalys = stats.loc['min', 'DALYs']
# start_year = stats.loc['min', 'Year']
# end_year = stats.loc['max', 'Year']


# 2. use iloc to access specific rows and columns
print("\n--- iloc practice ---")

# the first row, the fourth column (index 3)
print("First row, fourth column:", dalys_data.iloc[0, 3])

# Challenge task 1: Display columns 3 and 4 (indices 2, 3), first 10 rows
# Index 0:10 means rows from 0 to 9; 2:4 means columns from 3 to 4 (excluding index 4)
print("\nFirst 10 rows of Year and DALYs columns:")
print(dalys_data.iloc[0:10, 2:4])

# dalys_data.iloc[2, 0:5]      
# dalys_data.iloc[0:2, :]      
# dalys_data.iloc[0:10:2, 0:5] 

# 3. use buolean values to filter columns
my_columns = [True, True, False, True]
print("\nuse boolean list to filter columns (Year and DALYs):")
print(dalys_data.iloc[0:3, my_columns])

# 4. use loc to filter rows based on conditions
print("\n--- loc practice and zimbabwe ---")

# Step1 : Create a boolean series to identify rows where Entity is "Zimbabwe"
is_zimbabwe = dalys_data.Entity == "Zimbabwe"

# Step2 : Use this boolean series to filter the DataFrame and get the years for Zimbabwe
zimbabwe_years = dalys_data.loc[is_zimbabwe, "Year"]

print("Zimbabwe years:")
print(zimbabwe_years.values) # 

zimbabwe_full = dalys_data.loc[dalys_data.Entity == "Zimbabwe", ["Year", "DALYs"]]
print("\nZimbabwe detailed data:")
print(zimbabwe_full.head())


# =================================================================
###Task5 Examine the situation across countries###
# =================================================================
import matplotlib.pyplot as plt

# 1. Extract data for the year 2019 and sort by DALYs
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]

# sort the data by DALYs in ascending order
sorted_2019 = recent_data.sort_values(by="DALYs")

print("--- the country with the lowest DALYs in 2019 ---")
print(sorted_2019.head(1)) 

print("\n--- the country with the highest DALYs in 2019 ---")
print(sorted_2019.tail(1)) # 

# 2. Extract historical data for the United Kingdom
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]

# 3. Plot the DALYs trend for the United Kingdom
plt.figure(figsize=(10, 6)) 

plt.plot(uk.Year, uk.DALYs, 'b+') 

plt.title("DALYs Rate Over Time in the United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")

plt.xticks(uk.Year, rotation=-90)

plt.tight_layout() 
plt.show()



# =================================================================
# Task6 Self Question
# question: Compare the DALYs rate between China and the United Kingdom from 1990 to 2019. Which country has a higher DALYs rate, and how do their trends differ over time?
# =================================================================

# 1. Extract data for China (1990-2019)
china_data = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]

# 2. Extract data for the United Kingdom (1990-2019)
uk_data = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]

# 3. Plot the DALYs trends for both countries on the same graph for comparison
plt.figure(figsize=(12, 6))

# draw China's line (red, circle markers)
plt.plot(china_data.Year, china_data.DALYs, 'r-o', label='China')

#draw UK's line (blue, square markers)
plt.plot(uk_data.Year, uk_data.DALYs, 'b-s', label='United Kingdom')

# 4. Add title, labels, legend, and grid for better visualization
plt.title("Comparison of DALYs Rate: China vs United Kingdom (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs Rate (per 100,000)")
plt.xticks(china_data.Year, rotation=-90)
plt.legend() 
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()