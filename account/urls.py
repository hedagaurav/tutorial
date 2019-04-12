from django.urls import path
from account.views import home, user_login, user_logout
# from django.contrib.auth.views import LoginView

app_name = 'account'
urlpatterns = [
    path('', home, name='account_home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
