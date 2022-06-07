# Generated by Django 4.0.4 on 2022-05-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_dex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('index', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name_en', models.TextField(blank=True, null=True)),
                ('name_jp', models.TextField(blank=True, null=True)),
                ('name_ko', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'abilities',
            },
        ),
    ]
