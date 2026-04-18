#isalpha() - метод, который проверяет, состоил ли строка только из букв.

item = 'abc'
print(item.isalpha()) #True

item = 'abc123'
print(item.isalpha()) #False


a = [i for i in 'abc123' if i.isalpha()]
print(a) #['a', 'b', 'c']