from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.listar_salvar_autores),
    path('autores/<int:pk>/', views.deletar_autores),
    path('livros/', views.listar_salvar_livros)
]
