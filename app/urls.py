from django.urls import path, include
from . import views
from .views import (FuncionarioCreateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioDetailView, FuncionarioDeleteView)

urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view(), name="form_funcionario"),
    path('lista_funcionarios', FuncionarioListView.as_view(), name = "lista_funcionarios"),
    path('form_funcionario/<int:pk>', FuncionarioUpdateView.as_view(), name = "editar_funcionario"),
    path('lista_funcionario/<int:pk>', FuncionarioDetailView.as_view(), name = "listar_funcionario"),
    path('remover_funcionario/<int:pk>/', views.confirmar_remocao_funcionario, name='remover_funcionario'),
]