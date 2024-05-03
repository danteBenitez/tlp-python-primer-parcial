import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ejercicio_pandas import SUBJECTS, GRADES
from ejercicio_pandas.grades_analysis import get_student_avg_grade

# Construimos el DataFrame de las calificaciones
grade_frame = pd.DataFrame(GRADES)
# Obtenemos el promedio por estudiante con una función 
# ya implementada
student_avg = get_student_avg_grade(grade_frame, subjects=SUBJECTS)

# Mostramos los promedios por consola
print(student_avg)

# Creamos un gráfico de barra para el nombre y el promedio
plt.bar(student_avg["nombre"], student_avg["promedio"])

# Colocamos un título y etiquetas de ejes
plt.title("Promedio de calificaciones por estudiante")
plt.xlabel("Estudiantes")
plt.ylabel("Promedio de calificaciones")

# Mostramos el gráfico
plt.show()