#isdigit() - метод, который проверяет, состоил ли строка из цифр.

item = '12345' #True
print(item.isdigit())

item = 'abc123' #False
print(item.isdigit())


#Сохраняем в списке только цифры
item = 'abc123'
a = [int(i) for i in item if i.isdigit() == True]
print(a) #[1, 2, 3]