# Generated by Django 3.1.6 on 2021-09-12 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0012_auto_20210911_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variationattribute',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.attribute'),
        ),
        migrations.AlterField(
            model_name='variationattribute',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templates.attributeoption'),
        ),
    ]