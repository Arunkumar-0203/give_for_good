# Generated by Django 3.0.5 on 2021-11-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0011_auto_20211111_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefactorr',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
