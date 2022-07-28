# Importando la Base de Datos
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

datos = pd.read_csv('C:/Users/oscar/Documents/Program_ONE/Rutas_Opcionales/Python_Data_Science/Data-Visualization-Explorando-con-Seaborn/credit_card.csv', sep = ',')
print('Base de Datos - Credit Card')
print(f'{datos} \r\n')

print('Informacion de la base de Datos\r\n')
print(f'{datos.info()} \r\n')

print('Traduciendo las Variables de las Columnas')
print(f'{datos.columns} \r\n')
dic_columnas = {
    'LIMIT_BAL': 'Limite' ,
    'CHECKING_ACCOUNT': 'Cuenta_Corriente' ,
    'EDUCATION': 'Escolaridad',
    'MARRIAGE': 'Estado_Civil',
    'AGE': 'Edad',
    'BILL_AMT': 'Valor_Factura',
    'PAY_AMT': 'Valor_Pago',
    'DEFAULT': 'Moroso'
    }

tarjetas = datos.rename(columns=dic_columnas)
print(f'{tarjetas.head()} \r\n')

#continuacion del cambio de nombre de las variables
print(tarjetas.Cuenta_Corriente.unique())

dic_cuenta = {
    'Yes': 'Si',
    'No': 'No'
}

print(f'{tarjetas.Cuenta_Corriente.map(dic_cuenta)} \r\n')
print(f'{tarjetas.head()} \r\n')

tarjetas.Cuenta_Corriente = tarjetas.Cuenta_Corriente.map(dic_cuenta)
print(f'{tarjetas.head()}\r\n')

print(f'{tarjetas.Escolaridad.unique()}\r\n')
dic_escolaridad = {
    '2.University' : '2.Universidad',
    '3.Graduate School' : 'Post-graduacion',
    '1.High School' : '1.Colegio'
}

tarjetas.Escolaridad = tarjetas.Escolaridad.map(dic_escolaridad)
print(f'{tarjetas.head()}\r\n')

print(f'{tarjetas.Estado_Civil.unique()}\r\n')

dic_Estado_Civil = {
    'Married': 'Casado/a',
    'Single': 'Soltero/a'
}

tarjetas.Estado_Civil= tarjetas.Estado_Civil.map(dic_Estado_Civil)
print(f'{tarjetas.head()}\r\n')

print('Analisis 1 \r\n')
#sns.displot(tarjetas['Limite']) # Forma anterior de como visualizar el grafico en la version anterior
#sns.displot(data=tarjetas, x='Limite', hue='Escolaridad') #Forma actual para visualizar el grafico con la nueva version

print('Analisis 2 \r\n')
tarjetas['iu'] = tarjetas['Valor_Factura'] / tarjetas['Limite'] # iu es el porcentaje de uso
#sns.displot(data=tarjetas, x='iu')
print('Del grafico no.3 nos muestra que existe un publico que usa poco el limite que tiene disponible en su tarjeta \r\n')

print('Estilos y Colores \r\n')
print('Estilo 1 \r\n')
#sns.set_style('whitegrid') # Estilo 1
#sns.displot(data=tarjetas, x='Limite', hue='Escolaridad')

print('Estilo 2 \r\n')
#sns.set_style('darkgrid') # Estilo 2
#sns.displot(data=tarjetas, x='Limite', hue='Escolaridad')

print('Estilo 3, modificando paleta de colores \r\n')
#sns.set_style('darkgrid') # Estilo 2
#sns.displot(data=tarjetas, x='Limite', hue='Escolaridad', palette='plasma') #tambien se le puede modificar la paleta de colores

print('Analisis de Variables Categoricas \r\n')
#sns.countplot(x='Cuenta_Corriente', data=tarjetas, hue='Moroso')

print('Analisis de Variables Categoricas 2\r\n')
#sns.catplot(x='Estado_Civil', y='Limite', data=tarjetas, hue='Moroso', dodge=True)
#sns.swarmplot(x='Escolaridad', y='iu', data=tarjetas) con este grafico no fue posible mostrar el 100% de la informacion

#sns.boxplot(x='Escolaridad', y='iu', data=tarjetas, hue='Moroso')

#sns.violinplot(x='Escolaridad', y='iu', data=tarjetas, hue='Moroso')

print(tarjetas.head())

print(tarjetas.Edad.unique())

bins = [20, 30, 40, 50, 100]
nombres = ['20-30', '30-40', '40-50', '50+']

tarjetas['rango_edad'] = pd.cut(tarjetas['Edad'], bins, labels=nombres)
print(tarjetas.head())

#grafico de limite de credito por rango de edad
#sns.boxplot(x='rango_edad', y='Limite', data=tarjetas)

print('Analisis de Variables Numericas \r\n')
print(tarjetas.head())

#grafico de distribucion por escolaridad
#sns.displot(data=tarjetas, x='Limite', col='Escolaridad', kind='kde', hue='rango_edad')

#Vamos a utilizar el grafico de Dispersion
sns.scatterplot(x='iu', y='Valor_Factura', data=tarjetas)


plt.show()