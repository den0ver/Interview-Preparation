#login - функция, которая создаёт сессию и впускает пользователя в систему.
#работает в связке с функцией authenticate()

from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    #...
    cd = LoginForm(request.POST).cleaned_data
    user = authenticate(request, username=cd['username'], password=cd['password'])
    if user is not None and user.is_active:
        login(request, user)  #использование
        #...
