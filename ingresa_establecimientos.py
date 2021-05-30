from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Establecimiento, Parroquia
from configuracion import cadena_base_datos
import csv
import itertools

# Se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Lectura de datos csv
establecimientos = open("data/Listado-Instituciones-Educativas.csv", "r", encoding= 'utf-8')
# Se delara lista vacía
establecimientos1= []
# Uso de intertools.islice para omitir el encabezado del csv
# Uso de append para extraer las columnas requeridas
for p in  itertools.islice(establecimientos, 1, None):
    # Se elimina el separador     
    cadenaE = p.split("|")
    # Se elimina el salto de línea    
    cadenaE[-1] = cadenaE[-1].strip() 
    # Se agrega las columnas a la lista vacía      
    establecimientos1.append((cadenaE[7],cadenaE[0],cadenaE[1], cadenaE[8] , 
                        cadenaE[9],cadenaE[10], cadenaE[11] , cadenaE[12],
                        cadenaE[13],cadenaE[14], cadenaE[15]))

# Extraccion de registros unicos mediate set y tuple         
establecimientos1 = list(set(tuple(establecimientos1)))
# Consulta a la tabla Parroquia
parroquias = session.query(Parroquia).all()

# Ingreso de datos a tabla Establecimiento
# Se recorre la lista establecimientos1
for e in establecimientos1:  
    # Se recorre la consulta parroquias
    for p in parroquias:
        # Se compara en nombre parroquia de establecimientos1 con parroquias
        if(e[0] == p.nombre_parrq):
            # Se guarda el código parroquia en id_parrq
            id_parrq = p.cod_parrq
    # Se agregan los datos a la Tabla   
    session.add(Establecimiento(cod_amie = e[1], nombre_est = e[2], cod_distrito = e[3], sostenimiento = e[4],
                                tipo_educacion = e[5], modalidad = e[6], jornada = e[7], acceso = e[8],
                                num_estudiantes = e[9], num_docentes = e[10], parroquia_id = id_parrq))    

# Se confirma las transacciones      
session.commit()