# Configurar conexion a BD
from sqlalchemy import create_engine # para crear el engine (conexion a BD)
from sqlalchemy.orm import sessionmaker # para crear sesiones cuando se hagan consultas
from sqlalchemy.ext.declarative import declarative_base # para crear BaseClass y poder mapear tablas

# 1.- Configuracion de BD
# --> nombre_servidor://usuario:contraseña_del_usuario@URL_SERVIDOR:puerto/nombreBD
URL_BASE_DATOS = "postgresql://usuario-ejemplo:prest@localhost:5432/alumnos"


# 2.- conectarse con create_engine al esquema "app" (=app)
engine= create_engine(URL_BASE_DATOS,
                      connect_args={
                          "options":"-csearch_path= app"  # -csearch_path= Nombre del Esquema
                      })


# 3.- Clase que permite crear objetos tipo session para las query
SessionClass= sessionmaker(engine)


# 4.- Funcion para objetos clase tipo SessionClass
def generador_sesion(): # generar sesiones al hacer querys
    sesion= SessionClass()
    try:
        yield sesion # es como un "return sesion" 
    finally:
        sesion.close() # cerrar sesion al terminar query


# 5.- Clase base para mapear tablas
BaseClass = declarative_base()

