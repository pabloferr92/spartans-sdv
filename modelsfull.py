# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BancoDados(models.Model):
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Parceiro(models.Model):
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


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
