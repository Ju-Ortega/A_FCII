import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetro del oscilador de Van der Pol
mu = 1.0

# Función para la aceleración (du/dt)
def f(x, u):
    return -x + mu * (1 - x**2) * u

# Inicialización de los parámetros
tmax = 50.0  # Tiempo máximo para observar
h = 0.01      # Paso de tiempo
t = np.arange(0, tmax, h)  # Vector de tiempo

# Arrays vacíos para posición y velocidad
x = np.empty(t.size)  # Posición
u = np.empty(t.size)  # Velocidad

# Condiciones iniciales
x[0] = 1.0  # Posición inicial
u[0] = 0.0  # Velocidad inicial

# Paso inicial para la velocidad (Leapfrog)
u[0] -= 0.5 * h * f(x[0], u[0])

# Bucle Leapfrog para resolver el sistema
for n in range(t.size - 1):
    u[n + 1] = u[n] + h * f(x[n], u[n])  # Actualización de la velocidad
    x[n + 1] = x[n] + h * u[n + 1]      # Actualización de la posición

# Configuración de la figura para la animación
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)  # Rango para posición
ax.set_ylim(-3, 3)  # Rango para velocidad
ax.set_xlabel("Posición (x)")
ax.set_ylabel("Velocidad (u)")
ax.grid()

# Línea que se irá actualizando en la animación
line, = ax.plot([], [], lw=2)

# Función de inicialización para la animación
def init():
    line.set_data([], [])
    return line,

# Función de actualización para la animación
def update(frame):
    line.set_data(x[:frame], u[:frame])  # Actualiza los datos hasta el frame actual
    return line,

# Creación de la animación
ani = FuncAnimation(
    fig, update, frames=len(t), init_func=init, blit=True, interval=30, repeat=False
)

# Mostrar la animación
plt.show()
