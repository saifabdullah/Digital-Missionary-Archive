# Generated by Django 2.1 on 2018-09-22 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('db', '0002_auto_20180912_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_upload', 'User has the ability to upload a document.'), ('can_search', 'Permissions of can_upload, plus the ability to search the archive database'), ('can_edit', 'Permissions of can_search, plus the ability to edit data')),
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
