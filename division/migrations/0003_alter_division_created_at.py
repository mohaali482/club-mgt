# Generated by Django 3.2 on 2022-05-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0002_auto_20220510_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
