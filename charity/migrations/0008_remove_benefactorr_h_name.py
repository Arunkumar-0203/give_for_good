# Generated by Django 3.0.5 on 2021-11-09 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0007_auto_20211110_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benefactorr',
            name='h_name',
        ),
    ]