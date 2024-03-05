# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:14:29 2024

@author: SPECTRE
"""

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint


mass = 10 #kg
r_k = 4000 #N/m
alp = 20 #Ns/m
x_o = 0.01 # m
v_o = 0 # m/s
f_o = 100 #N
w =  10 #rad/s
#équation différentielle du syteme
def systeme(y,t):
    x, v = y
    dx_dt = v
    dv_dt = -(alp / mass)* v - (r_k / mass) * x
    return [dx_dt, dv_dt]
y_o = [x_o, v_o] #conditions initiales
temps = np.linspace(0, 10, 1000) # tabkeau de 1000 valeurs équidistantes de 0 à 10 secondes
solution = odeint(systeme, y_o, temps)
#extarction des positions et les vitesses
x, v = solution.T
#plotter les oscillations avec force externe
plt.plot(temps, x)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Oscillations libres du systeme Mécanique')
plt.show()

def systeme_forcee(y,t): #définition de l'équation dif du systeme avec Force ext.
    x, v = y
    dx_dt = v
    dv_dt = -(alp / mass)* v - (r_k / mass) * x + (f_o / mass) * np.cos(w * t)
    return [dx_dt, dv_dt]

y_o = [x_o, v_o] #conditions
temps = np.linspace(0, 10, 1000) ##temps d'intégration 
solution_forced = odeint(systeme_forcee, y_o, temps)
x_forced, v_forced = solution_forced.T #position
#plotter les oscillations
plt.plot(temps, x_forced)
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Oscillations du systeme Mécanique forcé')
plt.show()

kinetic = (1/2)*mass*v_forced**2 #calcul ENERGIE CINeTIQUE
potential = (1/2)*r_k*x_forced**2 #energie potentielle
mechanic = kinetic + potential #calcul de l'énergie mécanique totale
plt.plot(temps, kinetic, label='Energie Cinétique')
plt.plot(temps, potential, label='Energie Potentielle')
plt.plot(temps, mechanic, label='Energie Mécanique')
plt.xlabel('Temps (s)')
plt.ylabel('Energie (J)')
plt.title('Energies du systeme Mécanique forcé')
plt.legend()
plt.show()