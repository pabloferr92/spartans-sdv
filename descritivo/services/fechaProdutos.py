import xlrd

planilha = xlrd.open_workbook("datacenter.xlsx")

tabela = planilha.sheet_by_name("Base Dados")

def fechaContador(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro:
            totalContador+=linha[44]
    return totalContador

def contaContador(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro:
            totalContador=totalContador+1
        empresa = linha[0]
    return totalContador


def fechaReleaser(parceiro):
    totalReleaser = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro:
            totalReleaser+=int(linha[19])
    return totalReleaser


def fechaPoliticas(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro and (str(linha[20]) == "Sim" or str(linha[23])=="Sim"):
            totalContador+=linha[44]
    return totalContador

def fechaContas(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro and str(linha[22]) == "Sim":
            totalContador+=linha[44]
    return totalContador


def fechaMarca(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro and str(linha[21]) == "Sim":
            totalContador+=linha[44]
    return totalContador


def contaPoliticas(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro and (str(linha[20])=="Sim" or str(linha[23])=="Sim") :
            totalContador=totalContador+1
    return totalContador


def contaMarca(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro and str(linha[21])=="Sim":
            totalContador=totalContador+1
    return totalContador


def contaContas(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro and str(linha[23])=="Sim":
            totalContador=totalContador+1
    return totalContador

def contaReleaser(parceiro):
    totalContador = 0
    for i in range(tabela.nrows):
        if i == 0 or i == 1:
            continue
        linha = tabela.row_values(i)
        
        if str(linha[6])==parceiro and str(linha[19])!='0.0':
            totalContador=totalContador+1
    return totalContador
