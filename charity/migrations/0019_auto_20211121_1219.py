# Generated by Django 3.0.5 on 2021-11-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0018_auto_20211121_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer_reg',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
