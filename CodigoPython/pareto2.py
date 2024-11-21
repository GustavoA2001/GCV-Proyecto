#Diagrama de Pareto

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos ficticios (reemplazar con tus propios datos)
data = {
    'Error': ['Video no carga', 'Plataforma lenta', 'Material desactualizado', 'Dificultad para navegar', 'Otro'],
    'Frecuencia': [150, 120, 80, 50, 30]
}

df = pd.DataFrame(data)

# Calcular porcentajes
df['Porcentaje'] = df['Frecuencia'] / df['Frecuencia'].sum() * 100
df['Porcentaje Acumulado'] = df['Porcentaje'].cumsum()

# Ordenar por frecuencia
df = df.sort_values(by='Frecuencia', ascending=False)

# Crear el diagrama
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(df['Error'], df['Frecuencia'])
ax1.set_xlabel('Tipo de Error')
ax1.set_ylabel('Frecuencia')

ax2 = ax1.twinx()
ax2.plot(df['Error'], df['Porcentaje Acumulado'], color='red', marker='o')
ax2.set_ylabel('Porcentaje Acumulado (%)')

plt.title('Diagrama de Pareto: Errores en la Plataforma')
plt.xticks(rotation=45)
plt.grid(False)
plt.show()