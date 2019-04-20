from django.db import models
from descritivo.models.banco_dados import BancoDados

class AuditoriaBanco(models.Model):
    id_banco = models.ForeignKey('BancoDados', models.DO_NOTHING, db_column='id_banco', blank=True, null=True)
    nome_banco = models.CharField(max_length=50, blank=True, null=True)
    nome_banco_new = models.CharField(max_length=50, blank=True, null=True)
    qtde_releaser = models.IntegerField(blank=True, null=True)
    qtde_releaser_new = models.IntegerField(blank=True, null=True)
    policy = models.CharField(max_length=50, blank=True, null=True)
    policy_new = models.CharField(max_length=50, blank=True, null=True)
    charge_back = models.CharField(max_length=50, blank=True, null=True)
    charge_back_new = models.CharField(max_length=50, blank=True, null=True)
    tracking = models.CharField(max_length=50, blank=True, null=True)
    tracking_new = models.CharField(max_length=50, blank=True, null=True)
    isento = models.CharField(max_length=50, blank=True, null=True)
    isento_new = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_banco'
