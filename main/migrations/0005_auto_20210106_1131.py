# Generated by Django 3.1 on 2021-01-06 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210106_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='website_name',
            field=models.CharField(default='DEFAULT VALUE', max_length=50, unique=True),
        ),
    ]
