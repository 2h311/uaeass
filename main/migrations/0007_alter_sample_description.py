# Generated by Django 3.2.7 on 2021-11-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_sample_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]