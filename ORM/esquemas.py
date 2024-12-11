from pydantic import BaseModel
# ---> Este archivo esquemas.py sirve para asociar las tablas de la BD, donde se recibe lo que el cliente mande


# No se inlcuye la ruta, el id ni la fecha de registro porque no se quiere que el usuario pueda modificarlos

# Definir el esquema usuario
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str


# Definir el esquema Calificacion
class CalificacionBase(BaseModel):
    uea:str
    calificacion:str

# Definir el esquema fotos
class FotoBase(BaseModel):
    titulo:str
    descripcion:str
