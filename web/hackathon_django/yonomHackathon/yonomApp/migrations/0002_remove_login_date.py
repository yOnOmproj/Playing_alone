# Generated by Django 3.1.1 on 2020-09-24 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonomApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='date',
        ),
    ]