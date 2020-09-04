# Generated by Django 3.0.9 on 2020-08-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=100)),
                ('team', models.CharField(blank=True, max_length=100)),
                ('chassis', models.CharField(blank=True, max_length=100)),
                ('link', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1image', models.ImageField(upload_to='gamef1/')),
            ],
        ),
    ]
