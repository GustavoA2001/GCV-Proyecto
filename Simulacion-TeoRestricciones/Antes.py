import matplotlib.pyplot as plt
import numpy as np

# Datos ficticios sobre la frecuencia de cada problema
problemas = ['Falta de recursos', 'Insuficientes instructores especializados', 'Contenido de baja calidad o desactualizado',
             'Errores en los materiales escritos', 'Problemas técnicos', 'Incompatibilidad con el contenido de enseñanza']
frecuencias = [14, 29, 37, 20, 25, 32]

# Ordenar los datos de mayor a menor frecuencia
indices = np.argsort(frecuencias)[::-1]
problemas = [problemas[i] for i in indices]
frecuencias = [frecuencias[i] for i in indices]

# Calcular el porcentaje acumulado
porcentaje_acumulado = np.cumsum(frecuencias) / np.sum(frecuencias) * 100

# Crear el diagrama de Pareto
fig, ax1 = plt.subplots(figsize=(12, 6))

# Graficar las barras para las frecuencias
ax1.bar(problemas, frecuencias, color='skyblue')
ax1.set_xlabel('Causa del problema')
ax1.set_ylabel('Frecuencia', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title('Diagrama de Pareto: Causas de Problemas en la Creación de Cursos', fontsize=14)
ax1.set_xticklabels(problemas, rotation=45, ha='right')
ax1.grid(axis='y', linestyle='--')

# Crear un segundo eje y para la curva acumulada
ax2 = ax1.twinx()
ax2.plot(problemas, porcentaje_acumulado, color='red', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('Porcentaje Acumulado (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Añadir los valores del porcentaje acumulado encima de cada punto de la línea
for i in range(len(problemas)):
    ax2.text(i, porcentaje_acumulado[i] + 2, f'{porcentaje_acumulado[i]:.1f}%', ha='center', color='red')

# Línea de Pareto (80%) en el gráfico
ax2.axhline(y=80, color='green', linestyle='--', label='80%')
ax2.legend()

# Ajustar el espacio para que todo se vea bien
plt.tight_layout()
plt.show()
