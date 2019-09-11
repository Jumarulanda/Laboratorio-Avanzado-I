import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pandas.plotting import table # EDIT: see deprecation warnings below

ax = plt.subplot(111, frame_on=False) # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

data = pd.read_csv("circuito2.csv")
simul = pd.read_csv("circuito2_sim.csv")

data['I'] = data['I'].apply(lambda x: x/1000)
R = 2130 #Ohm

slope, intercept, r_value, p_value, std_err = linregress(data['V'],data['I'])

x = np.linspace(0,20,100)

print(1/slope)
#plt.plot(x, slope*x + intercept, 'r')

#plt.errorbar(data['V'],data['I'], xerr = 0.01, yerr = 0.0001)
#plt.plot(simul['V(R1.nA)'],simul['I(R1.nA)'], 'b')

#table(ax, data)  # where df is your data frame

#plt.savefig('mytable.png')


plt.show()
