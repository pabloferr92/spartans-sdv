from django.db import models
from descritivo.models.parceiro import Parceiro


class FechamentoParceiro(models.Model):
    idparceiro = models.ForeignKey('Parceiro', models.DO_NOTHING, db_column='idparceiro', blank=True, null=True)
    volume_total = models.IntegerField(blank=True, null=True)
    total_bancos = models.IntegerField(blank=True, null=True)
    valor_volume = models.IntegerField(blank=True, null=True)
    bancos_releaser = models.IntegerField(blank=True, null=True)
    total_releaser = models.IntegerField(blank=True, null=True)
    valor_releaser = models.IntegerField(blank=True, null=True)
    bancos_policy = models.IntegerField(blank=True, null=True)
    volume_policy = models.IntegerField(blank=True, null=True)
    valor_policy = models.IntegerField(blank=True, null=True)
    bancos_tracking = models.IntegerField(blank=True, null=True)
    volume_tracking = models.IntegerField(blank=True, null=True)
    valor_tracking = models.IntegerField(blank=True, null=True)
    mes_referencia = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fechamento_parceiro'