#authenticate - функция, которая проверяет логин и пароль, если все окей возвращает - объект User, если нет - None.
#работает в связке с функцией login()

from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    #...
    cd = LoginForm(request.POST).cleaned_data
    user = authenticate(request, username=cd['username'], password=cd['password'])  #использование
    if user is not None and user.is_active:
        login(request, user) 
        #...
