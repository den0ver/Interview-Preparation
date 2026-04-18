#isdigit() - метод, который проверяет, состоил ли строка из цифр.

item = '12345' 
print(item.isdigit()) #True

item = 'abc123' 
print(item.isdigit()) #False


#Сохраняем в списке только цифры
item = 'abc123'
a = [int(i) for i in item if i.isdigit() == True]
print(a) #[1, 2, 3]