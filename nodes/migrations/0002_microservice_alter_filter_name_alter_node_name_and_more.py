# Generated by Django 4.0.4 on 2022-05-27 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Microservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='filter',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='microservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodes.microservice'),
        ),
    ]
