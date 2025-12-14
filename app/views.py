from django.shortcuts import render
from django.views.generic import (CreateView, ListView, UpdateView, DetailView, DeleteView)
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Funcionario

# Create your views here.

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = "lista_funcionarios" 

class FuncionarioListView(ListView): 
    model = Funcionario 
    template_name = "lista_funcionarios.html"

class FuncionarioUpdateView(UpdateView): 
    model = Funcionario 
    fields = ("nome", "data_nascimento", "email", "remuneração") 
    template_name = "form_funcionario.html" 
    success_url = reverse_lazy("lista_funcionarios")

class FuncionarioDetailView(DetailView): 
    model = Funcionario 
    template_name = "lista_funcionario.html" 
    context_object_name = "fun"

class FuncionarioDeleteView(DeleteView): 
    model = Funcionario 
    template_name = "remover_funcionario.html" 
    success_url = reverse_lazy("lista_funcionarios")

def confirmar_remocao_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)

    if request.method == 'POST':
        funcionario.delete()
        return redirect('lista_funcionarios')

    return render(request, 'remover_funcionario.html', {
        'funcionario': funcionario
})