from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # Se importa el operador and
# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia
# Se importa información del archivo configuracion
from configuracion import cadena_base_datos
# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1 Las parroquias que tienen establecimientos únicamente en la jornada Nocturna.

consulta1 = session.query(Parroquia).join(Establecimiento).filter(
    Establecimiento.jornada == 'Nocturna').all()
print(" -- Parroquias con establecimientos en jornada nocturna --\n")
print(consulta1)

# Consulta 2 Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459

consulta2 = session.query(Canton).join(Parroquia, Establecimiento).filter(or_(Establecimiento.num_estudiantes == 448, Establecimiento.num_estudiantes == 450,
                                                                              Establecimiento.num_estudiantes == 451, Establecimiento.num_estudiantes == 454,
                                                                              Establecimiento.num_estudiantes == 458, Establecimiento.num_estudiantes == 459)).all()
print(" -- Cantones con establecimientos que tienen número de estudiantes ... --\n")
print(consulta2)
