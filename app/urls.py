from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_lavagens, name='listar_lavagens'),
    path('nova/', views.criar_lavagem, name='criar_lavagem'),
    path('editar/<int:lavagem_id>/', views.editar_lavagem, name='editar_lavagem'),
    path('deletar/<int:lavagem_id>/', views.deletar_lavagem, name='deletar_lavagem'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente' )
]