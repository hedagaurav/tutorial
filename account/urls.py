from django.urls import path
from account.views import home
from django.contrib.auth.views import LoginView

app_name = 'account'
urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
]
