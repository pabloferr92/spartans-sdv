import csv
import xlrd
from models.banco import insert_banco
from models.parceiro import read_parceiro

planilha = xlrd.open_workbook("datacenter.xlsx")
tabela = planilha.sheet_by_name("Base Dados")



def ResgistrarBancos(parceiro):
    idparceiro = read_parceiro("SELECT idparceiro FROM parceiro where nome_provedor = {}".format(parceiro))[0][0]
    for i in range(tabela.nrows):
        if i == 0:
            continue
        linha = tabela.row_values(i)
        if str(linha[6])==parceiro:
            vp = linha[44]
            vr = linha[19]
            if (str(linha[20]) == "Sim" or str(linha[23])=="Sim"):
                vpo=linha[44]
            if str(linha[6])==parceiro and str(linha[21]) == "Sim":
                vt = linha[44]
            print(idparceiro,vp,vr,vpo,vt)
            insert_banco(idparceiro,vp,vr,vpo,vt)

ResgistrarBancos("LELLOPRINT")