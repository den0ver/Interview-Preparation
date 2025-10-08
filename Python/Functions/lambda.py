# lambda - это анонимная функция в Python, которая используется одноразово.


# Обычная функция
def func(a, b):
    return a + b


# lambda-функция
lambda_func = lambda a, b: a + b


print(func(90, 10))
print(lambda_func(90, 10))
print()



numbers = list(range(1, 11))
users = [
    {'name': 'artem', 'age': 16, 'country': 'Spain'},
    {'name': 'denys', 'age': 17, 'country': 'USA'},
    {'name': 'seva', 'age': 18, 'country': 'Germany'},
    {'name': 'tanya', 'age': 18, 'country': 'Ukraine'},
]


# sorted()
sorted_data = sorted(users, key=lambda user: user['age'])


# map()
result = list(map(lambda x: x * 2, numbers))


# filter()
result2 = list(filter(lambda x: x % 2 == 0, numbers))


for i, user in enumerate(sorted_data):
    if i == len(sorted_data) - 1:
        print(f"{user['name'].title()} is {user['age']}.")
    else:
        print(f"{user['name'].title()} is {user['age']},")


print()
print(result)
print(result2)