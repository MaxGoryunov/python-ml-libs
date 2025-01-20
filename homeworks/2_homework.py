import numpy as np


# 1. Что надо изменить в последнем примере, чтобы он заработал без ошибок 
# (транслирование)?
"""
Необходимо изменить размерность второго массива. Это можно сделать либо
с помощью newaxis, либо при помощи reshape
"""
# a = np.ones((3, 2))
# b = np.arange(3)

a = np.ones((3, 2))
print(f'a = {a}')
b = np.arange(3)
print(f'b = {b}')

b1 = b[:, np.newaxis]
print(f'b1 = {b1}')
print(f'a + b1 = {a + b1}')

b2 = np.reshape(b, (3, 1))
print(f'b2 = {b2}')
print(f'a + b2 = {a + b2}')

#      a: (3, 2) -> (3, 2)
# b1, b2: (3, 1) -> (3, 2)
