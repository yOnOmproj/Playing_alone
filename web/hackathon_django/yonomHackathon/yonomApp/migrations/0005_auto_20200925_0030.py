# Generated by Django 3.1.1 on 2020-09-24 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yonomApp', '0004_auto_20200924_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_data',
            name='bingo1',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo2',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo3',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo4',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo5',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo6',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo7',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo8',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.AlterField(
            model_name='game_data',
            name='bingo9',
            field=models.ImageField(default=0, upload_to='bingo'),
        ),
        migrations.CreateModel(
            name='Bangkoker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bangkoker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]