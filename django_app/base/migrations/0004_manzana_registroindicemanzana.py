# Generated by Django 3.2.14 on 2023-02-22 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_indicador_es_porcentual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manzana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divipola', models.CharField(max_length=5, unique=True)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.municipio')),
            ],
            options={
                'ordering': ['divipola'],
            },
        ),
        migrations.CreateModel(
            name='RegistroIndiceManzana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.indicador')),
                ('manzana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.manzana')),
            ],
            options={
                'verbose_name': 'Registro índice - Manzana',
                'verbose_name_plural': 'Registros índices - Manzana',
                'ordering': ['indicador', 'manzana'],
            },
        ),
    ]
