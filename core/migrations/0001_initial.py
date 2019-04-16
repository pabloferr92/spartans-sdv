# Generated by Django 2.1.8 on 2019-04-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('iduser', models.AutoField(db_column='iduser', primary_key=True, serialize=False)),
                ('logon', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('senha', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('celular', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('dtexpiracao', models.DateField(blank=True, db_column='dtExpiracao', null=True)),
            ],
            options={
                'db_table': 'aluno',
                'managed': True,
            },
        ),
    ]