from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_salvar_autores),
    path('<int:pk>/', views.deletar_autores)
]
