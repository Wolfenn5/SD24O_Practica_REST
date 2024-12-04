# Atender peticiones:

## get("/alumnos”)
## get("/alumnos/{id})
## get("/alumnos/{id}/calificaciones")
## get("/alumnos/{id}/fotos")
## get("/fotos/{id}”)
## get("/calificaciones/{id}”)
# delete("/fotos/{id}”)
# delete("/calificaciones/{id}”)
## delete("/alumnos/{id}/calificaciones")
## delete("/alumnos/{id}/fotos")
"""# delete("/alumnos/{id})"""
from fastapi import FastAPI, UploadFile, File, Form, Depends # para manejo de archivos, formularios html y sesiones
from typing import Optional # para hacer que los argumentos señalados sean opcionales

from ORM.config import generador_sesion # generador de sesiones 
import ORM.repo as repo # funciones para hacer consultas a la BD del archivo repo.py
from sqlalchemy.orm import Session # para gestionar sesiones al hacer querys


# conda create --name prest               --> Para crear ambiente
# conda activate prest                    --> Para activar ambiente
# python -m uvicorn api:app --reload      --> Para levantar el servidor




# creación del servidor
app = FastAPI()


# decorador (actua como un home en el servidor)
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "Practica Rest SD24O"
    }

    return respuesta




# En las funciones, primero van los parametros obligatorios y luego los opcionales 
# Primero lo que el usuario proporciona y luego se pide el favor (una query) a repo.py (sesion)

#########################

# Alumnos

#########################

# Peticion get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("Api consultando lista de alumnos")
    return repo.devuelve_alumnos(sesion)


# Peticion get("/alumnos/{id})
@app.get("/alumnos/{id_alumno}")
def lista_alumnos_por_id(id_alumno:int, sesion:Session=Depends(generador_sesion)):
    print ("Api consultando el alumno: ", id_alumno)
    return repo.devuelve_alumnos_por_id(sesion,id_alumno)


# Peticion get("/alumnos/{id}/calificaciones")
@app.get("/alumnos/{id_alumno}/calificaciones")
def calificaciones_alumno_por_id(id_alumno:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando las calificaciones del alumno: ",id_alumno)
    return repo.devuelve_calificaciones_de_alumno_por_id(sesion, id_alumno)


# Peticion get("/alumnos/{id}/fotos")
@app.get("/alumnos/{id_alumno}/fotos")
def fotos_alumno_por_id(id_alumno:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando fotos del alumno: ",id_alumno)
    return repo.devuelve_fotos_de_alumno_por_id(sesion, id_alumno)



"""  Peticion aun por IMPLEMENTAR ya que requiere borrar calificaciones y fotos del alumno

# Peticion delete("/alumnos/{id})  
@app.delete("/alumnos/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    # Antes de borrar al alumno, primero hay que borrar las calificaciones y fotos que esten asociados a ese alumno
    repo.devuelve_borrar_calificaciones_de_alumno_por_id(sesion,id)
    repo.devuelve_borrar_fotos_de_alumno_por_id(sesion,id)
    # Y ahora si se puede borrar el usuario
    repo.borrar_alumno_por_id(sesion,id)
    return {"Api borrando alumno: ", "ok"}
"""


# Peticion delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_de_alumno_por_id(id_alumno:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando fotos del alumno:", id_alumno)
    return repo.devuelve_borrar_fotos_de_alumno_por_id(sesion, id_alumno)


# Peticion delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_de_alumno_por_id(id_alumno:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando calificaciones del alumno: ",id_alumno)
    return repo.devuelve_borrar_calificaciones_de_alumno_por_id(sesion,id_alumno)



#########################

# Calificaciones

#########################

# Peticion get("/calificaciones/{id}”)
@app.get("/calificaciones/{id_calificacion}")
def lista_calificaciones_por_id(id_calificacion:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando la calificacion con id: ", id_calificacion)
    return repo.devuelve_calificaciones_por_id(sesion, id_calificacion)


# Peticion get ("/calificaciones")
@app.get("/calificaciones")
def lista_calificaciones(sesion:Session=Depends(generador_sesion)):
    print("Api consultando lista de calificaciones")
    return repo.devuelve_calificaciones(sesion)


# Peticion delete("/calificaciones/{id}”)
@app.delete("/calificaciones/{id}")
def borrar_calificaciones_por_id(id_cal:int, sesion:Session=Depends(generador_sesion)):
    print("Api borrando la calificacion con id:",id_cal)
    return repo.devuelve_borrar_calificaciones_por_id(sesion, id_cal)



#########################

# Fotos

#########################

# Peticion get("/fotos/{id}")
@app.get("/fotos/{id_foto}")
def lista_fotos_por_id(id_foto:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando la foto con id:", id_foto)
    return repo.devuelve_fotos_por_id(sesion, id_foto)


# Peticion get("/fotos")
# Se hizo esta peticion para poder hacer la consulta SELECT * FROM app.fotos de repo.py
@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generador_sesion)):
    print("Api consultando lista de fotos")
    return repo.devuelve_fotos(sesion)