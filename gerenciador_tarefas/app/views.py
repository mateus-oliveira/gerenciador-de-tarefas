from django.shortcuts import render


# Create your views here.

def listar_tarefas(request):
    nome_tarefa = "Estudar para o ENEM"
    return render(request, 'tarefas/listar_tarefas.html', {"nome": nome_tarefa})
