# Generated by Django 3.1.4 on 2021-03-14 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thebible', '0002_auto_20210128_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bibletitles',
            options={'ordering': ['title'], 'verbose_name': '성경 제목', 'verbose_name_plural': '성경 제목'},
        ),
    ]
