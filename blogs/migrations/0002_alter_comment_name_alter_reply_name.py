# Generated by Django 4.2 on 2025-02-03 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profile_delete_personaltoken'),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
