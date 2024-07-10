#Graph of oscilators

import numpy as np
import math

'''Armonic oscilator'''

'''notation x[n] : n-derivation of the x funcion respect the time "t" '''

# Definir una función para verificar las variables
def check_variables(**kwargs):
    for var_name, var_value in kwargs.items():
        if var_value is None:
            raise ValueError(f'Need to define {var_name}')

def armonic_function(t,w,a,b):
    phi = math.atan(b/a)
    A = np.sqrt(a**2 + (b)*2 )
    x= A*np.sin(w*t + phi) # x =  A sin(wt + phi)
    return x

'''equation 1 : x[2] + w**2 x = 0 // solution : x(t) = x(0) cos(wt) + x[1](0) sin(wt)/w '''

def armonic_oscilator(t, w=None, x0=None, v0=None):
    check_variables(w=w, x0=x0, v0=v0) #check that the variables are defined
    a,b = x0 , v0/w #calculate the values of the function
    x = armonic_function(t,w,a,b)
    return x # Elongation

'''equation 2 : x[2]+ gamma*x[1] + w**2 x = 0 // solution : x(t) = exp(gamma/2 t) { x(0) cos(wat) + [x[1](0) + gamma/2 x(0)] sin(wat)/wa }  where wa = sqrt(x**2 - 1/4* gamma**2 )'''

def damped_harmonic_oscillator(t, w=None, gamma=None, x0=None, v0=None):
    check_variables(w=w, gamma=gamma, x0=x0, v0=v0) #check that the variables are defined
    wa = np.sqrt(w**2 - 0.25*gamma**2)
    a,b = x0 , (v0 + gamma/2 * x0)/wa #calculate the values of the function
    damping = np.exp(-gamma * t)
    x = damping * armonic_function(t,wa,a,b)
    return x


class perturbations:
    def __init__(self,t,w,gamma=0):
        self.t = t 
        self.gamma = gamma
        self.w = w

    def constant(self, parameter):
        '''constant f(t) = c'''
        c = parameter
        external_force = c
        wa = np.sqrt(self.w**2- self.gamma**2/4)
        perturbation = c * (1- np.cos(wa*self.t) ) / wa
        return (external_force, perturbation) 

    def lineal(self,parameter):
        '''constant f(t) = at'''
        a = parameter
        external_force = a * self.t
        wa = np.sqrt(self.w**2- self.gamma**2/4)
        perturbation = (a/wa**2) * (self.t - np.sin(wa*self.t) / wa )
        return (external_force, perturbation) 

    def harmonic(self, parameter):
        '''constant f(t) = sin(nu*t)'''
        nu = parameter
        external_force = np.sin(nu* self.t)
        perturbation = (nu/(self.w**2-nu**2)) * (np.sin(self.w*self.t)- np.sin(nu*self.t) )
        return (external_force, perturbation) 

    def damping(self, parameter):
        '''constant f(t) = exp(-alpha*t)'''
        alpha = parameter
        external_force = np.exp(-alpha*self.t)
        amplitud = np.sqrt((alpha/self.w)**2 + 1)
        phase = math.atan(-self.w/alpha)
        perturbation = external_force + amplitud * np.sin(self.w * self.t + phase) 
        perturbation = perturbation / (self.w**2 + alpha**2)
        return (external_force, perturbation) 



import matplotlib.pyplot as plt



def plot_damped_harmonic_with_perturbations(t_values, _w_, _gamma_, _x0_ = 1, _v0_ = 0, _parameter_ = 0, perturbation_type= 'constant'):
    if _gamma_ == 0:
        x = armonic_oscilator(t_values ,w=_w_, x0 = _x0_, v0= _v0_)
        _perturbation_ = perturbations(t_values, w= _w_ , gamma= _gamma_)

    if _gamma_ != 0:
        x = damped_harmonic_oscillator(t_values,w = _w_ ,gamma=_gamma_, x0 = _x0_, v0= _v0_)
        _perturbation_ = perturbations(t_values, w= _w_ , gamma= _gamma_)

    if perturbation_type == 'constant':
        x_perturbation = _perturbation_.constant(_parameter_) [1]
    elif perturbation_type == 'lineal':
        x_perturbation = _perturbation_.lineal(_parameter_)[1]
    elif perturbation_type == 'harmonic':
        x_perturbation = _perturbation_.harmonic(_parameter_)[1]
    elif perturbation_type == 'damping':
        x_perturbation = _perturbation_.damping(_parameter_)[1]
    else:
        raise ValueError("Type of perturbation not Valid")
    

   # Graficar la función original con línea discontinua
    _label_phrase_ = f'$\omega$ = {_w_} , $\gamma$ = {_gamma_}, $x_{0}$ = {_x0_} , $v_{0}$ = {_v0_}'

    line, = plt.plot(t_values, x, '-', label=_label_phrase_ )
    color = line.get_color()  # Obtener el color de la línea
    
    if _parameter_ != 0:
        _label_phrase_ = f' _para_ = {_parameter_}'
        # Sumar la perturbación
        x += x_perturbation
        
        # Graficar la función perturbada con línea continua y el mismo color
        plt.plot(t_values, x, '--',label = _label_phrase_, color=color)






t_values =  np.linspace(0, 10, 1000)
_gamma_ = 0.1
_x0_ = 2
_v0_ = 1
_parameter_ = 0.5


factor = 1
perturbation_type = 'constant'


for number in range(1,4,1):
    _w_ = number*factor*2
    _gamma_ = 1/_w_
    plot_damped_harmonic_with_perturbations(t_values, _w_, _gamma_, _x0_ = _x0_, _v0_ = _v0_, _parameter_ = _parameter_, perturbation_type = perturbation_type)

plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()

if _parameter_ == 0:
    perturbation_type = 'No'

plt.title(f'Damped Harmonic Oscillator with {perturbation_type.capitalize()} Perturbations')
plt.legend(bbox_to_anchor=(1.05, 0.5), loc='best')
plt.savefig('img.png')

plt.show()