import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =================================================================
# 1. Importing the dataset
# ================================================================= 

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# =================================================================
# 2. Afghanistan Analysis (iloc)
# =================================================================
afghan_subset = dalys_data.iloc[0:10, 2:4]
print("--- Afghanistan first 10 rows (Year & DALYs) ---")
print(afghan_subset)

# COMMENT: Across the first 10 years recorded in Afghanistan (1990-1999), 
# the year that reported the maximum DALYs is 1992.

# =================================================================
# 3. Zimbabwe Analysis (Boolean filtering)
# =================================================================
is_zimbabwe = dalys_data.Entity == "Zimbabwe"
zimbabwe_data = dalys_data.loc[is_zimbabwe, ["Year", "DALYs"]]

print("\n--- Zimbabwe years recorded ---")
print(zimbabwe_data["Year"].values)

# COMMENT: The DALYs for Zimbabwe were recorded from the first year 1990 
# to the last year 2019.

# =================================================================
# 4. 2019 Extremes Analysis
# =================================================================
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]

sorted_2019 = recent_data.sort_values(by="DALYs")
min_2019_country = sorted_2019.iloc[0]["Entity"]
max_2019_country = sorted_2019.iloc[-1]["Entity"]

print(f"\n2019 Minimum DALYs: {min_2019_country}")
print(f"2019 Maximum DALYs: {max_2019_country}")

# COMMENT: In 2019, the country with the minimum DALYs is San Marino, 
# and the country with the maximum DALYs is Central African Republic.

# =================================================================
# 5. Plotting DALYs over time (for the 2019 minimum country)
# =================================================================
plot_data = dalys_data.loc[dalys_data.Entity == min_2019_country, ["Year", "DALYs"]]

plt.figure(figsize=(10, 6))
plt.plot(plot_data.Year, plot_data.DALYs, 'bo-', label=min_2019_country)

plt.title(f"DALYs Rate Trend Over Time: {min_2019_country}")
plt.xlabel("Year")
plt.ylabel("DALYs Rate (per 100,000)")
plt.xticks(plot_data.Year, rotation=-90)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

# =================================================================
# 6. Task 6: Self-Question Analysis (China vs UK)
# =================================================================
# Question: Compare the DALYs rate between China and the UK (1990-2019).
# Are they becoming more similar, and what are the trends?

china_data = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]
uk_data = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]

plt.figure(figsize=(12, 6))
plt.plot(china_data.Year, china_data.DALYs, 'r-o', label='China')
plt.plot(uk_data.Year, uk_data.DALYs, 'b-s', label='United Kingdom')

plt.title("Comparison of DALYs Rate: China vs United Kingdom (1990-2019)")
plt.xlabel("Year")
plt.ylabel("DALYs Rate (per 100,000)")
plt.xticks(china_data.Year, rotation=-90)
plt.legend() 
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()