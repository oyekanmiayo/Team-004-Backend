# Generated by Django 3.0.6 on 2020-05-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme_management', '0005_auto_20200523_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sme',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
