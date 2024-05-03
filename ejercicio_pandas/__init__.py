import pandas as pd
from ejercicio_pandas.utils import average_of
from ejercicio_pandas.format import separate
from ejercicio_pandas.grades_analysis import top_students_for, calculate_passed_percentage, get_student_avg_grade

GRADES = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90,
     "historia": 75},
    {"nombre": "María", "matematicas": 70, "ciencias": 80,
     "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75,
     "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia":
     80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70,
     "historia": 95},
    {"nombre": "Sofía", "matematicas": 90, "ciencias": 85,
     "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90,
     "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75,
     "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85,
     "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70,
     "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85,
     "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90,
     "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75,
     "historia": 85}
]

SUBJECTS = ["matematicas", "ciencias", "historia"]


def main():
    """
        Realiza un análisis estadístico de las calificaciones de los estudiantes.
    """
    if not isinstance(GRADES, list):
        raise ValueError("Las calificaciones deben estar dispuestas en una lista.")

    for grade in GRADES:
        if not isinstance(grade, dict):
            raise ValueError("Las calificaciones deben ser diccionarios")
        elif "nombre" not in grade:
            raise ValueError("Las calificaciones deben contar con el nombre del alumno")

    # Creamos un DataFrame para trabajar con los datos más cómodamente
    grades_frame = pd.DataFrame(GRADES)

    # Calculamos y mostramos el promedio de cada asignatura
    average = average_of(grades_frame, columns=SUBJECTS)

    separate()
    print(f"El promedio por materia es el siguiente: ")
    print(average)
    separate()

    # Mostramos los mejores alumnos en cada asignatura
    for subject in SUBJECTS:
        print(f"Mejores alumnos para {subject}")
        print(top_students_for(grades_frame, subject=subject))
        separate()

    passed = calculate_passed_percentage(grades_frame, subjects=SUBJECTS)
    print(f"El porcentaje de aprobación es el siguiente: ")
    print(passed)
    separate()

    student_average = get_student_avg_grade(grades_frame, subjects=SUBJECTS)

    return student_average


if __name__ == "__main__":
    main()
