#Diagrama de Pareto

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Establecer la semilla para reproducibilidad
np.random.seed(42)

# Simular datos
n_cursos = 8
cursos = ['Python para Data Science', 'Diseño Gráfico con Adobe Illustrator', 'Marketing Digital',
          'Desarrollo Web con React', 'Gestión de Proyectos', 'Finanzas Personales',
          'Inglés para Negocios', 'Machine Learning']
data = {
    'Curso': cursos,  # Mantener el orden original de los cursos
    'Inscripciones': np.random.randint(50, 500, size=n_cursos)  # Rango de 50 a 500 inscripciones
}

df = pd.DataFrame(data)

# Ordenar los cursos por número de inscripciones (descendente)
df = df.sort_values(by='Inscripciones', ascending=False).reset_index(drop=True)

# Calcular el porcentaje acumulado de inscripciones
df['Porcentaje'] = df['Inscripciones'] / df['Inscripciones'].sum() * 100
df['Porcentaje Acumulado'] = df['Porcentaje'].cumsum()

# Diagrama de Pareto
fig, ax1 = plt.subplots(figsize=(12, 6))

# Gráfico de barras (Inscripciones por curso)
sns.barplot(x='Curso', y='Inscripciones', data=df, ax=ax1)  # Sin palette para evitar la advertencia
ax1.set_title('Diagrama de Pareto: Inscripciones por Curso', fontsize=16)
ax1.set_xlabel('Curso', fontsize=12)
ax1.set_ylabel('Número de Inscripciones', fontsize=12)

# Asegurarse de que los ticks y las etiquetas estén correctamente alineados
ax1.set_xticks(range(len(df['Curso'])))
ax1.set_xticklabels(df['Curso'], rotation=45, ha='right')

# Crear un segundo eje para el porcentaje acumulado
ax2 = ax1.twinx()
ax2.plot(df['Curso'], df['Porcentaje Acumulado'], color='red', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('Porcentaje Acumulado (%)', fontsize=12)
ax2.set_ylim([0, 100])

# Mostrar líneas de cuadrícula en el segundo eje (porcentaje acumulado)
ax2.grid(False)

plt.tight_layout()
plt.show()
