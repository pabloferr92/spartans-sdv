from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from core.models.models import AuthUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserForm

def home(request):
    return render(request, "home.html")


'''def autenticar(email,senha):
    U = Usuario.objects.get(email=email)
    if U:
        if U.senha == senha:
            return U
        return ("Usuário senha incorreta")
    return None '''

def entrar(request):
    if request.method == "POST":
        username=request.POST.get('email')
        password=request.POST.get('senha')
        usuario= authenticate(username=request.POST.get('email'),password=request.POST.get('senha'))
        if usuario is not None:            
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect('/home/usuarios/')
            return HttpResponseRedirect('/home/login/')
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    #HttpResponse.delete_cookie('sessionid')
    return HttpResponseRedirect('/')


def lerUsuarios(request):
    contexto = {
    "usuarios" : AuthUser.objects.all()
    }
    print("os usuarios são: ",contexto["usuarios"])
    return render(request,'ListaUsuarios.html',contexto)


def alterarusuario(request, iduser):
    usuario = AuthUser.objects.get(id=iduser)
    form = UserForm(instance=usuario)
    if request.method == "GET":
        return render(request, "formUsuario.html", {"form": form})
    username=request.POST.get('username')
    email=request.POST.get('email')
    user = User.objects.get(id=iduser)
    user.username = username
    user.email = email
    user.set_password(request.POST.get("password"))
    user.save()
    return redirect('usuarios')
    


def removerusuario(request,iduser):
    contexto = {
    "usuarios" : AuthUser.objects.all()
    }
    usuario = AuthUser.objects.filter(id=iduser)
    usuario.delete()
    return render(request,'ListaUsuarios.html',contexto)

def inserirusuario(request):
    form = UserForm(request.POST, None)
    if request.method == "POST":
        user = User.objects.create_user(username= request.POST.get("username"),
        password= request.POST.get("password"),
        email= request.POST.get("email"))   
        user.save()
        print(user)
        return redirect('usuarios')
    return render(request, "formUsuario.html",{"form": form} )




# Create your views here.
