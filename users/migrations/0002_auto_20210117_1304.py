# Generated by Django 3.1.4 on 2021-01-17 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thebible', '0002_auto_20210117_1255'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlikeverses',
            name='user_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlikeverses',
            name='verse_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='thebible.bibleverses'),
        ),
    ]
