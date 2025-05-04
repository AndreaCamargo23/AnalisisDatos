import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('penguins_size.csv')
print (df)
#DATOS FALTANTES
#calcular los datos 
print (df.isnull().sum())
print (df.isnull().mean()*100)

#contar la cantidad de datos por columna 
print(df["sex"].value_counts())

#Eliminar filas
df = df.drop(index=339) 
df = df.drop(index=3) 
print (df)

#contar la cantidad de datos por columna 
print(df["sex"].value_counts())
print (df.isnull().sum())

df.replace({'.', 'unknow'})
df['sex'] = df['sex'].fillna('unknow')
print(df["sex"].value_counts())
print (df.isnull().sum())

#DATOS DUPLICADOS
# Mostrar filas duplicadas
print('duplicados: ', df[df.duplicated()])


#DATOS ANOMALOS
#Categoricos: islas y especies
values = df["island"].value_counts()
values.plot(kind='bar')

#datos anomalos en los datos numericos

df_numeric = df.select_dtypes(include=['culmen_length_mm'])

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_numeric)
plt.xticks(rotation=45)
plt.title('Boxplot de Variables Numéricas')
plt.tight_layout()
plt.show()
