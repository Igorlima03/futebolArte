# Generated by Django 5.0.2 on 2024-02-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('SP', 'São Paulo'), ('RJ', 'Rio de Janeiro'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('RS', 'Rio Grande do Sul')], max_length=120, null=True)),
                ('cores', models.CharField(blank=True, max_length=80, null=True)),
                ('ano_fundacao', models.PositiveBigIntegerField(default=0)),
                ('tem_mundial', models.BooleanField(default=False)),
            ],
        ),
    ]