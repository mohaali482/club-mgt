# Generated by Django 3.2 on 2022-05-10 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('division', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='division.division')),
            ],
        ),
    ]
