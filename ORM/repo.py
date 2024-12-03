# Implementar consultas sql SELECT y DELETE

## SELECT * FROM app.alumnos
## SELECT * FROM app.alumnos WHERE id={id_al}
# SELECT * FROM app.fotos
# SELECT * FROM app.fotos WHERE id={id_fo}
# SELECT * FROM app.fotos WHERE id_alumno={id_al}
# SELECT * FROM app.calificaciones
# SELECT * FROM app.calificaciones WHERE id={id_fo}
# SELECT * FROM app.calificaciones WHERE id_alumno={id_al}
# DELETE FROM app.alumnos WHERE id_alumno={id_al}
# DELETE FROM app.calificaciones WHERE id_alumno={id_al}
# DELETE FROM app.fotos WHERE id_alumno={id_al}
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
    print("SELECT * FROM app.alumnos WHERE id={id_al}")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()









#########################

# Calificaciones

#########################






#########################

# Fotos

#########################