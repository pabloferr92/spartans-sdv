from fechaProdutos import fechaReleaser, contaReleaser, fechaContador, fechaPoliticas, contaPoliticas, fechaMarca, contaMarca, contaContador
from fechaProdutos import contaContas,fechaContas

def fechaVolumes(parceiro):
    volumes = {"parceiro":parceiro,
    "qtdeReleaser":"",
    "bancosReleaser":"",
    "volume":"",
    "bancosVolume":"",
    "volumePoliticas":"",
    "bancosPoliticas":"",
    "volumeMarca":"",
    "bancosMarca":"",
    }
    volumes["qtdeReleaser"] = int(fechaReleaser(parceiro))
    volumes["bancosReleaser"] = int(contaReleaser(parceiro))
    volumes["volume"]= int(fechaContador(parceiro))
    volumes["bancosVolume"]= int(contaContador(parceiro))
    volumes["volumePoliticas"]= int(fechaPoliticas(parceiro))
    volumes["bancosPoliticas"] = int(contaPoliticas(parceiro))
    volumes["volumeMarca"] = int(fechaMarca(parceiro))
    volumes["bancosMarca"] = int(contaMarca(parceiro))
    return volumes


