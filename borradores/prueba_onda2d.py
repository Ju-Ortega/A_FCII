import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
Lx, Ly = 1.0, 1.0  # Tamaño del dominio en x y y
Nx, Ny = 100, 100  # Número de puntos en cada dirección
dx = Lx / (Nx - 1)  # Paso espacial en x
dy = Ly / (Ny - 1)  # Paso espacial en y
c = 1.0  # Velocidad de la onda
h = 0.005  # Paso temporal
tmax = 2.0  # Tiempo máximo de simulación

# Inicialización de las matrices
u = np.zeros((Nx, Ny))  # Estado actual de la onda
u_prev = np.zeros((Nx, Ny))  # Estado en el tiempo anterior
u_next = np.zeros((Nx, Ny))  # Estado en el siguiente paso

# Condición inicial: un pulso en el centro del dominio
u[Nx // 2, Ny // 2] = 1.0

# Parámetros de la animación con fondo blanco
fig, ax = plt.subplots(facecolor="white")  # Fondo blanco
im = ax.imshow(u, cmap='inferno', extent=[0, Lx, 0, Ly], origin='lower', vmin=-1, vmax=1)
plt.colorbar(im)

def update(frame):
    global u, u_prev, u_next
    
    # Bucle sobre cada punto interior del dominio
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            laplacian = (u[i+1, j] - 2*u[i, j] + u[i-1, j]) / dx**2 + \
                        (u[i, j+1] - 2*u[i, j] + u[i, j-1]) / dy**2
            u_next[i, j] = 2 * u[i, j] - u_prev[i, j] + c**2 * h**2 * laplacian
    
    # Actualización de los estados
    u_prev, u, u_next = u, u_next, u_prev
    
    # Actualización de la imagen
    im.set_array(u)
    return [im]

# Animación de la onda
ani = FuncAnimation(fig, update, frames=int(tmax / h), blit=True)
plt.show()
