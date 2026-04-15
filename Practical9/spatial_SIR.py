import numpy as np
import matplotlib.pyplot as plt

# =================================================================
# PSEUDOCODE 
# 1. initialize a 100x100 two-dimensional array, all elements set to 0 (susceptible S).
# 2. randomly select a coordinate (x, y) as the initial outbreak point, and set it to 1 (infected I).
# 3. set the infection rate (beta) and recovery rate (gamma).
# 4. enter the time loop (100 steps):
#    a. check if the current time step is a pre-set plotting time point; if so, draw a heatmap.
#    b. find all coordinates in the map with value 1 (infected).
#    c. create a copy of the current map to update states simultaneously.
#    d. for each infected coordinate:
#       i. with gamma probability, change its state to 2 (recovered R); otherwise, it remains 1 (infected I).
#       ii. if it remains infected, check its 8 neighbors (including diagonals):
#       iii. if a neighbor is 0 (susceptible S), it has a beta probability of becoming infected (change to 1).
#    e. use the updated map for the next iteration.
# =================================================================

# --- 1. initialize the population ---
size = 100
# create a 100x100 array to represent the population, where 0 = susceptible (S), 1 = infected (I), 2 = recovered (R)
population = np.zeros((size, size)) 

# randomly select an initial outbreak point and set it to infected (1)
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# parameters
beta = 0.3    # infection rate
gamma = 0.05  # recovery rate
time_steps = 100

# record the history of infected individuals for plotting
plot_times = [0, 10, 50, 100]

# --- 2. time loop ---
for t in range(time_steps + 1):
    
    # output (Series of plots)
    if t in plot_times:
        plt.figure(figsize=(6, 4))
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Spatial SIR - Time Step: {t}")
        plt.colorbar(ticks=[0, 1, 2], label='0:S, 1:I, 2:R')
        plt.show() 

    # find all infected coordinates (np.where)
    infectedIndex = np.where(population == 1)
    
    # create a copy of the current map to update states simultaneously
    new_population = population.copy()

    # iterate through all infected coordinates
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        
        # --- (Recovery) ---
        if np.random.random() < gamma:
            new_population[x, y] = 2
        else:
            # --- (Infection of 8 neighbours) ---
            # infect neighbors with beta probability
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    
                    nx, ny = x + dx, y + dy
                    
                    # check if the neighbor is within bounds
                    if 0 <= nx < size and 0 <= ny < size:
                        # only attempt to infect if the neighbor is currently susceptible (0)
                        if population[nx, ny] == 0:
                            if np.random.random() < beta:
                                new_population[nx, ny] = 1

    population = new_population