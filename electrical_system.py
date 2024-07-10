'''Electrical Systems'''

import numpy as np
from scipy.constants import epsilon_0, mu_0, c, h, hbar, k, G, e, pi

# Constantes físicas utilizadas en el código:
# - epsilon_0 (Permitividad del vacío): 8.854187817e-12 F/m
#   Representa la capacidad del vacío para permitir el campo eléctrico.
# - mu_0 (Permeabilidad del vacío): 4π × 10^-7 N/A^2
#   Es la medida de la resistencia del vacío contra la formación de un campo magnético.
# - c (Velocidad de la luz en el vacío): 2.99792458e8 m/s
#   La velocidad máxima a la que la información y la energía pueden viajar.
# - h (Constante de Planck): 6.62607015e-34 J·s
#   La constante que relaciona la energía de un fotón con su frecuencia.
# - hbar (Constante de Planck reducida): 1.054571817e-34 J·s
#   La constante de Planck dividida por 2π, utilizada en la mecánica cuántica.
# - k (Constante de Boltzmann): 1.380649e-23 J/K
#   Relaciona la energía cinética media de las partículas en un gas con la temperatura del gas.
# - G (Constante de gravitación universal): 6.67430e-11 m^3/kg/s^2
#   Describe la fuerza gravitacional entre dos masas.
# - e (Carga del electrón): 1.602176634e-19 C
#   La cantidad de carga eléctrica transportada por un electrón único.
# - pi (π): 3.141592653589793
#   La relación entre la circunferencia de un círculo y su diámetro.

_ke_ =  1 / (4 * pi * epsilon_0)

'''potenciales electricos'''

'''distribucion de carga discreta'''

def puntual_change(r, Q =1 , ro = 0):
    return _ke_ * Q/ (r - ro)

'''distribucion de carga continua'''

def ring_(r, Q =1, z = 1):
    return _ke_ * Q / np.sqrt(r**2 + z**2)

def sphere_(r, Q = 1 , ro = 1, volumetric = False):
    if volumetric == False :
        if r <= ro :
            R = r-ro
        if r > ro :
            R = ro
    elif volumetric == True:
        if r <= ro :
            R = 2*ro / (3 - (r/ro)**2)
        if r > ro :
            R = ro
    return _ke_ * Q / R

def plane_(z ,_sigma_, z0 = 0, infinite = True):
    if infinite == True:
        return  _sigma_ * abs(z-z0)/ (-2*epsilon_0)
    
def cilindro_(r, ro, _lambda_):
    if r <= ro:
        P = 0.5*(1-(r/ro)**2) -np.log(r/ro) 
    if r > ro : #out of the cilinder
        P =  -1*np.log(r/ro) 
    return 2 *_ke_* _lambda_ * P


'''calculo de campos electricos a partir de potenciales electricos'''











