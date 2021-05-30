from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_  # se importa el operador and
# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia
# Se importa información del archivo configuracion
from configuracion import cadena_base_datos
# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()
# Consulta 1 Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.

consulta1 = session.query(Establecimiento).filter(
    Establecimiento.num_docentes > 100).order_by(Establecimiento.num_estudiantes).all()
print(" -- Establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores --\n")
print(consulta1)

# Consulta 2 Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.

consulta2 = session.query(Establecimiento).filter(
    Establecimiento.num_docentes > 100).order_by(Establecimiento.num_docentes).all()
print(" -- Establecimientos ordenados por número de profesores; que tengan más de 100 profesores. ... --\n")
print(consulta2)
