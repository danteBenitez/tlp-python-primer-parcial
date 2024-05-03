import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ejercicio_pandas import SUBJECTS, GRADES
from ejercicio_pandas.grades_analysis import get_student_avg_grade

grade_frame = pd.DataFrame(GRADES)
student_avg = get_student_avg_grade(grade_frame, subjects=SUBJECTS)

print(student_avg)
plt.bar(student_avg["nombre"], student_avg["promedio"])

plt.title("Promedio de calificaciones por estudiante")

plt.xlabel("Estudiantes")
plt.ylabel("Promedio de calificaciones")
plt.legend()

plt.show()