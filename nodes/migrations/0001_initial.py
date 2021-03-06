# Generated by Django 4.0.4 on 2022-05-28 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Microservice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('microservice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nodes.microservice')),
            ],
        ),
        migrations.CreateModel(
            name='FilterNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_nodes', to='nodes.filter')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nodes.node')),
            ],
            options={
                'unique_together': {('filter', 'node', 'index')},
            },
        ),
    ]
