# Generated by Django 3.0.5 on 2021-05-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210505_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.CharField(choices=[('game', 'Game'), ('foss', 'FOSS'), ('sec', 'Security'), ('devel', 'Development')], default=True, max_length=255),
        ),
    ]