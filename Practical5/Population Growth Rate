import matplotlib.pyplot as plt
import numpy as np
countries = np.array(['UK', 'China', 'Italy', 'Brazil', 'USA'])
population_2020=np.array([66.7,1426.0,59.4,208.6,331.6])
population_2024=np.array([69.2, 1410, 58.9, 212.0, 340.1])
population_2020 = np.array(population_2020)
population_2024 = np.array(population_2024)
changes=(population_2024-population_2020)/population_2020*100
print('Population growth rate from 2020 to 2024:' + str(changes)) 
sorted_indices = np.argsort(changes)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_changes = [changes[i] for i in sorted_indices]
print('Countries sorted by population growth rate:' + str(sorted_countries))
Maxium_increase_country = sorted_countries[-1]
Maxium_decrease_country = sorted_countries[0]
Maxium_increase_change = sorted_changes[-1]
Maxium_decrease_change = sorted_changes[0]
print('Maximum increase country:' + Maxium_increase_country + ', Change:' + str(Maxium_increase_change))
print('Maximum decrease country:' + Maxium_decrease_country + ', Change:' + str(Maxium_decrease_change))
plt.bar(countries, changes)
plt.xlabel('Countries')
plt.ylabel('Population Growth Rate (%)')
plt.title('Population Growth Rate from 2020 to 2024')
plt.show()


