# Generated by Django 3.1.4 on 2021-01-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thebible', '0002_auto_20210117_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibleverses',
            name='verse',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='내용'),
        ),
    ]