# map() - функция высшего порядка, которая применяет действие ко всем элементам.


numbers = list(range(1, 11))


# Возведение в квадрат.
result = list(map(lambda num: num ** 2, numbers))


print(result)
print()


users = ['denys', 'artem', 'gleb', 'seva']


# Преобразовать список строк в заглавные.
result2 = list(map(lambda user: user.title(), users))


print(result2)
print()


# Добавить 10 к каждому числу.
result3 = list(map(lambda num: num + 10, numbers))


print(result3)
print()


f_name = ['denys', 'seva', 'tanya']
l_name = ['iliashenko', 'orlovskiy', 'myronenko']


# Объединяем имя и фамилию.
result4 = list(map(lambda f, l: f.title() + ' ' + l.title(), f_name, l_name))


print(result4)