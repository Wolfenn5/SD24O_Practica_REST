# Atender peticiones:

## get("/alumnos”)
## get("/alumnos/{id})
## get("/alumnos/{id}/calificaciones")
## get("/alumnos/{id}/fotos")
## get("/fotos/{id}”)
# get("/calificaciones/{id}”)
# delete("/fotos/{id}”)
# delete("/calificaciones/{id}”)
# delete("/alumnos/{id}/calificaciones")
# delete("/alumnos/{id}/fotos")
# delete("/alumnos/{id})
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




#########################

# Calificaciones

#########################






#########################

# Fotos

#########################

# Peticion get("/fotos/{id}")
@app.get("/fotos/{id_foto}")
def lista_fotos_por_id(id_foto:int, sesion:Session=Depends(generador_sesion)):
    print("Api consultando lista de fotos")
    return repo.devuelve_fotos_por_id(sesion, id_foto)