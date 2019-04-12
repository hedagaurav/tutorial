from django.urls import path
from account.views import home, login, logout
# from django.contrib.auth.views import LoginView

app_name = 'account'
urlpatterns = [
    path('', home, name='home'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
