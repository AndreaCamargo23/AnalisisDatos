import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#leer el csv
df = pd.read_csv('sales_videoGame.csv')
#imprimir la tabla
print("Dimensiones:", df.shape)
print(df.columns)
print(df.head())
print(df.info())

# Agrupamos por Género y Rating, y sumamos las ventas globales
ventas_por_genero_rating = df.groupby(['Genre', 'Rating'])['Global_Sales'].sum().reset_index()

# Ordenamos de mayor a menor por ventas
ventas_ordenadas = ventas_por_genero_rating.sort_values(by='Global_Sales', ascending=False)

# Mostramos el top 10
print(ventas_ordenadas.head(10))
# Agrupar por Rating y sumar las ventas globales
ventas_por_rating = df.groupby('Rating')['Global_Sales'].sum().reset_index()

# Ordenar de mayor a menor
ventas_por_rating = ventas_por_rating.sort_values(by='Global_Sales', ascending=False)

# Mostrar la tabla
print(ventas_por_rating)

# Preprocesamiento de datos
print("PREPROCESAMIENTO DE DATOS")
print("Data Cleaning")
#Cantidad de nulos por columna
print(df.isnull().sum())
#Buscar las filas que tienen nulo el nombre del Juego
print(df[df['Name'].isnull()])
#Borrar estas filas
df = df.drop(index=659) 
df = df.drop(index=14246) 

# Eliminar filas donde la columna 'Rating' es nula
df = df.dropna(subset=['Rating'])

#Se le asigna un valor a los valores nulos de Publisher y las otras columnas con mayores valores nulos
df['Publisher'] = df['Publisher'].fillna('unknow')
df['Critic_Score'] = df['Critic_Score'].fillna('0')
df['Critic_Count'] = df['Critic_Count'].fillna('0')
df['User_Score'] = df['User_Score'].fillna('0')
df['User_Count'] = df['User_Count'].fillna('0')
df['Year_of_Release'] = df['Year_of_Release'].fillna('0')

#Cantidad de nulos por columna
print(df.isnull().sum())

# Datos Duplicados
print("Cantidad de filas dupliadas: ", df.duplicated().sum())

#Datos Atipicos
values = df['Name'].value_counts()
values.plot(kind='bar')



