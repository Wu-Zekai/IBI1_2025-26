import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  

#  define the parameters 
N = 10000          # total population (keep as 10000)
beta = 0.3         # infection rate
gamma = 0.05       # recovery rate
time_steps = 1000  # simulation duration
# cover all the posible rates of vaccination from 0% to 100%
vax_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(8, 5), dpi=150)

#  Loop through each vaccination rate and simulate the SIR model 
for i, v_rate in enumerate(vax_rates):
    #  Initialize the population counts (total always remains N) 
    V_count = int(N * v_rate)       # vaccinated individuals
    I_count = 1                     # initial infected individuals
    R_count = 0                     # initial recovered individuals
    S_count = N - V_count - I_count # susceptible individuals
    
    # track the history of infected individuals for plotting
    I_history = [I_count]

    #  time loop 
    for t in range(time_steps):
        #  Calculate Infection Process 
        # The probability that each susceptible individual gets infected = beta * (current infected / total population
        p_inf = beta * (I_count / N)
        p_rec = gamma
        
        # random process: new infections
        if S_count > 0:
            num_new_inf = np.sum(np.random.choice([0, 1], size=S_count, p=[1 - p_inf, p_inf]))
        else:
            num_new_inf = 0
            
        # random process: new recoveries
        if I_count > 0:
            num_new_rec = np.sum(np.random.choice([0, 1], size=I_count, p=[1 - p_rec, p_rec]))
        else:
            num_new_rec = 0

        # update the counts
        S_count -= num_new_inf
        I_count += (num_new_inf - num_new_rec)
        R_count += num_new_rec
        
        I_history.append(I_count)

    #  Plotting and Labeling 
    plt.plot(I_history, label=f'{v_rate*100:.0f}% Vaccinated', color=cm.viridis(i/len(vax_rates)))

# set the labels and title
plt.xlabel('Time Step')
plt.ylabel('Number of Infected People')
plt.title('Infection Curves at Different Vaccination Rates')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.tight_layout()

plt.savefig("SIR_vaccination_comparison.png")
plt.show()