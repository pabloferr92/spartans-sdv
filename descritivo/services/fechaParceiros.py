from listaParceiros import listaParceiro
from fechaProdutos import fechaContador, fechaContas, fechaMarca, fechaReleaser, fechaPoliticas
import csv

def custoDoParceiro(parceiro):
    lista = listaParceiro()
    for i in lista:
        if i[0] == parceiro:
            return i
    print("Parceiro não cadastrado na planilha de custos")

def volumePorProduto(parceiro):
    volumeTotal = {
        "qtdeReleaser":"",
        "volume":"",
        "volumePoliticas":"",
        "volumeMarca":"",
        
    } 
    volumeTotal["qtdeReleaser"] = fechaReleaser(parceiro)
    volumeTotal["volume"] = fechaContador(parceiro)
    volumeTotal["volumePoliticas"] = fechaPoliticas(parceiro)
    volumeTotal["volumeMarca"] = fechaMarca(parceiro)
    return volumeTotal

def custoGeralParceiro(parceiro):
    fechamento = {
    "custoMPS":"",
    "custoReleaser":"",
    "custoPoliticas":"",
    "custoMarca": "",
    "total":""
    }
    custo = custoDoParceiro(parceiro)
    volumeGeral = volumePorProduto(parceiro)
    fechamento['custoMPS'] = volumeGeral["volume"]*float(custo[2])
    fechamento['custoReleaser'] = volumeGeral["qtdeReleaser"]*float(custo[3])
    fechamento['custoPoliticas'] = volumeGeral["volumePoliticas"]*float(custo[4])
    fechamento['custoMarca'] = volumeGeral["volumeMarca"]*float(custo[5])
    fechamento["total"] = round(fechamento['custoMarca'] + fechamento['custoPoliticas'] + fechamento['custoReleaser'] + fechamento['custoMPS'],2)
    return fechamento
