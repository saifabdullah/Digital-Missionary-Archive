# Generated by Django 2.1 on 2018-09-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_auto_20180923_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='archive_number',
            field=models.CharField(max_length=300),
        ),
    ]
