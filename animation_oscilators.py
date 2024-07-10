import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def animate_damped_harmonic(t_values, x_values, title="Damped Harmonic Oscillator Animation", xlabel="t", ylabel="x(t)", interval=200):
    """
    Crea una animación de un oscilador amortiguado con perturbaciones.

    Parameters:
        t_values (array-like): Array de valores de tiempo.
        x_values (array-like): Array de valores de posición en función del tiempo.
        title (str): Título de la animación.
        xlabel (str): Etiqueta del eje X.
        ylabel (str): Etiqueta del eje Y.
        interval (int): Intervalo entre cuadros en milisegundos.
    """
    # Crear la figura y el eje
    fig, ax = plt.subplots()
    ax.set_xlim(np.min(t_values), np.max(t_values))
    ax.set_ylim(np.min(x_values), np.max(x_values))
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid()

    # Línea inicial vacía
    line, = ax.plot([], [], lw=2)

    # Función de inicialización (vacía en este caso)
    def init():
        line.set_data([], [])
        return line,

    # Función de animación
    def animate(frame):
        x = t_values[:frame]
        y = x_values[:frame]
        line.set_data(x, y)
        return line,

    # Crear la animación
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(t_values), interval=interval, blit=True)

    # Mostrar la animación
    plt.show()

# Ejemplo de uso
t_values = np.linspace(0, 10, 100)
x_values_list = []
for number in range(1, 3):
    _w_ = number * 0.5
    _gamma_ = (number + 3) / 10
    x_values = np.sin(_w_ * t_values) * np.exp(-_gamma_ * t_values)
    x_values_list.append(x_values)

# Anima cada conjunto de datos
for i, x_values in enumerate(x_values_list):
    animate_damped_harmonic(t_values, x_values, title=f'Damped Harmonic Oscillator Animation {i+1}')

