# Generated by Django 4.0.4 on 2022-05-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0011_filterbenchmark_request_json_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filterbenchmark',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
