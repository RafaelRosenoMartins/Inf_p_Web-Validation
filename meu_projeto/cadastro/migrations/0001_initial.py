# Generated by Django 5.1.5 on 2025-02-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]
