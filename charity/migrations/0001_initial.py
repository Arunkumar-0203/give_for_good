# Generated by Django 3.0.5 on 2021-11-05 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=50)),
                ('type1', models.CharField(max_length=50)),
                ('status', models.CharField(default=0, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('status', models.CharField(default=1, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('proof', models.FileField(null=True, upload_to='', verbose_name='file/')),
                ('qualification', models.CharField(max_length=50)),
                ('phone', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request_Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, null=True)),
                ('members', models.CharField(max_length=50, null=True)),
                ('product_need', models.CharField(max_length=300, null=True)),
                ('benfi_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charity.Beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiary_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, null=True)),
                ('reply', models.CharField(max_length=50)),
                ('status', models.CharField(default=0, max_length=100)),
                ('beneficiary_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charity.Beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='Benefactorr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('phone', models.IntegerField(null=True)),
                ('h_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('type1', models.CharField(max_length=50)),
                ('status', models.CharField(default=0, max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Benefactor_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, null=True)),
                ('reply', models.CharField(max_length=50)),
                ('status', models.CharField(default=0, max_length=100)),
                ('benefactor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charity.Benefactorr')),
            ],
        ),
    ]
