import numpy as np
import matplotlib.pyplot as plt

# Definición de las variables iniciales
errores_promedio_antes = 10  
n_estudiantes = 500  # Número total de estudiantes

# Simulación del estado después de aplicar mejoras
mejora_calidad = errores_promedio_antes * 0.7  
nuevos_estudiantes = int(n_estudiantes * 0.8)  

# Generar nuevos números de errores (considerando una distribución de Poisson)
# La distribución de Poisson es adecuada para modelar eventos raros como la detección de errores
nuevos_errores = np.random.poisson(lam=mejora_calidad, size=nuevos_estudiantes)

# Diagrama de Control
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, nuevos_estudiantes + 1), nuevos_errores, marker='o', linestyle='-', color='b')
plt.axhline(y=mejora_calidad, color='r', linestyle='--', label=f'Límite superior (Mejorado): {mejora_calidad} errores')
plt.title('Diagrama de Control - Calidad de Materiales (Después)')
plt.xlabel('Número de Estudiantes')
plt.ylabel('Número de Errores Detectados')
plt.legend()
plt.grid(True)
plt.show()
