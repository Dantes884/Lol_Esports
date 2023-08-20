# Generated by Django 4.2.4 on 2023-08-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_player_role'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='substitution',
            field=models.ManyToManyField(blank=True, null=True, related_name='sub', to='players.player'),
        ),
    ]