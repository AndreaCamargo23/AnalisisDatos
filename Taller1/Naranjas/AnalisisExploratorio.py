import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df = pd.read_csv('OrangeQualityData.csv')
# Vista general
print("Primeras filas del dataset:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nDistribución de columnas categóricas:")
print("Color:\n", df['Color'].value_counts())
print("Variedad:\n", df['Variety'].value_counts())
print("Imperfecciones (Y/N):\n", df['Blemishes (Y/N)'].value_counts())
#1. ¿Qué tan dulce debe ser para tener buena calidad? (Brix vs Quality)
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Quality (1-5)', y='Brix (Sweetness)', palette='YlOrBr')
plt.title('Dulzor (Brix) según nivel de calidad')
plt.xlabel('Calidad')
plt.ylabel('Dulzor (Brix)')
plt.show()

#2. ¿Cuál es el color que más predomina entre las naranjas? (Variety vs Color)
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Color', hue='Variety', palette='Set2')
plt.title('Distribución de color según variedad')
plt.xlabel('Color')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.show()

# También el color predominante general
print("Color predominante general:")
print(df['Color'].value_counts().head(1))


#3. ¿Qué variedad tiene el tamaño de naranjas más grande? (Variety vs Size)
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Variety', y='Size (cm)', palette='cool')
plt.title('Tamaño de naranjas según variedad')
plt.xlabel('Variedad')
plt.ylabel('Tamaño (cm)')
plt.xticks(rotation=45)
plt.show()

# Medias por variedad
print("Promedio de tamaño por variedad:")
print(df.groupby('Variety')['Size (cm)'].mean().sort_values(ascending=False))

#4. Tiempo de cosecha vs peso
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='HarvestTime (days)', y='Weight (g)', hue='Variety', palette='tab10')
plt.title('Tiempo de cosecha vs peso')
plt.xlabel('Días de cosecha')
plt.ylabel('Peso (g)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Correlación simple
correlation = df[['HarvestTime (days)', 'Weight (g)']].corr().iloc[0, 1]
print(f"Correlación entre tiempo de cosecha y peso: {correlation:.2f}")


#5. ¿Cuál es el tipo de naranja más recomendable a cultivar según tamaño, dulzor y tiempo de cosecha?
recomendadas = df.groupby('Variety')[['Size (cm)', 'Brix (Sweetness)', 'HarvestTime (days)']].mean()
recomendadas = recomendadas.sort_values(by=['Size (cm)', 'Brix (Sweetness)'], ascending=[False, False])

print("Variedades ordenadas por tamaño y dulzor (de mayor a menor):")
print(recomendadas)

# Visualización
recomendadas.plot(kind='bar', figsize=(12, 6))
plt.title('Comparación entre variedades: tamaño, dulzor y tiempo de cosecha')
plt.ylabel('Media por métrica')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
