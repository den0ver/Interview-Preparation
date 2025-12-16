#PasswordResetConfirmView - базовое представление, которое позволяет пользователям устанавливать новый пароль.
#Работает с связке с базовым представлением PasswordResetCompleteView.

from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy


app_name = 'my_app'


urlpatterns = [
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="my_app/password_reset_confirm.html", 
                    success_url=reverse_lazy('my_app:password_reset_complete')), name="password_reset_confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="my_app/password_reset_complete.html"), name="password_reset_complete"),
]