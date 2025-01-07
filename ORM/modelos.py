from sqlalchemy import Column, String, Integer, DateTime, ForeignKey # traer los tipos de dato que usa sqlalchemy
import datetime # para calcular la hora actual del pc, porque la columna fecha_registro de la tabla alumnos es de tipo TIMESTAMP WITH TIME ZONE
from sqlalchemy.ext.declarative import declarative_base # para crear BaseClass y poder mapear tablas

BaseClass = declarative_base()

# ---> Este archivo modelos.py sirve para mapear clases 

# Clases de tipo BaseClass por cada tipo de tabla que hay en la BD (alumnos, calificaciones, fotos)
# __tablename__= Nombre_tabla_BD
# --> column(tipo de dato de sqlalchemy)       tambien puede tener argumentos extras

# -----argumentos extras-----
# primary_key=True          indica que el id es una llave primaria
# ForeignKey(arg1, arg2)    indica que es una llave foranea donde tiene 2 parametros. La tabla que se referencia y que campo de esa tabla es la llave
# "email"                   indica que es formato email. Por ejemplo, si no se pone un @, no se inserta
# timezone= True            indica que se inserte con la zona horaria
# default=                  indica que por "default" se obtiene la fecha y hora del dispositivo con datetime.datetime.now




# Tabla alumnos
class Alumno(BaseClass):
    __tablename__= "alumnos"
    id= Column(Integer, primary_key= True)
    nombre= Column(String(100))
    edad= Column(Integer)
    domicilio= Column(String(100))
    carrera= Column(String(100))
    trimestre= Column(String(100))
    email= Column("email",String(100)) 
    password= Column(String(100))
    fecha_registro= Column(DateTime(timezone=True), default= datetime.datetime.now)   




# Tabla calificaciones
class Calificacion(BaseClass):
    __tablename__= "calificaciones" 
    id= Column(Integer, primary_key= True)
    id_alumno= Column(Integer, ForeignKey(Alumno.id)) # indica que es llave foranea de la tabla Alumno y es el id
    uea= Column(String(100))
    calificacion= Column(String(100))




# Tabla fotos
class Foto(BaseClass):
    __tablename__= "fotos"
    id= Column(Integer, primary_key=True)
    id_alumno= Column(Integer, ForeignKey(Alumno.id)) # indica que es llave foranea de la tabla Alumno y es el id
    titulo= Column(String(100))
    descripcion= Column(String(100))
    ruta= Column(String(100)) 

