from sqlalchemy import create_engine # para crear el engine (conexion a BD)
from sqlalchemy.orm import sessionmaker # para crear sesiones cuando se hagan consultas

# Importar de modelos.py las tablas si se quiere desplegar en render
from ORM import modelos
import os 

# ---> Este archivo config.py sirve para configurar la conexion a BD

##### Para conectarse de forma local (misma PC) #####

# # 1.- Configuracion de BD
# # --> nombre_servidor://usuario:contraseña_del_usuario@URL_SERVIDOR:puerto/nombreBD
# URL_BASE_DATOS = "postgresql://usuario-ejemplo:prest@localhost:5432/alumnos"

# # 2.- conectarse con create_engine al esquema "app" (=app)
# engine= create_engine(URL_BASE_DATOS,
#                       connect_args={
#                           "options":"-csearch_path=app"  # -csearch_path=Nombre del Esquema
#                       })



##### Para desplegar en render #####
# 2.- conectarse con create_engine al ambiente del servidor
engine= create_engine(os.getenv("db_uri", "sqlite://base-ejemplo.db"))  # la primera variable almacena el id de datos y la segunda sera el nombre de la BD
# uri es un identificador muy general como /usuarios 
modelos.BaseClass.metadata.create_all(engine) # con todas las "hijas" (tabla alumno, calificacion, foto) de la BaseClass crear la BD



# 3.- Clase que permite crear objetos tipo session para las query
SessionClass= sessionmaker(engine)


# 4.- Funcion para objetos clase tipo SessionClass
def generador_sesion(): # generar sesiones al hacer querys
    sesion= SessionClass()
    try:
        yield sesion # es como un "return sesion" 
    finally:
        sesion.close() # cerrar sesion al terminar query



##### Para conectarse de forma local (misma PC) #####
# # 5.- Clase base para mapear tablas
# BaseClass = declarative_base()

