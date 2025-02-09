# Generated by Django 5.1.6 on 2025-02-09 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Brend nomi')),
                ('country', models.CharField(max_length=100, verbose_name='Kelib chiqishi')),
                ('founded_at', models.DateTimeField(blank=True, null=True, verbose_name='Tashkil topgan vaqti')),
            ],
            options={
                'verbose_name': 'Brend',
                'verbose_name_plural': 'Brendlar',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Mashina nomi')),
                ('model_year', models.IntegerField(verbose_name='Model yili')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narxi')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.brand', verbose_name='Brendi')),
            ],
            options={
                'verbose_name': 'Mashina',
                'verbose_name_plural': 'Mashinalar',
            },
        ),
    ]
