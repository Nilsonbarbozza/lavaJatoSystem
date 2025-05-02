from django.shortcuts import render, redirect, get_object_or_404
from .models import Lavagem, Cliente
from django.urls import reverse
from django.utils import timezone


# 🔍 READ – Listar lavagens
def listar_lavagens(request):
    if request.method == 'GET':
        lavagens = Lavagem.objects.select_related('cliente').order_by('-data')
        return render(request, 'agendamentos/lista.html', {'lavagens': lavagens})
    lavagens = Lavagem.objects.select_related('cliente').order_by('-data')
    return render(request, 'agendamentos/lista.html', {'lavagens': lavagens})

# ➕ CREATE – Criar novo cliente
def criar_cliente(request):
    if request.method == "GET":
        return render(request, "agendamentos/criar_cliente.html")
    
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
    
    if nome and telefone:
        cliente = Cliente.objects.create(
            nome=nome,
            telefone=telefone,
        )
        return redirect('criar_cliente')
    return render(request, 'agendamentos/criar_cliente.html')


# ➕ CREATE – Agendar nova lavagem
def criar_lavagem(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        tipo = request.POST['tipo']
        data = request.POST['data']

        lavagem = Lavagem.objects.create(
            cliente_id=cliente_id,
            tipo=tipo,
            data=data,
            concluida=False
        )
        return redirect('listar_lavagens')
    return render(request, 'agendamentos/form.html', {'clientes': clientes})

# ✏️ UPDATE – Editar lavagem
def editar_lavagem(request, lavagem_id):
    lavagem = get_object_or_404(Lavagem, pk=lavagem_id)
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        lavagem.cliente_id = request.POST['cliente']
        lavagem.tipo = request.POST['tipo']
        lavagem.data = request.POST['data']
        lavagem.concluida = 'concluida' in request.POST
        lavagem.save()
        return redirect('listar_lavagens')
    
    return render(request, 'agendamentos/form.html', {
        'lavagem': lavagem,
        'clientes': clientes
    })

# ❌ DELETE – Remover lavagem
def deletar_lavagem(request, lavagem_id):
    lavagem = get_object_or_404(Lavagem, pk=lavagem_id)
    if request.method == 'POST':
        lavagem.delete()
        return redirect('listar_lavagens')
    return render(request, 'agendamentos/confirm_delete.html', {'lavagem': lavagem})
