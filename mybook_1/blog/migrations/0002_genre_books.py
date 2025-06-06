# Generated by Django 5.1.5 on 2025-01-30 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('Gener', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.genre')),
            ],
        ),
    ]
