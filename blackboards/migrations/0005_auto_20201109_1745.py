# Generated by Django 3.0 on 2020-11-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackboards', '0004_auto_20201031_1326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listtableitem',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterField(
            model_name='listtable',
            name='table_name',
            field=models.CharField(max_length=100),
        ),
    ]