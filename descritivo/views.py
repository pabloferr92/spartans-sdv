from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from descritivo.models.parceiro import Parceiro
from .forms import ParceiroForm
from core.models.models import AuthUser


def ler_parceiro(request):
    pass

def criar_parceiro(request):
    form = ParceiroForm(request.POST, None)
    if request.method == "POST":
        usuario_dono = AuthUser.objects.get(id=request.POST.get('usuario_dono'))
        Parceiro.objects.create(
            id = 1,
            nome_provedor = request.POST.get('razao_social'),
            razao_social = request.POST.get('razao_social'),
            valor_pagina = request.POST.get('valor_pagina'),
            valor_releaser = request.POST.get('valor_releaser'),
            valor_policy = request.POST.get('valor_policy'),
            valor_tracking = request.POST.get('valor_tracking'),
            franquia = request.POST.get('franquia'),
            faturamento_minimo = request.POST.get('faturamento_minimo'),
            usuario_dono = usuario_dono
        )
        return redirect('usuarios')
    return render(request, "FormParceiro.html",{"form": form} )

def alterar_parceiro(request):
    pass

def remover_parceiro(request):
    pass
