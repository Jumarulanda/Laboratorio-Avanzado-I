import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv("circuito1.csv")
simul = pd.read_csv("circuito1_sim.csv")

data['I'] = data['I'].apply(lambda x: x/100)
R = 2130 #Ohm

slope, intercept, r_value, p_value, std_err = linregress(data['V'],data['I'])

x = np.linspace(0,20,100)

plt.plot(x, slope*x + intercept, 'r')

plt.errorbar(data['V'],data['I'], xerr = 0.01, yerr = 0.0001)
plt.plot(simul['V(R1.nA)'],simul['I(R1.nA)'], 'b')

plt.show()
