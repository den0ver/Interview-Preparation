from datetime import date
# filter() - функция высшего порядка, которая фильтрует объекты по условию.


numbers = list(range(1, 11))


# Сохранить только чётные числа.
result = list(filter(lambda num: num % 2 == 0, numbers))


print(result)
print()


users = [
    {'name': 'denys', 'birthday': date(2008, 7, 16)},
    {'name': 'tanya', 'birthday': date(2006, 9, 12)},
    {'name': 'dima', 'birthday': date(2015, 5, 21)},
    {'name': 'milana', 'birthday': date(2019, 12, 7)},
]


# Сохранить пользователей которые родились позже 2014
result2 = list(filter(lambda user: user['birthday'] > date(2014, 1, 1), users))


for r in result2:  
    print(f"{r['name'].title()}'s birthday: {r['birthday']}")