#is_active - поле пользователя, которое показывает активен ли он: если False - нельзя войти в систему, True - можно.


from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from my_app.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:  #использование атрибута
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid log-in')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)