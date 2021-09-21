import numpy as np

#открываем файл с таблицей
test=np.genfromtxt('C:/Users/Olga/rand_number1.csv', delimiter=';')

print(test)

#создаем единичную матрицу с помощью функции eye()
#задаем ей размерность = размерности матрицы из файла
m_eye=np.eye(*test.shape)
print(m_eye)

#перемножаем две матрицы
new_test=test.dot(m_eye)
print(new_test)

#сохранение полученных данных в новый файл
np.savetxt('new_rand_number1.csv', new_test, delimiter=",")