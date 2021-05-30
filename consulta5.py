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

# Consulta 1 Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.

consulta1 = session.query(Establecimiento).join(Parroquia).filter(and_(Establecimiento.num_docentes >
                                                                       20, Establecimiento.tipo_educacion.like("%Permanente%"))).order_by(Parroquia.nombre_parrq).all()
print(" -- Establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena Permanente en tipo de educación --\n")
print(consulta1)

# Consulta 2 Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.

consulta2 = session.query(Establecimiento).filter(
    Establecimiento.cod_distrito == "11D02").order_by(Establecimiento.sostenimiento).all()
print(" -- Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02 --\n")
print(consulta2)
