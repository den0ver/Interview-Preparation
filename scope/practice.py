num = 100  #глобальная переменная


def outer():
    global num  #делаем переменную x доступной в outer()
    num = 123
    value = 50  #локальная переменная
    def inner():
        nonlocal value  #делаем переменную value доступной в inner()
        return value + 10
    return f"Value: {inner()}\nNum: {num}" 

print(outer())


def make_multiplier(num1):
    def inner(num2):
        nonlocal num1
        return num1 * num2
    return inner

times3 = make_multiplier(3)
print(times3(5))
