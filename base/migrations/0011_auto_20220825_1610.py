# Generated by Django 3.2.14 on 2022-08-25 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20220825_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroIndiceMunicipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.indicador')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.municipio')),
            ],
            options={
                'verbose_name': 'Registro índice - municipal',
                'verbose_name_plural': 'Registros índices - municipal',
            },
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]