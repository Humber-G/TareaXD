# Generated by Django 3.2.3 on 2021-06-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50, verbose_name='Nombre Categoria')),
                ('descripcion_categoria', models.TextField(max_length=150, verbose_name='Descripción Categoria')),
            ],
        ),
    ]
