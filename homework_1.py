import array
import numpy as np


## 1. Какие еще существуют коды типов?
print(list(array.typecodes))
print('b - знаковый char')
print('B - беззнаковый char')
print('u - символ unicode')
print('h - знаковый short')
print('H - беззнаковый short')
print('i - знаковый int')
print('I - беззнаковый int')
print('l - знаковый long')
print('L - беззнаковый long')
print('f - float')
print('d - double')


## 2. Напишите код, подобный приведенному выше, но с другим типом
print('Примеры:')
b = array.array('d', [2.5, 3.2, 3.3]) # float
print(b)
c = array.array('b', [1, 0, 1, 0]) # boolean
print(c)
d = array.array('u', 'hello') # unicode
print(d)

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

eq_space = np.linspace(0, 1, 5)
print(eq_space)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

np.random.seed(1)
uni = np.random.uniform(size=5)
print(uni)

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1

normal = np.random.normal(size=5)
print(normal)

## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)

rand = np.random.randint(0, 10, 5)
print(rand)

## 7. Написать код для создания срезов массива 3 на 4
## - первые две строки и три столбца
## - первые три строки и второй столбец
## - все строки и столбцы в обратном порядке
## - второй столбец
## - третья строка
source = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(source)
print('-' * 10)
print(source[:2, :3])
print('-' * 10)
print(source[:3, 1])
print('-' * 10)
print(source[::-1, ::-1])
print('-' * 10)
print(source[:, 1])
print('-' * 10)
print(source[2, :])

## 8. Продемонстрируйте, как сделать срез-копию
origin = np.array([1, 2, 3, 4, 5])
other = origin[1:-1].copy()
other[1] = 100
print(origin)
print(other)

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

## 10. Разберитесь, как работает метод dstack

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

## 12. Привести пример использования всех универсальных функций, которые я привел

