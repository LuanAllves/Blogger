from django.contrib.auth import views as auth_views
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    # URLS para Login, Logout e Register.
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', next_page='/'), name="loginview"), # Página de Login.
    path('logout/', auth_views.LogoutView.as_view(), name="logoutview"), # Pagina de Logout.

]