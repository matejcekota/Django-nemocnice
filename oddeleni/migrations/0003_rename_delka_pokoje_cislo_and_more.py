# Generated by Django 5.0 on 2024-02-22 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oddeleni', '0002_alter_pacient_oddeleni_alter_pokoje_pokoj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokoje',
            old_name='Delka',
            new_name='Cislo',
        ),
        migrations.RenameField(
            model_name='pokoje',
            old_name='Pokoj',
            new_name='Oddeleni',
        ),
    ]
