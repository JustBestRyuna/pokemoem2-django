# Generated by Django 4.0.4 on 2022-06-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_dex', '0004_alter_abilities_index_alter_abilities_isbreakable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typechart',
            fields=[
                ('index', models.TextField(primary_key=True, serialize=False)),
                ('damagetaken', models.JSONField(blank=True, null=True)),
                ('hpivs', models.JSONField(blank=True, null=True)),
                ('hpdvs', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'typechart',
            },
        ),
        migrations.RenameField(
            model_name='items',
            old_name='name_jp',
            new_name='namejp',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='name_ko',
            new_name='nameko',
        ),
        migrations.RenameField(
            model_name='moves',
            old_name='name_jp',
            new_name='namejp',
        ),
        migrations.RenameField(
            model_name='moves',
            old_name='name_ko',
            new_name='nameko',
        ),
    ]