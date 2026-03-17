heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
print(len(heart_rates))
sum_rates =0
for rate in heart_rates:
    sum_rates += rate
    average_rate = sum_rates / len(heart_rates)
print(f"Average heart rate: {average_rate:.2f} bpm")    
low_rates = []
normal_rates = []
high_rates = []
for rate in heart_rates:
    if rate < 60:
        low_rates.append(rate)
    elif 60 <= rate <= 120:
        normal_rates.append(rate)
    else:
        high_rates.append(rate)
print("Low heart rates number:", len(low_rates))
print("Normal heart rates number:", len(normal_rates))
print("High heart rates number:", len(high_rates))
if len(low_rates) > len(normal_rates) and len(low_rates) > len(high_rates):
    print("Most heart rates are low.")
elif len(normal_rates) > len(low_rates) and len(normal_rates) > len(high_rates):
    print("Most heart rates are normal.")
else:    print("Most heart rates are high.")
import matplotlib.pyplot as plt
labels = ['Low', 'Normal', 'High']
sizes = [len(low_rates), len(normal_rates), len(high_rates)]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Distribution of Heart Rates')
plt.show()