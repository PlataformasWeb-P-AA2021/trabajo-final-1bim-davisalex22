from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Canton, Provincia
from configuracion import cadena_base_datos
import itertools
import csv

# Se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Lectura de datos csv
cantones = open("data/Listado-Instituciones-Educativas.csv", "r", encoding= 'utf-8')
# Se delara lista vacía
cantonesU = []

# Uso de intertools.islice para omitir el encabezado del csv
# Uso de append para extraer las columnas requeridas
for p in  itertools.islice(cantones, 1, None):  
    # Se elimina el separador   
    cadenaCanton = p.split("|")
    # Se elimina el salto de línea  
    cadenaCanton[-1] = cadenaCanton[-1].strip()   
    # Se agrega las columnas a la lista vacía    
    cantonesU.append((cadenaCanton[4],cadenaCanton[5], cadenaCanton[3]))

# Extraccion de registros unicos mediate set y tuple         
cantonesU = list(set(tuple(cantonesU)))
# Consulta a la tabla Provincia
provincias = session.query(Provincia).all()

# Ingreso de datos a tabla Cantones
# Se recorre la lista cantonesU
for c in cantonesU:  
    # Se recorre la consulta provincias
    for p in provincias:
        # Se compara en nombre canton de cantonesU con provincias
        if(c[2] == p.nombre_prov):
            # Se guarda el código provincia en id_prov
            id_prov = p.cod_prov
    # Se agregan los datos a la Tabla        
    session.add(Canton(cod_cant = c[0], nombre_cant = c[1], provincia_id = id_prov ))    

# Se confirma las transacciones       
session.commit()