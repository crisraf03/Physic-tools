import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Datos iniciales
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data)

# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
line, = ax.plot([], [], lw=2)

# Función de inicialización (vacío en este caso)
def init():
    line.set_data([], [])
    return line,

# Función de animación
def animate(frame):
    x = x_data[:frame]
    y = y_data[:frame]
    line.set_data(x, y)
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=len(x_data), init_func=init, blit=True)

# Mostrar la animación
plt.show()
