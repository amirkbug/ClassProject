# Generated by Django 4.2 on 2025-01-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='content',
            field=models.TextField(default='good reporter'),
        ),
    ]
