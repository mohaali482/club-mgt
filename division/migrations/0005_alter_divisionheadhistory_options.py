# Generated by Django 3.2 on 2022-05-17 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0004_divisionhead_divisionheadhistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='divisionheadhistory',
            options={'verbose_name': 'Division Head History', 'verbose_name_plural': 'Division Head Histories'},
        ),
    ]