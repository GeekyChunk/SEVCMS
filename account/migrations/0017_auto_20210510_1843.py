# Generated by Django 3.0.5 on 2021-05-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20210510_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='prof',
            field=models.ImageField(default='', upload_to='profs'),
        ),
    ]
