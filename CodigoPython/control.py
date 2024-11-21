#Grafico de Control

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Semilla para la reproducibilidad
np.random.seed(42)

# Simulamos 30 semanas de calificaciones promedio de los estudiantes
n_semanas = 30
calificaciones_promedio = np.random.normal(loc=75, scale=5, size=n_semanas)  # Media 75, desviación estándar 5

# Crear DataFrame
df = pd.DataFrame({
    'Semana': np.arange(1, n_semanas + 1),
    'Calificación': calificaciones_promedio
})

# Cálculos para el gráfico de control
media = df['Calificación'].mean()
std_dev = df['Calificación'].std()

# Límites de control (3 desviaciones estándar por encima y por debajo de la media)
ucl = media + 3 * std_dev  # Upper Control Limit (Límite de Control Superior)
lcl = media - 3 * std_dev  # Lower Control Limit (Límite de Control Inferior)

# Crear Gráfico de Control
plt.figure(figsize=(12, 6))
plt.plot(df['Semana'], df['Calificación'], marker='o', label='Calificaciones', color='blue')
plt.axhline(media, color='green', linestyle='--', label='Media')
plt.axhline(ucl, color='red', linestyle='--', label='Límite Superior de Control (UCL)')
plt.axhline(lcl, color='red', linestyle='--', label='Límite Inferior de Control (LCL)')

# Añadir etiquetas y título
plt.title('Gráfico de Control: Calificaciones Promedio por Semana')
plt.xlabel('Semana')
plt.ylabel('Calificación Promedio')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar gráfico
plt.show()
