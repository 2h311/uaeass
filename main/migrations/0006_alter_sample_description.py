# Generated by Django 3.2.7 on 2021-11-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211104_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
