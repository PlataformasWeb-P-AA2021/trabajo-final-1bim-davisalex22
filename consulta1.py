from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_  # Se importa el operador and
# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia
# Se importa información del archivo configuracion
from configuracion import cadena_base_datos
# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1 Todos los establecimientos de la provincia de Loja.

consulta1 = session.query(Establecimiento).join(
    Parroquia, Canton, Provincia).filter(Provincia.nombre_prov == 'LOJA').all()
print(" -- Establecimientos de la Provincia de Loja --\n")
print(consulta1)

# Consulta 2 Todos los establecimientos del cantón de Loja.

consulta2 = session.query(Establecimiento).join(
    Parroquia, Canton, Provincia).filter(Canton.nombre_cant == 'LOJA').all()
print(" -- Establecimientos del Cantón Loja --\n")
print(consulta2)
