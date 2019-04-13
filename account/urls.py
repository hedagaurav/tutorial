from django.urls import path
from account.views import user_home, user_login, user_logout, user_register

# from django.contrib.auth.views import LoginView

app_name = 'account'
urlpatterns = [
    path('', user_home, name='account_home'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
