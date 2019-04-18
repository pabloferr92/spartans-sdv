from django.db import models

class BancoDados(models.Model):
    id = models.AutoField(primary_key=True)
    nome_banco = models.CharField(max_length=50, blank=True, null=True)
    id_parceiro = models.ForeignKey('Parceiro', models.DO_NOTHING, db_column='id_parceiro', blank=True, null=True)
    volume_paginas = models.IntegerField(blank=True, null=True)
    qtde_releaser = models.IntegerField(blank=True, null=True)
    policy = models.CharField(max_length=3, blank=True, null=True)
    charge_back = models.CharField(max_length=3, blank=True, null=True)
    tracking = models.CharField(max_length=3, blank=True, null=True)
    isento = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banco_dados'