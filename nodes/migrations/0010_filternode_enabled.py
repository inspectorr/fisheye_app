# Generated by Django 4.0.4 on 2022-05-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0009_alter_filterbenchmark_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='filternode',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
