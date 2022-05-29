# Generated by Django 4.0.4 on 2022-05-28 14:24

from django.db import migrations, models
import nodes.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0006_staticimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticimage',
            name='image',
            field=models.ImageField(upload_to='static/', validators=[nodes.helpers.validate_uploading_image]),
        ),
    ]