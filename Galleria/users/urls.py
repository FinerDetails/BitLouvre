from django.urls import  path
from . views import *

#MITÄ VITTUA MÄ TEEN :D
#auth_view.LoginView.as_view(), name='login'
app_name = 'users'
urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', logout_request, name='logout'),
]
