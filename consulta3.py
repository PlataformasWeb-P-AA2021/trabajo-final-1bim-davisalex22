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

# Consulta 1 Los cantones que tiene establecimientos con 0 número de profesores
consulta1 = session.query(Canton).filter(
    Establecimiento.num_docentes == 0).all()
print(" -- Cantones que tiene establecimientos con 0 número de profesores --\n")
print(consulta1)

# Consulta 2 Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21

consulta2 = session.query(Establecimiento).join(Parroquia).filter(and_(
    Parroquia.nombre_parrq == 'CATACOCHA', Establecimiento.num_estudiantes >= 21)).all()
print(" -- Establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21 --\n")
print(consulta2)
