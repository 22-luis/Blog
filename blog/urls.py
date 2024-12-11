from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detalle de un post
    path('new/', views.new_post, name='new_post'),  # Crear un post
]
