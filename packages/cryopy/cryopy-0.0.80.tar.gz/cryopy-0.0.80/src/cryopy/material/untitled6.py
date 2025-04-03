#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 11:02:39 2025

@author: valentinsauvage
"""


import numpy as np
import matplotlib.pyplot as plt


RRR_50 = np.array([1.8743, -0.41538, -0.6018, 0.13294, 0.26426, -0.0219, -0.051276, 0.0014871, 0.003723])
RRR_100 = np.array([2.2154, -0.47461, -0.88068, 0.13871, 0.29505, -0.02043, -0.04831, 0.001281, 0.003207])
RRR_150 = np.array([2.3797, -0.4918, -0.98615, 0.13942, 0.30475, -0.019713, -0.046897, 0.0011969, 0.0029988])
RRR_200 = np.array([1.357, 0.3981, 2.669, -0.1346, -0.6683, 0.01342, 0.05773, 0.0002147, 0])
RRR_300 = np.array([2.8075, -0.54074, -1.2777, 0.15362, 0.36444, -0.02105, -0.051727, 0.001222, 0.0030964])



def function_from_coef_to_conductivity(temperature, coefficients):
    """
    Calculate conductivity from given temperature and coefficients.
    
    Parameters:
        temperature (float): The temperature in Kelvin.
        coefficients (list of floats): The coefficients for the numerator and denominator of the formula.
        
    Returns:
        float: The calculated conductivity value.
    """

    # Define powers of temperature for readability and efficiency
    temperature_powers = [temperature**(0.5), temperature**(1), temperature**(1.5), temperature**(2)]

    # Numerator: Linear combination of temperature powers with the corresponding coefficients
    numerator = coefficients[0] + coefficients[2] * temperature_powers[0] + coefficients[4] * temperature_powers[1] + \
                coefficients[6] * temperature_powers[2] + coefficients[8] * temperature_powers[3]
    
    # Denominator: Linear combination of temperature powers with corresponding coefficients
    denominator = 1 + coefficients[1] * temperature_powers[0] + coefficients[3] * temperature_powers[1] + \
                  coefficients[5] * temperature_powers[2] + coefficients[7] * temperature_powers[3]
    
    # Calculate the value of conductivity (base 10)
    value = numerator / denominator
    value = 10 ** value
    
    return value


Temperature_array = np.logspace(np.log10(4),np.log10(300),100)

Conductivity_50 = [function_from_coef_to_conductivity(temperature,RRR_50) for temperature in Temperature_array]
Conductivity_100 = [function_from_coef_to_conductivity(temperature,RRR_100) for temperature in Temperature_array]
Conductivity_150 = [function_from_coef_to_conductivity(temperature,RRR_150) for temperature in Temperature_array]
Conductivity_200 = [function_from_coef_to_conductivity(temperature,RRR_200) for temperature in Temperature_array]
Conductivity_300 = [function_from_coef_to_conductivity(temperature,RRR_300) for temperature in Temperature_array]


plt.figure()
plt.plot(Temperature_array,Conductivity_50, label = 'RRR 50')
plt.plot(Temperature_array,Conductivity_100, label = 'RRR 100')
plt.plot(Temperature_array,Conductivity_150, label = 'RRR 150')
plt.plot(Temperature_array,Conductivity_200, label = 'RRR 200')
plt.plot(Temperature_array,Conductivity_300, label = 'RRR 300')
plt.grid()
plt.xscale('log')
plt.legend()
plt.yscale('log')
plt.xlabel('Temperature [K]')
plt.ylabel(r' Thermal conductivity [W.m$^{-1}$.K$^{-1}$]')
plt.title('Thermal conductivity of copper against the temperature')



#%%

import numpy as np
from scipy.interpolate import RegularGridInterpolator

# Example Data (Replace with your actual data)
temperature  = Temperature_array  # 50 points from 4K to 300K
resistance = np.array([50,100,150,200,300])  # 50 points from 50Ω to 300Ω

# Example conductivity values: sigma(T, R) (Replace with your real data)
conductivity = np.array([Conductivity_50,Conductivity_100,Conductivity_150,Conductivity_200,Conductivity_300])
conductivity = np.transpose(conductivity)

# Create the interpolator
interp_func = RegularGridInterpolator((temperature, resistance), conductivity)

def interpolate_conductivity(T, R):
    """Interpolates conductivity for a given Temperature (T) and Resistance (R)."""
    return interp_func([[T, R]])[0]



#%%

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection

# Define temperature array (example range)

# Define RRR values
rrr_values = [50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]

# Create figure and axis
fig, ax = plt.subplots()

# Create a colormap from blue (low RRR) to red (high RRR)
norm = mcolors.Normalize(vmin=min(rrr_values), vmax=max(rrr_values))
colormap = cm.coolwarm  # Choose a colormap

# Prepare data for LineCollection
lines = []
colors = []

for rrr in rrr_values:
    conductivity = [interpolate_conductivity(t, rrr) for t in temperature]
    points = np.array([Temperature_array, conductivity]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lines.append(segments)
    # Assign a single color to the entire curve based on RRR
    curve_color = colormap(norm(rrr))  # Single color for this RRR
    colors.extend([curve_color] * len(segments))  # Repeat for all segments

# Convert lines and colors to a LineCollection
lc = LineCollection(np.vstack(lines), colors=colors, linewidth=2)
ax.add_collection(lc)

# Set log scale
ax.set_xscale("log")
ax.set_yscale("log")

# Set labels and title
ax.set_xlabel("Temperature [K]")
ax.set_ylabel(r"Thermal conductivity [W.m$^{-1}$.K$^{-1}$]")
ax.set_title("Thermal conductivity of copper against the temperature")

# Add colorbar
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=colormap), ax=ax)
cbar.set_label("RRR (Residual Resistivity Ratio)")

# Adjust limits
ax.set_xlim(min(Temperature_array), max(Temperature_array))

plt.grid()
plt.show()

#%% Fonction that take in input all the data on copper ? 


temperature_1 = [2,4,6,8,10]
resistance_1 = [1,2,3,4,5]
conductivity_1 = [[10,11,12,13,14],
                  [20,21,22,23,24],
                  [30,31,32,33,34],
                  [40,41,42,43,44],
                  [50,51,52,53,54]]



temperature_2 = [20,30,40]
resistance_1 = [8,10,12]
conductivity_1 = [[100,110,120],
                  [200,210,220],
                  [300,310,320]]






