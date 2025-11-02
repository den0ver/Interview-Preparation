#PasswordResetView - базовое представление, которое позволяет пользователю сбросить свой пароль.
#Генерирует одноразовую ссылку с токеном и отправляет её на электронную почту юзера.
#Работает с связке с базовым представлением PasswordResetDoneView.

from django.contrib.auth.views import PasswordResetView
from django.urls import path


urlpatterns = [
    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
]