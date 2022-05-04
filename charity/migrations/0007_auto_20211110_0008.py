# Generated by Django 3.0.5 on 2021-11-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_auto_20211106_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='benefactorr',
            name='image',
        ),
        migrations.RemoveField(
            model_name='beneficiary',
            name='address',
        ),
        migrations.AddField(
            model_name='benefactorr',
            name='City_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='benefactorr',
            name='Home_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='benefactorr',
            name='Street_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='city_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='home_Address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='beneficiary',
            name='street_Address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]