# Generated by Django 2.1 on 2018-10-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0012_auto_20181023_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='notes',
            field=models.CharField(max_length=4500),
        ),
    ]
