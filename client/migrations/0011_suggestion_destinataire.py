# Generated by Django 4.2 on 2023-05-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_billet_bl_valide'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='destinataire',
            field=models.CharField(default='La Plateforme', max_length=30),
        ),
    ]
