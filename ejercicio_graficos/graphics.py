import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from ejercicio_pandas import main as get_student_avg

student_avg = get_student_avg()

print(student_avg)
plt.bar(student_avg["nombre"], student_avg["promedio"])

plt.title("Promedio de calificaciones por estudiante")

plt.xlabel("Estudiantes")
plt.ylabel("Promedio de calificaciones")
plt.show()