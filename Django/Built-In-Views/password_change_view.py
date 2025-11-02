#PasswordChangeView - базовое представление, которое работает с формой для смены пароля пользователя.
#Работает с связке с базовым представлением PasswordChangeDoneView.

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy


app_name = "my_app"


urlpatterns = [
    path('password-change/', PasswordChangeView.as_view(template_name="my_app/password_change.html", 
            success_url=reverse_lazy('my_app:password_change_done')), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="my_app/password_change_done.html"), name="password_change_done"),
]