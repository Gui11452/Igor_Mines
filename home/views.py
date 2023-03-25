from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import Perfil

def index(request):
    return redirect('login')

def login(request):
    if request.user.is_authenticated:
        return redirect('mines_hack')
    
    if request.method != 'POST':
        return render(request, 'login.html')

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if not User.objects.filter(email=email).exists():
        messages.error(request, 'O E-mail informado não está atrelado a nenhuma conta!')
        return render(request, 'login.html')

    username = User.objects.get(email=email).username
    user = auth.authenticate(request, username=username, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'login.html')

    if user.username != 'admin':
        perfil = Perfil.objects.get(usuario=user)

        if not perfil:
            return redirect('login')

        if not perfil.validacao:
            messages.error(request, 'Espere o Admnistrador do site validar a sua conta!')
            return redirect('login')

    auth.login(request, user)
    messages.success(request, 'Você fez o login com sucesso!')
    return redirect('mines_hack')


def logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    auth.logout(request)
    messages.success(request, 'Você fez o logout com sucesso!')
    return redirect('login')


def registro(request):
    if request.user.is_authenticated:
        return redirect('login')

    if request.method != 'POST':
        return render(request, 'registro.html')

    email = request.POST.get('email')
    name = request.POST.get('name')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')
    
    if not email or not senha1 or not senha2 or not name:
        messages.error(request, 'Nenhum campo pode ficar vazio!')
        return render(request, 'registro.html')
    
    if len(name) > 15:
        messages.error(request, 'Digite um nome com 15 caracteres ou menos!')
        return render(request, 'registro.html')
    
    if len(senha1) < 8:
        messages.error(request, 'Digite um senha com 8 caracteres ou mais!')
        return render(request, 'registro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido!')
        return render(request, 'registro.html')

    if senha1 != senha2:
        messages.error(request, 'As senhas tem que ser iguais!')
        return render(request, 'registro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'O E-mail informado já está sendo utilizado!')
        return render(request, 'registro.html')
    
    messages.success(request, 'Registrado com sucesso!')
    user = User.objects.create_user(email=email, password=senha1, username=name)
    user.save()
    perfil = Perfil.objects.create(usuario=user)
    perfil.save()

    return redirect('login')


def mines_hack(request):
    if not request.user.is_authenticated:
        messages.success(request, 'Faça o login primeiro!')
        return redirect('login')
    
    if request.user.username != 'admin':
        if not Perfil.objects.filter(usuario=request.user).exists():
            return redirect('login')

        perfil = Perfil.objects.get(usuario=request.user)

        if not perfil.validacao:
            messages.error(request, 'Espere o Admnistrador do site validar a sua conta!')
            return redirect('login')

    return render(request, 'mines_hack.html')

