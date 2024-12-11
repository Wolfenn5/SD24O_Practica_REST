import ORM.modelos as modelos # para traer las tablas que se mapearon de modelos.py
from sqlalchemy.orm import Session # para gestionar sesiones al hacer querys
import ORM.esquemas as esquemas


# ---> Este archivo repo.py implementa las siguientes consultas SQL SELECT y DELETE

# SELECT * FROM app.alumnos
# SELECT * FROM app.alumnos WHERE id={id_al}
# SELECT * FROM app.fotos
# SELECT * FROM app.fotos WHERE id={id_fo}
# SELECT * FROM app.fotos WHERE id_alumno={id_al}
# SELECT * FROM app.calificaciones
# SELECT * FROM app.calificaciones WHERE id={id_cal}
# SELECT * FROM app.calificaciones WHERE id_alumno={id_al}
# DELETE FROM app.alumnos WHERE id_alumno={id_al}
# DELETE FROM app.calificaciones WHERE id_alumno={id_al}
# DELETE FROM app.fotos WHERE id_alumno={id_al}

# Las funciones implementadas son llamadas por api.py
# Primero va el argumento sesion y luego los de consulta por ejemplo, el id
# Primero se recibe el favor (una query) y luego lo que pide (id u otra cosa)

# -----Tipos de filtro-----
# .first()    muestra el primer elemento de la query que se hace
# .all()      muestra todos los elementos de la query que se hace
# .filer()    muestra los elementos de acuerdo a un criterio dado. Por ejemplo WHERE 


# -----------Tablas mapeadas-----------
# Tabla alumnos           modelos.Alumno
# Tabla calificaciones    modelos.Calificacion
# Tabla fotos             modelos.Foto



#########################

# Alumnos

#########################

#---------------Consultas SELECT---------------#

# Funcion para devolver la lista de todos los alumnos
# SELECT * FROM app.alumnos
def devuelve_alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()


