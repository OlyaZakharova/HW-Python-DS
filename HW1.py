import numpy as np
import pandas as pd

#открываем файл с таблицей
test=pd.read_csv('HW1.csv', delimiter=';')

test

#создаем единичную матрицу с помощью функции eye()
#задаем ей размерность = размерности матрицы из файла
m_eye=np.eye(*test.shape)
m_eye

#перемножаем две матрицы
new_test=test.dot(m_eye)
print(new_test)

#сохранение полученных данных в новый файл
np.savetxt('new_HW1.csv', new_test, delimiter=",")
