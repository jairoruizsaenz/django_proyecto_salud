# Generated by Django 3.2.14 on 2022-08-18 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterModelOptions(
            name='indicador',
            options={'verbose_name': 'Indicador', 'verbose_name_plural': 'Indicadores'},
        ),
    ]
