from django.db import models


class Parceiro(models.Model):
    id = models.IntegerField(primary_key=True)
    nome_provedor = models.CharField(max_length=50, blank=True, null=True)
    razao_social = models.CharField(max_length=150, blank=True, null=True)
    valor_pagina = models.FloatField(blank=True, null=True)
    valor_releaser = models.FloatField(blank=True, null=True)
    valor_policy = models.FloatField(blank=True, null=True)
    valor_tracking = models.FloatField(blank=True, null=True)
    franquia = models.IntegerField(blank=True, null=True)
    faturamento_minimo = models.IntegerField(blank=True, null=True)
    usuario_dono = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='usuario_dono', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parceiro'
