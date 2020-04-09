# Generated by Django 3.0.3 on 2020-04-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawnumber', '0006_remove_number_drawingcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='drawingcode',
            field=models.TextField(default='2', max_length=20000),
        ),
        migrations.AlterField(
            model_name='number',
            name='drawing',
            field=models.CharField(max_length=1000),
        ),
    ]
