# Generated by Django 3.0.5 on 2021-11-20 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0015_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_add',
            name='collected_date',
            field=models.DateField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product_add',
            name='volunteer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charity.volunteer_reg'),
        ),
    ]
