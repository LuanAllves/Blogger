from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', next_page='/'), name="loginview"), # Página de Login.
    path('logout/', auth_views.LogoutView.as_view(), name="logoutview"), # Pagina de Registro.
]