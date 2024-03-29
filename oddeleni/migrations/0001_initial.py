# Generated by Django 5.0 on 2024-02-22 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oddeleni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('nazev', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pokoje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delka', models.IntegerField()),
                ('Pokoj', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokoje', to='oddeleni.oddeleni')),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First', models.CharField(max_length=64)),
                ('Last', models.CharField(max_length=64)),
                ('Oddeleni', models.ManyToManyField(blank=True, related_name='pacienti', to='oddeleni.pokoje')),
            ],
        ),
    ]
