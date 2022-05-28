# Generated by Django 4.0.4 on 2022-05-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0002_alter_filternode_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='filternode',
            name='default_json_params',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='node',
            name='req_fields',
            field=models.TextField(default='image_base64,text,', help_text='\n    allowed comma-separated request json data field names, example:\n    image_base64,text,\n    '),
        ),
        migrations.AddField(
            model_name='node',
            name='res_fields',
            field=models.TextField(default='image_base64,text,', help_text='\n    allowed comma-separated response json data field names, example:\n    image_base64,text,\n    '),
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
