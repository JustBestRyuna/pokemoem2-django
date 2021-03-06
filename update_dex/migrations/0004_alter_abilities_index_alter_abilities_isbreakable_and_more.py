# Generated by Django 4.0.4 on 2022-06-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update_dex', '0003_items_moves_natures_remove_abilities_name_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilities',
            name='index',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='isbreakable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='isnonstandard',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='ispermanent',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='namejp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='nameko',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onallybasepowerpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onallymodifyatkpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onallymodifyspdpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onanybasepowerpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onanyfaintpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onanyinvulnerabilitypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onanymodifyaccuracypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onbasepowerpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onbeforemovepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='oncriticalhit',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='ondamagepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='ondamaginghitorder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='ondragoutpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onfractionalpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onfractionalprioritypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifyaccuracypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifyatkpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifydefpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifymovepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifyspapriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifytypepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onmodifyweightpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onresidualorder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onresidualsuborder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onsourcebasepowerpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onsourcemodifyaccuracypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onsourcemodifyatkpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onsourcemodifydamagepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='onsourcemodifyspapriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='ontryeatitempriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='ontryhitpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='shortdesc',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='abilities',
            name='suppressweather',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='forcedforme',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ignoreklutz',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='index',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='items',
            name='isberry',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ischoice',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='isgem',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='isnonstandard',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ispokeball',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='itemuser',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='megaevolves',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='megastone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='naturalgift',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onaftermovesecondarypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onaftermovesecondaryselfpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onaftersetstatuspriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onattractpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onbasepowerpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onboostpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ondamagepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ondamaginghitorder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ondrive',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='oneat',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onfractionalpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onfractionalprioritypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmemory',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmodifyaccuracypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmodifyatkpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmodifydefpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmodifymovepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmodifyspapriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onmodifyspdpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onnegateimmunity',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onplate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onresidualorder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onresidualsuborder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='onsourcemodifyaccuracypriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ontakeitem',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ontrappokemonpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='ontryhealpriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='shortdesc',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='zmove',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='zmovefrom',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='zmovetype',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='basepower',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='breaksprotect',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='contesttype',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='critratio',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='forceswitch',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='hascrashdamage',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='ignoreability',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='ignoredefensive',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='ignoreevasion',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='ignoreimmunity',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='index',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='moves',
            name='isfuturemove',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='ismax',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='isnonstandard',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='isz',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='maxmove',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='mindblownrecoil',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='nometronome',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='nonghosttarget',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='noppboosts',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='nosketch',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='ondamagepriority',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='overridedefensivestat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='overrideoffensivepokemon',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='overrideoffensivestat',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='pressuretarget',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='pseudoweather',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='realmove',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='selfboost',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='selfswitch',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='shortdesc',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='sidecondition',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='sleepusable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='slotcondition',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='smarttarget',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='stallingmove',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='stealsboosts',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='strugglerecoil',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='thawstarget',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='trackstarget',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='volatilestatus',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='willcrit',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moves',
            name='zmove',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='natures',
            name='namejp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='natures',
            name='nameko',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='baseforme',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='basespecies',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='basestats',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='battleonly',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='cangigantamax',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='canhatch',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='cannotdynamax',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='changesfrom',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='cosmeticformes',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='egggroups',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='eventdata',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='eventonly',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='evocondition',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='evoitem',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='evolevel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='evomove',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='evotype',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='formeorder',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='formtuple',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='genderratio',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='iconfilename',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='index',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='isnonstandard',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='maxhp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='nameko',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='nameliberty',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='namenouthuca',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='otherformes',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='requiredability',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='requireditem',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='requireditems',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedex',
            name='requiredmove',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
