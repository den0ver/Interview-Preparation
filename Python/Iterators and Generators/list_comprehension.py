"""создаём список с чётными числами"""
nums = list(range(1, 11))

a = [i for i in nums if i%2==0]
print(a)


"""C помощью input()+split() разбиваем каждый ответ на объект списка
и далее меняем тип на int."""
question = input().split()
b = [int(item) for item in question]
print(type(b[0]))



"""Из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
 получить список кубов только нечётных чисел.
"""
nums = list(range(1, 11))
c = [item**3 for item in nums if not item%2==0]
print(c)


"""
Из списка слов ["apple", "banana", "kiwi", "mango"] оставить только те,
длина которых больше 4 символов, и привести их к верхнему регистру.
"""
arr = ['apple', 'banana', 'kiwi', 'mango']
d = [item.upper() for item in arr if len(item) > 4]
print(d)


"""
Создать список пар (i, i²) для чисел от 1 до 5.
"""
e = [(i, i**2) for i in range(1, 6)]
print(e)


"""
«Сгладить» вложенный список [[1,2],[3,4],[5,6]]
 в один плоский список.
"""
arr = [[1, 2], [3, 4], [5, 6]]
k = [i for item in arr for i in item]
print(k)