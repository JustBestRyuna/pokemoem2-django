# Generated by Django 4.0.4 on 2022-05-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokedex',
            fields=[
                ('index', models.TextField(primary_key=True, serialize=False)),
                ('num', models.BigIntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('types', models.TextField(blank=True, null=True)),
                ('genderratio', models.TextField(blank=True, db_column='genderRatio', null=True)),
                ('basestats', models.TextField(blank=True, db_column='baseStats', null=True)),
                ('abilities', models.TextField(blank=True, null=True)),
                ('heightm', models.FloatField(blank=True, null=True)),
                ('weightkg', models.FloatField(blank=True, null=True)),
                ('color', models.TextField(blank=True, null=True)),
                ('evos', models.TextField(blank=True, null=True)),
                ('egggroups', models.TextField(blank=True, db_column='eggGroups', null=True)),
                ('tier', models.TextField(blank=True, null=True)),
                ('prevo', models.TextField(blank=True, null=True)),
                ('evolevel', models.FloatField(blank=True, db_column='evoLevel', null=True)),
                ('otherformes', models.TextField(blank=True, db_column='otherFormes', null=True)),
                ('formeorder', models.TextField(blank=True, db_column='formeOrder', null=True)),
                ('cangigantamax', models.TextField(blank=True, db_column='canGigantamax', null=True)),
                ('basespecies', models.TextField(blank=True, db_column='baseSpecies', null=True)),
                ('forme', models.TextField(blank=True, null=True)),
                ('requireditem', models.TextField(blank=True, db_column='requiredItem', null=True)),
                ('isnonstandard', models.TextField(blank=True, db_column='isNonstandard', null=True)),
                ('changesfrom', models.TextField(blank=True, db_column='changesFrom', null=True)),
                ('evocondition', models.TextField(blank=True, db_column='evoCondition', null=True)),
                ('evotype', models.TextField(blank=True, db_column='evoType', null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('gen', models.FloatField(blank=True, null=True)),
                ('evoitem', models.TextField(blank=True, db_column='evoItem', null=True)),
                ('canhatch', models.TextField(blank=True, db_column='canHatch', null=True)),
                ('evomove', models.TextField(blank=True, db_column='evoMove', null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('baseforme', models.TextField(blank=True, db_column='baseForme', null=True)),
                ('cosmeticformes', models.TextField(blank=True, db_column='cosmeticFormes', null=True)),
                ('maxhp', models.FloatField(blank=True, db_column='maxHP', null=True)),
                ('requiredability', models.TextField(blank=True, db_column='requiredAbility', null=True)),
                ('battleonly', models.TextField(blank=True, db_column='battleOnly', null=True)),
                ('requiredmove', models.TextField(blank=True, db_column='requiredMove', null=True)),
                ('requireditems', models.TextField(blank=True, db_column='requiredItems', null=True)),
                ('cannotdynamax', models.TextField(blank=True, db_column='cannotDynamax', null=True)),
                ('formtuple', models.TextField(blank=True, db_column='formTuple', null=True)),
                ('nameko', models.TextField(blank=True, db_column='nameKo', null=True)),
                ('namenouthuca', models.TextField(blank=True, db_column='nameNouthuca', null=True)),
                ('nameliberty', models.TextField(blank=True, db_column='nameLiberty', null=True)),
                ('iconfilename', models.TextField(blank=True, db_column='iconFilename', null=True)),
            ],
            options={
                'db_table': 'pokedex',
            },
        ),
    ]
