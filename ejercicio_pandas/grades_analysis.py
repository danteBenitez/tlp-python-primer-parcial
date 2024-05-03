import pandas as pd

def calculate_passed_percentage(grades: pd.DataFrame, *, subjects: list[str]) -> pd.DataFrame:
    """
        Calcula qué porcentaje de las notas en `grades` son mayores o iguales a 60
        para cada una de las materias en `subjects`

        :param grades Las calificaciones
        :type pd.DataFrame

        :param subjects Las materias correspondientes
        :type list[str]

        :returns Un DataFrame donde las materias están en una columna
                 y el porcentaje en otra.
        :rtype pd.DataFrame
    """
    # Creamos un nuevo DataFrame para utilizar
    passed_data_frame = pd.DataFrame()

    # En `materias` ponemos los nombres de las columnas de `grades`
    passed_data_frame["materias"] = grades[subjects].columns

    # Filtramos las notas que son mayores o iguales a 60
    # y las contamos
    passed_data_frame["aprobacion"] = grades[subjects][grades[subjects] >= 60].index.size

    # El total de alumnos
    total_students = grades.index.size

    # Convertimos la aprobación a porcentaje
    passed_data_frame["aprobacion"] = passed_data_frame["aprobacion"] * 100 / total_students

    return passed_data_frame



def top_students_for(grades: pd.DataFrame, *, subject: str) -> pd.DataFrame:
    """
        Retorna un DataFrame con el mejor estudiante en `grades` para 
        la materia `subject`. 

        :param grades
        :type pd.DataFrame

        :param subject
        :type str
    """
    # Obtenemos la nota máxima para subject
    top_student_grade = grades[subject].max()

    # Filtramos las notas para sólo incluir los estudiantes
    # con la nota máxima para esa materia.
    top_students = grades[grades[subject] == top_student_grade]

    # Incluimos sólo las columnas "nombre" y la materia.
    top_students = top_students[["nombre", subject]]

    return top_students

def get_student_avg_grade(grades: pd.DataFrame, *, subjects: list[str]) -> pd.DataFrame:
    """
        Toma una planilla de calificaciones y retorna un DataFrame con dos columnas.
        
        :param grades Las calificaciones de cada estudiante
        :type pd.DataFrame

        :returns Un DataFrame cuyas columnas son: El nombre del estudiante,
                 y el promedio de su calificación en las materias
        :rtype pd.DataFrame
    """
    # Creamos un nuevo DataFrame
    student_avg = pd.DataFrame()

    # Obtenemos los nombres de alumnos
    student_avg["nombre"] = grades["nombre"]

    # Calculamos el promedio con .mean()
    # Pero esta vez usamos el eje de las columnas
    # Esto hará que por cada alumno calculemos el promedio de calificaciones
    student_avg["promedio"] = grades[subjects].mean(axis=1)

    return student_avg