# Generated by Django 3.2.14 on 2022-11-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20221102_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador',
            name='es_porcentual',
            field=models.BooleanField(default=False),
        ),
    ]
