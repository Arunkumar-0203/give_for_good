# Generated by Django 3.0.5 on 2021-11-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0009_remove_benefactorr_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer_reg',
            name='address',
        ),
        migrations.AddField(
            model_name='volunteer_reg',
            name='City_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteer_reg',
            name='Home_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteer_reg',
            name='Street_Address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
