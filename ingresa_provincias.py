from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Provincia
from configuracion import cadena_base_datos
import csv
import itertools

# Se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Lectura de datos csv
provincia = open("data/Listado-Instituciones-Educativas.csv", "r", encoding= 'utf-8')
# Se declara una lista vacía 
provinciaU = []
# Uso de intertools.islice para omitir el encabezado del csv
# Uso de append para extraer las columnas requeridas
for p in  itertools.islice(provincia, 1, None):  
    # Se elimina el separador 
    cadenaProvincia = p.split("|")
    # Se elimina el salto de línea
    cadenaProvincia[-1] = cadenaProvincia[-1].strip()    
    # Se agrega las columnas a la lista vacía
    provinciaU.append((cadenaProvincia[2],cadenaProvincia[3]))

# Extraccion de registros unicos mediate set y tuple        
provinciaU = list(set(tuple(provinciaU)))

# Ingreso de datos a tabla Provincia
for p in provinciaU:
    # Se agregan los datos a la Tabla
    session.add(Provincia(cod_prov = p[0], nombre_prov = p[1]))      

# Se confirma las transacciones       
session.commit()