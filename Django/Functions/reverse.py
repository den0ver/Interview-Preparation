#reverse - функция, которая строит URL по имени маршрута и аргументам.
#Работает в связке с функцией redirect()

from django.urls import reverse
from django.shortcuts import redirect


def func(request):
    return redirect(reverse('my_app:home'))