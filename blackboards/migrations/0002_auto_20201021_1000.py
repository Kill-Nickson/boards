# Generated by Django 3.0 on 2020-10-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackboards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
