import pandas as pd

df = pd.read_csv('penguins_size.csv')
print (df)

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
