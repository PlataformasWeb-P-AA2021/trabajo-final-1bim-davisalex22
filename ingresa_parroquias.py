from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Parroquia, Canton
from configuracion import cadena_base_datos
import itertools
import csv

# Se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Lectura de datos csv
parroquias = open("data/Listado-Instituciones-Educativas.csv", "r", encoding= 'utf-8')
# Se declara una lista vacía 
parroquiasU = []
# Uso de intertools.islice para omitir el encabezado del csv
# Uso de append para extraer las columnas requeridas
for p in  itertools.islice(parroquias, 1, None): 
    # Se elimina el separador   
    cadenaParroquia = p.split("|")
    # Se elimina el salto de línea    
    cadenaParroquia[-1] = cadenaParroquia[-1].strip() 
    # Se agrega las columnas a la lista vacía   
    parroquiasU.append((cadenaParroquia[5],cadenaParroquia[6], cadenaParroquia[7]))

# Extraccion de registros unicos mediate set y tuple         
parroquiasU = list(set(tuple(parroquiasU)))
# Consulta a la tabla Canton
cantones = session.query(Canton).all()

# Ingreso de datos a tabla Parroquia
# Se recorre la lista parroquiasU
for p in parroquiasU:  
    # Se recorre la consulta cantones
    for c in cantones:
        # Se compara en nombre canton de parroquiasU con cantones
        if(p[0] == c.nombre_cant):
            # Se guarda el código canton en id_cant
            id_cant = c.cod_cant
    # Se agregan los datos a la Tabla        
    session.add(Parroquia(cod_parrq = p[1], nombre_parrq = p[2], canton_id = id_cant ))    

# Se confirma las transacciones       
session.commit()