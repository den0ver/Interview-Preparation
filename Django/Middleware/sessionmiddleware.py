#SessionMiddleware - отвечает за поддержку сессий

#request.session - объект (dict) с данными сесси на сервере.

from django.http import HttpResponse


def set_session(request):  #редактирование
    request.session['username'] = 'den0ver'
    request.session['is_logged_in'] = True
    return HttpResponse('Сессия установлена')


def get_session(request):  #получение
    username = request.session.get('username')
    is_logged = request.session.get('is_logged_in')
    return HttpResponse(f'Name: {username},\nLogged In: {is_logged}.')


def clear_session(request):
    request.session.flush()


def visit_counter(request):
    visits = request.session.get('visits', 0)
    visits += 1
    request.session['visits'] = visits
    return HttpResponse('{visits} раз вы зашли на эту страницу.')