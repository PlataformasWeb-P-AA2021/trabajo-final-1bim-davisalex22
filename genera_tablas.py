from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from configuracion import cadena_base_datos

# Se genera en enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)
Base = declarative_base()

# Genera clase Establecimiento
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    cod_amie = Column(String, nullable=false)
    nombre_est = Column(String, nullable=false)
    cod_distrito = Column(String, nullable=false)
    sostenimiento = Column(String, nullable=false)
    tipo_educacion = Column(String, nullable=false)
    modalidad = Column(String, nullable=false)
    jornada = Column(String, nullable=false)
    acceso = Column(String, nullable=false)
    num_estudiantes = Column(Integer, nullable=false)
    num_docentes = Column(Integer, nullable=false)
    parroquia_id = Column(String, ForeignKey('parroquia.cod_parrq'))
    parroquia = relationship("Parroquia", back_populates="establecimientos")

    def __repr__(self):
        return "[ Establecimiento %d = Nombre:%s - Numero de distrito: %s - Sostenimiento: %s - Tipo Educacion: %s - Modalidad: %s - Jornada: %s - Acceso: %s - Numero Estudiantes: %d - Numero Docenctes: %d] \n..........\n" % (
            self.id,
            self.nombre_est,
            self.cod_distrito,
            self.sostenimiento,
            self.tipo_educacion,
            self.modalidad,
            self.jornada,
            self.acceso,
            self.num_estudiantes,
            self.num_docentes)

# Genera clase Parroquia
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    cod_parrq = Column(String, nullable=False)
    nombre_parrq = Column(String, nullable=False)
    establecimientos = relationship("Establecimiento", back_populates="parroquia")
    canton_id = Column(String, ForeignKey('canton.cod_cant'))
    canton = relationship("Canton", back_populates="parroquias")

    def __repr__(self):
        return "[ Parroquia %d: Codigo Parroquia: %s - Nombre Parroqui: %s ] \n ..........\n" % (
            self.id,
            self.cod_parrq,
            self.nombre_parrq
        )
# Genera clase Canton
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    cod_cant = Column(String, nullable=False)
    nombre_cant = Column(String, nullable=False)
    parroquias = relationship("Parroquia", back_populates="canton")
    provincia_id = Column(String, ForeignKey('provincia.cod_prov'))
    provincia = relationship("Provincia", back_populates="cantones")

    def __repr__(self):
        return "[ Canton %d: Codigo Canton: %s - Nombre Canton: %s ]\n..........\n" % (
            self.id,
            self.cod_cant,
            self.nombre_cant
        )

# Genera clase Provincia
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    cod_prov = Column(String, nullable=False)
    nombre_prov = Column(String, nullable=False)
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "[ Provincia: Codigo Provincia: %s - Nombre Provincia: %s ]\n..........\n" % (
            self.cod_prov,
            self.nombre_prov
        )


Base.metadata.create_all(engine)
