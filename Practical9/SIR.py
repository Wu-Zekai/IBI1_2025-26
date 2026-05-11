import numpy as np
import matplotlib.pyplot as plt

# define the initial parameters
N = 10000          # total population
I_count = 1        # initial infected individuals
R_count = 0        # initial recovered individuals
S_count = N - I_count  # initial susceptible individuals

beta = 0.3         # infection rate
gamma = 0.05       # recovery rate

# create arrays to track the changes 
S_history = [S_count]
I_history = [I_count]
R_history = [R_count]

time_steps = 1000

for t in range(time_steps):
    # Calculate Infection Process 
    # The probability that each susceptible individual gets infected = beta * (current infected / total population)
    p_inf = beta * (I_count / N)
    

    if S_count > 0:
        new_infections = np.random.choice([0, 1], size=S_count, p=[1 - p_inf, p_inf])
        num_new_inf = np.sum(new_infections)
    else:
        num_new_inf = 0
        
    # Calculate Recovery Process 
    p_rec = gamma
    
    # Only calculate recoveries if there are currently infected individuals
    if I_count > 0: 
        new_recoveries = np.random.choice([0, 1], size=I_count, p=[1 - p_rec, p_rec])
        num_new_rec = np.sum(new_recoveries)
    else:
        num_new_rec = 0

    S_count -= num_new_inf
    I_count += (num_new_inf - num_new_rec)
    R_count += num_new_rec

    S_history.append(S_count)
    I_history.append(I_count)
    R_history.append(R_count)


plt.figure(figsize=(6, 4), dpi=150) 

plt.plot(S_history, label='Susceptible', color='blue')
plt.plot(I_history, label='Infected', color='red')
plt.plot(R_history, label='Recovered', color='green')

plt.xlabel('Time Step')
plt.ylabel('Number of People')
plt.title('Simple SIR Model Simulation')
plt.legend()

plt.savefig("SIR_plot.png")

plt.show()