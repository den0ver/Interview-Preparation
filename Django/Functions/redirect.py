#redirect() - функция, которая перенаправляет пользователя на другую страницу


from django.shortcuts import redirect


def my_view(request):
    return redirect('URL-route')