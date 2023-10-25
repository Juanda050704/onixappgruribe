import pandas as pd

from helpers.crearCSV import crearCSV
from helpers.crearTablaHTML import crearTabla

from data.ventas import *
from data.Productos import *
from data.empleados import *
#1. Crear un CSV con los datos de las ventas
crearCSV(ventas,'ventas.csv', nombresVentas)
crearCSV(Productos,'Productos.csv', nombresProdructos)
crearCSV(empleados, 'empleados.csv',Nombre_empleados)

#2. Cargo la fuente datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv')
crearTabla(ventasDataFrame,'tablaventas')

ProductosDataFrame=pd.read_csv('data/Productos.csv')
crearTabla(ProductosDataFrame, 'tablaproductos')

empleadosDataFrame=pd.read_csv('data/empleados.csv')
crearTabla(empleadosDataFrame, 'tablaempleados')
#print(ventasDataFrame)

#3. Explorar los datos
examen1=ventasDataFrame.head()
examen2=ventasDataFrame.tail()
examen3=ventasDataFrame.head(20)
examen4=ventasDataFrame.info()
examen5=ventasDataFrame.describe()
examen6=ventasDataFrame.tail(50)


#4. Filtrar y ordenar(limpiar)

#5. Modelar o aplicar modelos Estadistica

#6. Presentar y exportar los datos