# Funcion para devolver un alumno dado un id 
# SELECT * FROM app.alumnos WHERE id={id_al}
def devuelve_alumnos_por_id(sesion:Session,id_alumno:int):
    print("SELECT * FROM app.alumnos WHERE id=", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()



#---------------Consultas DELETE---------------#

# Funcion para borrar un alumno dado un id
def devuelve_borrar_alumnos_por_id(sesion:Session, id_al:int):
    # 1.- Primero se verifica que el alumno existe
    print("Consultando si el alumno", id_al, "existe")
    alumno= devuelve_alumnos_por_id(sesion, id_al)
    # 2.- Si existe entonces se borra
    if alumno is not None:
        print("El alumno: ", id_al, "existe")
        print("DELETE FROM app.alumnos WHERE id_alumno= ", id_al)
        sesion.delete(alumno)
    # 3.- Se confirman los cambios
        sesion.commit()
    respuesta= {
        "mensaje": "alumno borrado"
    }
    return respuesta


#---------------Consultas INSERT---------------#

# Funcion para devolver un alumno nuevo 
# INSERT INTO app.alumnos
def devuelve_alumno_nuevo(sesion:Session, alumno_nuevo:esquemas.AlumnoBase): # alumno_nuevo es lo que se recibe del usuario
    # 1.- Crear un nuevo objeto de la clase modelo Alumno
    alumno_bd = modelos.Alumno()
    # 2.- Llenar el nuevo objeto con los parametros que pasa el usuario
    alumno_bd.nombre = alumno_nuevo.nombre   
    alumno_bd.edad = alumno_nuevo.edad
    alumno_bd.domicilio = alumno_nuevo.domicilio
    alumno_bd.carrera = alumno_nuevo.carrera
    alumno_bd.trimestre = alumno_nuevo.trimestre
    alumno_bd.email = alumno_nuevo.email
    alumno_bd.password = alumno_nuevo.password
    # 3.- Insertar el nuevo objeto a la BD
    sesion.add(alumno_bd)
    # 4.- Confirmar los cambios
    sesion.commit()
    # 5.- Refrescar/actualizar los cambios
    sesion.refresh(alumno_bd)
    return alumno_bd


# Funcion para devolver una calificacion nueva a un alumno dado un id
# INSERT INTO app.calificaciones WHERE id_alumno={id_al}
def devuelve_calificacion_nueva(sesion:Session, id_alumno:int, calificacion_nueva:esquemas.CalificacionBase):
    # 1.- Verificar que el alumno exista
    calificacion_bd = devuelve_alumnos_por_id(sesion, id_alumno)
    # 2.- Si existe, crear un nuevo objeto de la clase modelo Calificacion
    if calificacion_bd is not None: 
        calificacion_bd = modelos.Calificacion()
    # 3.- Llenar el nuevo objeto con los parametros que pasa el usuario
        calificacion_bd.uea = calificacion_nueva.uea
        calificacion_bd.calificacion = calificacion_nueva.calificacion
        # Como el usuario no puede modificar tal cual el id_alumno, se utiliza el que se recibe del usuario sin que el lo haga manualmente
        calificacion_bd.id_alumno = id_alumno
    # 4.- Insertar el nuevo objeto a la BD
        sesion.add(calificacion_bd)
    # 5.- Confirmar los cambios
        sesion.commit()
    # 6.- Refrescar/actualizar los cambios
        sesion.refresh(calificacion_bd)
        return calificacion_bd
    else:
        respuesta = {"mensaje" : "No existe el alumno"}
        return respuesta


# Funcion para devolver una foto nueva a un alumno dado un id
# INSERT INTO app.foto WHERE id_alumno={id_al}
def devuelve_foto_nueva(sesion:Session, id_alumno:int, foto_nueva:esquemas.FotoBase):
    # 1.- Verificar que el alumno exista
    foto_bd = devuelve_alumnos_por_id(sesion, id_alumno)
    # 2.- Si existe, crear un nuevo objeto de la clase modelo Foto
    if foto_bd is not None: 
        foto_bd = modelos.Foto()
    # 3.- Llenar el nuevo objeto con los parametros que pasa el usuario
        foto_bd.titulo = foto_nueva.titulo
        foto_bd.descripcion = foto_nueva.descripcion
        # Como el usuario no puede modificar tal cual el id_alumno, se utiliza el que se recibe del usuario sin que el lo haga manualmente
        foto_bd.id_alumno = id_alumno
    # 4.- Insertar el nuevo objeto a la BD
        sesion.add(foto_bd)
    # 5.- Confirmar los cambios
        sesion.commit()
    # 6.- Refrescar/actualizar los cambios
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"mensaje" : "No existe el alumno"}
        return respuesta


#---------------Consultas UPDATE---------------#

# Funcion para devolver datos actualizados de un alumno dado un id
# UPDATE app.foto WHERE id_alumno={id_al}
def devuelve_actualizar_datos_alumno(sesion:Session, id_alumno:int, alumno_esquema:esquemas.AlumnoBase):
    # 1.- Primero se verifica que el alumno exista
    alumno_bd = devuelve_alumnos_por_id(sesion, id_alumno) # objeto de la clase de la BD
    # 2.- Si existe, entonces se actualizan los datos
    if alumno_bd is not None:
        alumno_bd.nombre = alumno_esquema.nombre   
        alumno_bd.edad = alumno_esquema.edad
        alumno_bd.domicilio = alumno_esquema.domicilio
        alumno_bd.carrera = alumno_esquema.carrera
        alumno_bd.trimestre = alumno_esquema.trimestre
        alumno_bd.email = alumno_esquema.email
        alumno_bd.password = alumno_esquema.password
    # 3.- Confirmar los cambios
        sesion.commit()
    # 4.- Refrescar/actualizar los cambios
        sesion.refresh(alumno_bd)
    # 5.- Imprimir los datos nuevos
        print(alumno_esquema)
        return (alumno_esquema)
    else:
        respuesta = {"mensaje" : "No existe el alumno"}
        return respuesta
    

#########################

# Calificaciones

#########################

