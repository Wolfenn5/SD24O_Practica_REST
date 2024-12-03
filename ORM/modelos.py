# Mapear clases
from ORM.config import BaseClass # traer del archivo config.py la clase BaseClass (declarative_base) para poder mapear las tablas
from sqlalchemy import column, String, Integer, DateTime, ForeignKey, Float # traer los tipos de dato que usa sqlalchemy
import datetime # para calcular la hora actual del pc, porque la columna fecha_registro de la tabla alumnos es de tipo TIMESTAMP WITH TIME ZONE


# Clases de tipo BaseClass por cada tipo de tabla que hay en la BD (alumnos, calificaciones, fotos)
# __tablename__= Nombre_tabla_BD
# --> column(tipo de dato de sqlalchemy)       tambien puede tener argumentos extras

# -----argumentos extras-----
# primary_key=True          indica que el id es una llave primaria
# ForeignKey(arg1, arg2)    indica que es una llave foranea donde tiene 2 parametros. La tabla que se referencia y cual es la llave
# "email"                   indica que es formato email. Por ejemplo, si no se pone un @, no se inserta
# timezone= True            indica que se inserte con la zona horaria
# default=                  indica que por "default" se obtiene la fecha y hora del dispositivo con datetime.datetime.now




# Tabla alumnos
class Alumno(BaseClass):
    __tablename__= "alumnos"
    id= column(Integer, primary_key= True)
    nombre= column(String(100))
    edad= column(Integer)
    domicilio= column(String(100))
    carrera= column(String(100))
    trimestre= column(String(100))
    email= column("email",String(100)) 
    password= column(String(100))
    fecha_registro= column(DateTime(timezone=True)), default= datetime.datetime.now   


# Tabla calificaciones
class Calificacion(BaseClass):
    __tablename__= "calificaciones" 
    id= column(Integer, primary_key= True)
    id_alumno= (Integer, ForeignKey(Alumno.id)) # indica que es llave foranea de la tabla Alumno y es el id
    uea= (String(100))
    calificacion= (String(100))

# Tabla fotos
class Foto(BaseClass):
    __tablename__=