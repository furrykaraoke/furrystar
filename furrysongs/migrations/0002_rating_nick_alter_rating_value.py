# Generated by Django 4.2.5 on 2023-09-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furrysongs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='nick',
            field=models.CharField(default='Anonymus', max_length=60),
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
