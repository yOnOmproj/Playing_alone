# Generated by Django 3.1.1 on 2020-09-24 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonomApp', '0003_game_data_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_data',
            old_name='name',
            new_name='user_name',
        ),
    ]
