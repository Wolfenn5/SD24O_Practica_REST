# Implementar consultas sql SELECT y DELETE

## SELECT * FROM app.alumnos
## SELECT * FROM app.alumnos WHERE id={id_al}
## SELECT * FROM app.fotos
## SELECT * FROM app.fotos WHERE id={id_fo}
## SELECT * FROM app.fotos WHERE id_alumno={id_al}
## SELECT * FROM app.calificaciones
## SELECT * FROM app.calificaciones WHERE id={id_cal}
## SELECT * FROM app.calificaciones WHERE id_alumno={id_al}
# DELETE FROM app.alumnos WHERE id_alumno={id_al}
## DELETE FROM app.calificaciones WHERE id_alumno={id_al}
## DELETE FROM app.fotos WHERE id_alumno={id_al}
import ORM.modelos as modelos # para traer las tablas que se mapearon de modelos.py
from sqlalchemy.orm import Session # para gestionar sesiones al hacer querys

# Las funciones son llamadas por api.py

# .first()    muestra el primer elemento de la query que se hace
# .all()      muestra todos los elementos de la query que se hace
# .filer()    muestra los elementos de acuerdo a un criterio dado. Por ejemplo WHERE 


# -----------Tablas mapeadas-----------
# Tabla alumnos           modelos.Alumno
# Tabla calificaciones    modelos.Calificacion
# Tabla fotos             modelos.Foto



# En las funciones, primero va el argumento sesion y luego los de consulta por ejemplo, el id
# Primero se recibe el favor (una query) y luego lo que pide (id u otra cosa)

#########################

# Alumnos

#########################

# Funcion para devolver la lista de todos los alumnos
# SELECT * FROM app.alumnos
def devuelve_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()


# Funcion para devolver un alumno dado un id 
# SELECT * FROM app.alumnos WHERE id={id_al}
def devuelve_alumnos_por_id(sesion:Session,id_alumno:int):
    print("SELECT * FROM app.alumnos WHERE id=", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).all()




#########################

# Calificaciones

#########################

# Funcion para devolver las calificaciones de un alumno dado un id 
# SELECT * FROM app.calificaciones WHERE id_alumno={id_al}
def devuelve_calificaciones_de_alumno_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumno=", id_al)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_al).first()

# Funcion para devolver una calificacion dado un id 
# SELECT * FROM app.calificaciones WHERE id={id_cal}
def devuelve_calificaciones_por_id(sesion:Session, id_cal:int):
    print("SELECT * FROM app.calificaciones WHERE id=", id_cal)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_cal).first()

# Funcion para devolver la lista de todas las calificaciones
# SELECT * FROM app.calificaciones
def devuelve_calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()


# Funcion para borrar las calificaciones de un alumno dado un id
# DELETE FROM app.calificaciones WHERE id_alumno={id_al}
def devuelve_borrar_calificaciones_de_alumno_por_id(sesion:Session, id_alumno:int):
    # 1.- Antes de borrar primero se va a verificar que el alumno tiene calificaciones y ademas existe con un SELECT
    print("Consultando si el alumno:", id_alumno, "existe")
    calificaciones_alumno= devuelve_calificaciones_de_alumno_por_id(sesion, id_alumno) # se pasa sesion y no sesion:Session para no crear una doble sesion
    # 2.- Si existe entonces se borra
    if calificaciones_alumno is not None:
        print("El alumno:", id_alumno, "existe")
        print("DELETE FROM app.calificaciones WHERE id_alumno= ", id_alumno)
        sesion.delete(calificaciones_alumno)
    # 3.- Se confirman los cambios
        sesion.commit() # Se hacen todos los cambios a la vez (se borran todos a la vez y no uno por uno)
    respuesta= {
        "mensaje": "calificaciones del alumno borradas"
    }
    return respuesta


# Funcion para borrar calificaciones dado un id
# DELETE FROM app.calificaciones WHERE id={id_cal}
def devuelve_borrar_calificaciones_por_id(sesion:Session, id_cal):
    # 1.- Primero se verifica si la calificacion con el id existe
    print("Consultando si la calificacion:",id_cal, "existe")
    calificacion= devuelve_calificaciones_por_id(sesion, id_cal)
    # 2.- Si existe entonces se borra
    if calificacion is not None:
        print("La calificacion:", id_cal, "existe")
        print("DELETE FROM app.calificaciones WHERE id= ", id_cal)
        sesion.delete(calificacion)
    # 3.- Se confirman los cambios
        sesion.commit()
    respuesta= {
        "mensaje": "calificacion borrada"
    }
    return respuesta


#########################

# Fotos

#########################

# Funcion para devolver las fotos de un alumno dado un id 
# SELECT * FROM app.fotos WHERE id_alumno={id_al}
def devuelve_fotos_de_alumno_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.fotos WHERE id_alumno=", id_al)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_al).first()


# Funcion para devolver una foto dado un id
# SELECT * FROM app.fotos WHERE id={id_fo}
def devuelve_fotos_por_id(sesion:Session, id_fot:int):
    print("SELECT * FROM app.fotos WHERE id=", id_fot)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_fot).first()


# Funcion para devolver lista de todas las fotos
# SELECT * FROM app.fotos
def devuelve_fotos(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()


# Funcion para borrar las fotos de un alumno dado un id
# DELETE FROM app.fotos WHERE id_alumno={id_al}
def devuelve_borrar_fotos_de_alumno_por_id(sesion:Session, id_alumno:int):
    print("Consultando si el alumno:", id_alumno, "existe")
    # 1.- Antes de borrar primero se va a verificar que el alumno tiene fotos y ademas existe con un SELECT
    fotos_de_alumno= devuelve_fotos_de_alumno_por_id(sesion,id_alumno) # la sesion se pasa como un argumento y no como sesion:Session, porque se crearia una doble sesion
    # 2.- Si existe, entonces se borra el alumno
    if fotos_de_alumno is not None:
        print("El alumno:", id_alumno,"existe")
        print("DELETE FROM app.fotos WHERE id_alumno= ", id_alumno)
        sesion.delete(fotos_de_alumno)
    # 3.- Se confirma que se hizo el cambio
        sesion.commit() # Se hacen todos los cambios a la vez (si llegasen a existir varios alumnos con un mismo id, se borran todos a la vez y no uno por uno)
    respuesta = {
        "mensaje": "fotos del alumno borradas"
    }
    return respuesta


# Funcion para borrar fotos dado un id
# DELETE FROM app.fotos WHERE id={id_fo}
def devuelve_borrar_fotos_por_id(sesion:Session, id_fo):
    # 1.- Primero se verifica que la foto existe
    print("Consultando si la foto", id_fo, "existe")
    foto= devuelve_fotos_por_id(sesion, id_fo)
    # 2.- Si existe entonces se borra
    if foto is not None:
        print("La foto: ", id_fo, "existe")
        print("DELETE FROM app.fotos WHERE id= ", id_fo)
        sesion.delete(foto)
    # 3.- Se confirman los cambios
        sesion.commit()
    respuesta= {
        "mensaje": "foto borrada"
    }
    return respuesta