# Generated by Django 4.0.4 on 2022-05-28 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0008_filterbenchmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterbenchmark',
            name='filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benchmarks', to='nodes.filter'),
        ),
    ]
