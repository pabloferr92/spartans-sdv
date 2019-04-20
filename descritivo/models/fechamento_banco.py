from django.db import models
from descritivo.models.banco_dados import BancoDados

class FechamentoBanco(models.Model):
    id_banco = models.ForeignKey(BancoDados, models.DO_NOTHING, db_column='id_banco', blank=True, null=True)
    volume_paginas = models.CharField(max_length=10, blank=True, null=True)
    valor_paginas = models.IntegerField(blank=True, null=True)
    qtde_releaser = models.IntegerField(blank=True, null=True)
    valor_releaser = models.IntegerField(blank=True, null=True)
    volume_policy = models.IntegerField(blank=True, null=True)
    valor_policy = models.IntegerField(blank=True, null=True)
    volume_charge_back = models.IntegerField(blank=True, null=True)
    valor_charge_back = models.IntegerField(blank=True, null=True)
    volume_tracking = models.IntegerField(blank=True, null=True)
    valor_tracking = models.IntegerField(blank=True, null=True)
    valor_total = models.IntegerField(blank=True, null=True)
    mes_referencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fechamento_banco'