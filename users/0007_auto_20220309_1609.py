# Generated by Django 3.2.6 on 2022-03-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220309_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='wp_password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='wp_username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
