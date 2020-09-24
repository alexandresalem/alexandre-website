# Generated by Django 3.0.9 on 2020-09-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamef1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='f1prediction',
            name='position',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='f1prediction',
            name='probability',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]