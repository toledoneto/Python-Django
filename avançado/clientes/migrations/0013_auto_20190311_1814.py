# Generated by Django 2.1.7 on 2019-03-11 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_auto_20190309_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('deletar_clientes', 'User pode deletar clientes'),)},
        ),
    ]
