import xlrd

planilha = xlrd.open_workbook("CONTRATOS.xlsx")

tabela = planilha.sheet_by_name("GERAL")

def listaParceiro():
    lista = []
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        lista.append(linha)
    return lista

def custoParceiro(parceiro):
    for i in range(tabela.nrows):
            if i == 0:
                continue
            linha = tabela.row_values(i)