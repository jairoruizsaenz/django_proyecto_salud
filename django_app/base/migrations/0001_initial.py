# Generated by Django 3.2.14 on 2022-11-02 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divipola', models.CharField(max_length=2, unique=True)),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Dimensión',
                'verbose_name_plural': 'Dimensiones',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=255)),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.dimension')),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'Indicadores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divipola', models.CharField(max_length=5, unique=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.departamento')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Punto_Salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(default='', max_length=255)),
                ('municipio', models.CharField(default='', max_length=255)),
                ('direccion', models.CharField(default='', max_length=255, verbose_name='Dirección')),
                ('longitud', models.CharField(default='', max_length=255)),
                ('latitud', models.CharField(default='', max_length=255)),
                ('es_IPS', models.CharField(choices=[('Sí', 'Sí'), ('No', 'No')], default='-', max_length=2, verbose_name='¿Esta sede pertenecerá o será una IPS?')),
                ('naturaleza_juridica', models.CharField(choices=[('Pública', 'Pública'), ('Privada', 'Privada'), ('Mixta', 'Mixta')], default='-', max_length=7, verbose_name='Naturaleza jurídica de la IPS')),
                ('nivel_atencion', models.CharField(choices=[('Primer nivel', 'Primer nivel'), ('Segundo nivel', 'Segundo nivel'), ('Tercer nivel', 'Tercer nivel')], default='-', max_length=13, verbose_name='Nivel de atención (Si es pública)')),
                ('entidad_territorial', models.CharField(choices=[('Municipal', 'Municipal'), ('Departamental', 'Departamental')], default='-', max_length=13, verbose_name='Entidad territorial a la que pertenece')),
                ('tipo_servicios', models.CharField(choices=[('Primario', 'Primario'), ('Complementario', 'Complementario')], default='-', max_length=14, verbose_name='Tipo de servicios')),
            ],
            options={
                'verbose_name': 'Punto de salud',
                'verbose_name_plural': 'Puntos de salud',
            },
        ),
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
                'ordering': ['indicador', 'municipio'],
            },
        ),
    ]