import numpy as np
import matplotlib.pyplot as plt

def fit_n_plot(x, y, ux, uy, intercept, xlabel, ylabel,figsize=(5,4)):

    if not intercept:

        m = np.sum(x*y)/np.sum(x*x)
        um = uy/np.sqrt(np.sum(x*x))

        # ---------------------------------------
        
        x_range = np.linspace(0, np.max(x), 1000)
        y_range = x_range*m
        
        fig, ax = plt.subplots(figsize=figsize)

        ax.errorbar(x, y, xerr=ux, yerr=uy, fmt=".", ecolor="red")

        ax.plot(x_range, y_range, "k-")

        ax.set_xlabel(xlabel, fontsize=11)
        ax.set_ylabel(ylabel, fontsize=11)

        # print(np.max(x),np.min(x_range), np.max(x_range), np.max(x_range)*m, m)
        
        ax.set_xlim(0, np.max(x))
        ax.set_ylim(0, np.max(y_range))
        
        ax.text(np.max(x_range)/20, 8*np.max(y_range)/9, r"$ {} = ({:.1f} \pm {:.1f}) {}  $".format(xlabel[0], m, um, ylabel[0]), fontsize=11)

        return ax, fig
