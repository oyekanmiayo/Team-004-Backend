# Generated by Django 3.0.6 on 2020-05-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sme_management', '0002_smeuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sme',
            name='org_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
