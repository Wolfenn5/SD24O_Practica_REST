# Atender peticiones:

# get("/alumnos”)
# get("/alumnos/{id})
# get("/alumnos/{id}/calificaciones")
# get("/alumnos/{id}/fotos")
# get("/fotos/{id}”)
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


#########################

# Alumnos

#########################

# Peticion get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("SELECT * FROM app.alumnos")
    return repo.devuelve_alumnos(sesion)





#########################

# Calificaciones

#########################






#########################

# Fotos

#########################