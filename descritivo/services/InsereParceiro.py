### esse módulo irá ler o CSV de carteira de parceiros e realizar o cadastro de todos os parceiros.
from descritivo.models.parceiro import Parceiro
from core.models.models import AuthUser
import csv
import xlrd


planilha = xlrd.open_workbook("inputs\CONTRATOS.xlsx")
tabela = planilha.sheet_by_name("GERAL")

def LerParceiroDoArquivo():
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        np = str(linha[0]) #nome do provedor
        rs = str(linha[1]) #razao social
        vp = float(linha[3]) #valor pagina
        vr = float(linha[4]) # valor releaser
        vpo = float(linha[5]) #valor policy
        vt = float(linha[6]) #valor tracking
        franquia = int(linha[7]) #franquia
        vm = float(linha[8]) #valor minimo
        CriarParceirosEmLote(np,rs,vp,vr,vpo,vt, franquia, vm)

def CriarParceirosEmLote(np,rs,vp,vr,vpo,vt, franquia, vm):
     Parceiro.objects.create(
            nome_provedor = np,
            razao_social = rs,
            valor_pagina = vp,
            valor_releaser = vr,
            valor_policy = vpo,
            valor_tracking = vt,
            franquia = franquia,
            faturamento_minimo = vm,
            usuario_dono = AuthUser.objects.get(id=1)
        )