#---------------Consultas SELECT---------------#

# Funcion para devolver las calificaciones de un alumno dado un id 
# SELECT * FROM app.calificaciones WHERE id_alumno={id_al}
def devuelve_calificaciones_de_alumno_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumno=", id_al)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_al).all()

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



#---------------Consultas DELETE---------------#

# Funcion para borrar las calificaciones de un alumno dado un id
# DELETE FROM app.calificaciones WHERE id_alumno={id_al}
def devuelve_borrar_calificaciones_de_alumno_por_id(sesion:Session, id_alumno:int):
    # 1.- Antes de borrar primero se va a verificar que el alumno tiene calificaciones y ademas existe con un SELECT
    print("Consultando si el alumno:", id_alumno, "existe y tiene calificaciones")
    calificaciones_de_alumno= devuelve_calificaciones_de_alumno_por_id(sesion, id_alumno) # se pasa sesion y no sesion:Session para no crear una doble sesion
    # 2.- Si existe entonces se borran las calificaciones del alumno
    if calificaciones_de_alumno is not None:
        print("El alumno:", id_alumno, "existe")
        print("DELETE FROM app.calificaciones WHERE id_alumno= ", id_alumno)
        # Por si hay un alumno que tenga varias calificaciones (como el alumno 1 que tiene 2 fotos). Se elimina cada calificacion
        for calificacion in calificaciones_de_alumno:
            sesion.delete(calificacion)
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


#---------------Consultas UPDATE---------------#

# Funcion para devolver datos actualizados de una calificacion dado un id
# UPDATE app.calificaciones WHERE id_calificacion={id_cal}
def devuelve_actualizar_datos_calificacion(sesion:Session, id_calificacion:int, calificacion_esquema:esquemas.CalificacionBase):
    # 1.- Primero se verifica que la calificacion exista
    calificacion_bd = devuelve_calificaciones_por_id(sesion, id_calificacion) # objeto de la clase de la BD
    # 2.- Si existe, entonces se actualizan los datos
    if calificacion_bd is not None:
        calificacion_bd.uea = calificacion_esquema.uea
        calificacion_bd.calificacion = calificacion_esquema.calificacion
    # 3.- Confirmar los cambios
        sesion.commit()
    # 4.- Refrescar/actualizar los cambios
        sesion.refresh(calificacion_bd)
    # 5.- Imprimir los datos nuevos
        print(calificacion_esquema)
        return (calificacion_esquema)
    else:
        respuesta = {"mensaje" : "No existe la calificacion"}
        return respuesta
    

#########################

# Fotos

#########################

#---------------Consultas SELECT---------------#

# Funcion para devolver las fotos de un alumno dado un id 
# SELECT * FROM app.fotos WHERE id_alumno={id_al}
def devuelve_fotos_de_alumno_por_id(sesion:Session, id_al:int):
    print("SELECT * FROM app.fotos WHERE id_alumno=", id_al)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_al).all()


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



#---------------Consultas DELETE---------------#

# Funcion para borrar las fotos de un alumno dado un id
# DELETE FROM app.fotos WHERE id_alumno={id_al}
def devuelve_borrar_fotos_de_alumno_por_id(sesion:Session, id_alumno:int):
    print("Consultando si el alumno:", id_alumno, "existe y tiene calificaciones")
    # 1.- Antes de borrar primero se va a verificar que el alumno tiene fotos y ademas existe con un SELECT
    fotos_de_alumno= devuelve_fotos_de_alumno_por_id(sesion,id_alumno) # la sesion se pasa como un argumento y no como sesion:Session, porque se crearia una doble sesion
    # 2.- Si existe, entonces se borran las fotos del alumno
    if fotos_de_alumno is not None:
        print("El alumno:", id_alumno,"existe")
        print("DELETE FROM app.fotos WHERE id_alumno= ", id_alumno)
        # Por si hay un alumno que tenga varias fotos (como el alumno 2 que tiene 2 fotos). Se elimina cada foto
        for foto in fotos_de_alumno:
            sesion.delete(foto)
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