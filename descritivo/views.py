from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from descritivo.models.parceiro import Parceiro
from .forms import ParceiroForm
from descritivo.models.banco_dados import BancoDados
from descritivo.forms import BancoForm
from core.models.models import AuthUser


def ler_parceiro(request):
    context = {
        "parceiros": Parceiro.objects.all()
    }
    return render(request,"ListaParceiros.html", context)

def criar_parceiro(request):
    form = ParceiroForm(request.POST, None)
    if request.method == "POST":
        usuario_dono = AuthUser.objects.get(id=request.POST.get('usuario_dono'))
        Parceiro.objects.create(
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
        return redirect('parceiros')
    return render(request, "FormParceiro.html",{"form": form} )

def alterar_parceiro(request,id):
    parceiro = Parceiro.objects.get(id=id)
    form = ParceiroForm(instance=parceiro)
    if request.method == "GET":
        return render(request, "FormParceiro.html", {"form": form})
    dono = AuthUser.objects.get(id=request.POST.get('usuario_dono'))
    parceiro.nome_provedor =request.POST.get('nome_provedor')
    parceiro.razao_social=request.POST.get('razao_social')
    parceiro.valor_pagina = request.POST.get('valor_pagina')
    parceiro.valor_releaser = request.POST.get('valor_releaser')
    parceiro.valor_policy = request.POST.get('valor_policy')
    parceiro.valor_tracking = request.POST.get('valor_tracking')
    parceiro.franquia = request.POST.get('franquia')
    parceiro.faturamento_minimo = request.POST.get('faturamento_minimo')
    parceiro.usuario_dono = dono
    parceiro.save()
    return redirect('parceiros')
    

def remover_parceiro(request,id):
    parceiro = Parceiro.objects.filter(id=id)
    parceiro.delete()
    return redirect('parceiros')

def ler_banco(request):
    context = {
        "bancos": BancoDados.objects.all()
    }
    return render(request,"ListaBancos.html", context)

def criar_banco(request):
    form = BancoForm(request.POST, None)
    if request.method == "POST":
        id_parceiro = Parceiro.objects.get(id=request.POST.get('id_parceiro'))
        BancoDados.objects.create(
            nome_banco = request.POST.get('nome_banco'),
            id_parceiro = id_parceiro,
            volume_paginas = request.POST.get('volume_paginas'),
            qtde_releaser = request.POST.get('qtde_releaser'),
            policy = request.POST.get('policy'),
            charge_back = request.POST.get('charge_back'),
            tracking = request.POST.get('tracking'),
            isento = request.POST.get('isento'),
        )
        return redirect('bancos')
    return render(request, "FormBancos.html",{"form": form} )

def alterar_banco(request,id):
    banco = BancoDados.objects.get(id=id)
    form = BancoForm(instance=banco)
    if request.method == "GET":
        return render(request, "FormBancos.html", {"form": form})
    parceiro = Parceiro.objects.get(id=request.POST.get('id_parceiro'))
    banco.nome_banco =request.POST.get('nome_banco')
    banco.id_parceiro= parceiro
    banco.volume_paginas = request.POST.get('volume_paginas')
    banco.qtde_releaser = request.POST.get('qtde_releaser')
    banco.policy = request.POST.get('policy')
    banco.charge_back = request.POST.get('charge_back')
    banco.tracking = request.POST.get('tracking')
    banco.isento = request.POST.get('isento')
    banco.save()
    return redirect('bancos')
    

def remover_banco(request,id):
    banco = BancoDados.objects.get(id=id)
    banco.delete()
    return redirect('bancos')
