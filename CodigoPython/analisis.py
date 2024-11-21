#Analisis de tendencia

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Establecer la semilla para reproducibilidad
np.random.seed(42)

# Simular datos
n_cursos = 8
cursos = ['Python para Data Science', 'Diseño Gráfico con Adobe Illustrator',
          'Marketing Digital', 'Desarrollo Web con React', 'Gestión de Proyectos',
          'Finanzas Personales', 'Inglés para Negocios', 'Machine Learning']

# Simulación de inscripciones para 12 meses por curso (8 cursos, 12 meses)
meses = [f'Mes {i+1}' for i in range(12)]
data = {
    'Curso': np.repeat(cursos, 12),
    'Mes': meses * n_cursos,
    'Inscripciones': np.random.randint(50, 500, size=n_cursos * 12)  # Inscripciones aleatorias
}

# Convertir a DataFrame
df = pd.DataFrame(data)

# Convertir la columna 'Mes' a un número entero para mantener el orden correcto
df['Mes'] = df['Mes'].str.extract('(\d+)').astype(int)

# Gráfico de tendencias: Inscripciones a lo largo de los meses
plt.figure(figsize=(14, 8))

# Gráfico de líneas que muestra la tendencia de inscripciones por curso
sns.lineplot(x='Mes', y='Inscripciones', hue='Curso', data=df, marker='o')

plt.title('Tendencia de Inscripciones por Curso a lo Largo del Tiempo', fontsize=16)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Número de Inscripciones', fontsize=12)
plt.grid(True)

# Asegurar que las etiquetas no se solapen
plt.xticks(ticks=np.arange(1, 13), labels=meses, rotation=45)

plt.tight_layout()
plt.show()
