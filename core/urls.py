from django.urls import path, include
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.dashboard_view, name="dashboardview"), # Página Dashboard.
    path('reels/', views.reels_view, name="reelsview"), # Pagina Reels onde listara todas os post's.
    path('post/', views.post_view, name="postview"), # Página post para os post's do blogger.
]
