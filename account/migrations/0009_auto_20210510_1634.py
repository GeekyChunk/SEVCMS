# Generated by Django 3.0.5 on 2021-05-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210510_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='userid',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
