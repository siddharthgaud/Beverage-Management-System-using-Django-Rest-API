# Generated by Django 5.1 on 2024-11-07 06:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBVdrinksapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinksDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredients', models.CharField(max_length=200)),
                ('sweetner', models.CharField(max_length=200)),
                ('carbonation', models.CharField(max_length=200)),
                ('drinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='CBVdrinksapp.drinks')),
            ],
        ),
    ]
