from itertools import zip_longest, combinations, product
import re

from django.db.models import F, Q, BooleanField, IntegerField, FloatField, CharField, TextField, JSONField
from django.db.models.expressions import RawSQL
from rest_framework import generics, filters

from update_dex.models import Pokedex, Abilities, Items, Moves, Natures, Typechart
from .serializers import PokedexSerializer, AbilitiesSerializer, ItemsSerializer, \
                         MovesSerializer, NaturesSerializer, TypechartSerializer

regex_number = re.compile('[0-9.]+')
regex_pokemon_name = re.compile('[가-힣a-zA-Z2]+')
regex_other_name = re.compile('[가-힣a-zA-Z0-9]+')


def filter_isnull(field, term):
    return Q(**{field + '__isnull': True})


def filter_numberfield(field, term):
    cur = Q()
    if dots := [i for i in re.finditer('[.]{2}', term)]:
        gte = term[:dots[0].start()].strip()
        lte = term[dots[0].end():].strip()
        if re.match(regex_number, gte):
            cur = Q(**{field + '__gte': float(gte)})
        if re.match(regex_number, lte):
            cur &= Q(**{field + '__lte': float(lte)})
    else:
        if re.match(regex_number, term):
            cur = Q(**{field: float(term)})
    return cur


def filter_textfield(field, term):
    if field.find('__isnull') > -1:
        return filter_isnull(field[:-8], term)
    if field.find('__notnull') > -1:
        return ~filter_isnull(field[:-9], term)
    if re.match(regex_other_name, term):
        return Q(**{field + '__icontains': term})


def filter_booleanfield(field, term):
    if term.lower() in ['y', 't']:
        cur = Q(**{field: True})
    elif term.lower() in ['n', 'f']:
        cur = Q(**{field: False})
    else:
        cur = Q(**{field: None})
    return cur


def filter_types_of_two(field, term):
    if field.find('count') > -1:
        column = field[:-7]
        return Q(**{column + '__in': RawSQL(
            f"""
            select {column} from pokedex where jsonb_array_length({column}) = %s
            """,
            params=[int(term)]
        )})
    else:
        return filter_textfield(field, term)


def filter_array_or_null(field, term):
    def filter_count(field, term):
        column = field[:-7]
        if int(term) == 0:
            return Q(**{column + '__in': RawSQL(
                f"""
                select {column} from pokedex where jsonb_typeof({column}) = 'null'
                """, params=[]
            )})
        else:
            return Q(**{column + '__in': RawSQL(
                f"""
                select {column} from (select * from pokedex where jsonb_typeof({column}) <> 'null') as pd
                where jsonb_array_length({column}) = %s
                """, params=[term]
            )})

    if field.find('count') > -1:
        cur = Q()
        if dots := [i for i in re.finditer('[.]{2}', term)]:
            gte = term[:dots[0].start()].strip()
            lte = term[dots[0].end():].strip()
            if not re.match(regex_number, gte):
                gte = 0
            if not re.match(regex_number, lte):
                lte = 50
            print(gte, lte)
            for i in range(int(gte), int(lte) + 1):
                cur |= filter_count(field, i)
        else:
            if re.match(regex_number, term):
                cur = filter_count(field, term)
        return cur
    else:
        return filter_textfield(field, term)


def filter_types(field, term):
    if field.find('eff') > -1:
        types = Typechart.objects.all()
        cur = Q(pk__in=[])

        def get_index_in_list(somelist):
            newlist = []
            for type in somelist:
                newlist.append(getattr(type, 'index').capitalize())
            return newlist

        neutral = get_index_in_list(list(types.filter(**{'damagetaken__' + term: 0})))
        effective = get_index_in_list(list(types.filter(**{'damagetaken__' + term: 1})))
        not_effective = get_index_in_list(list(types.filter(**{'damagetaken__' + term: 2})))
        no_effect = get_index_in_list(list(types.filter(**{'damagetaken__' + term: 3})))

        def eff__x4():
            cur = Q(pk__in=[])
            for type1, type2 in combinations(effective, 2):
                cur |= Q(types__contains=type1) & Q(types__contains=type2)
            return cur

        def eff__x2():
            cur = Q(pk__in=[])
            for efftype in effective:
                filter_for_efftype = Q(types__contains=efftype)
                for badtype in not_effective + no_effect:
                    filter_for_efftype &= ~Q(types__contains=badtype)
                cur |= filter_for_efftype
            return cur

        def eff__x1():
            cur = Q(pk__in=[])
            for efftype, badtype in product(effective, not_effective):
                cur |= Q(types__contains=efftype) & Q(types__contains=badtype)
            for type1, type2 in combinations(neutral, 2):
                cur |= Q(types__contains=type1) & Q(types__contains=type2)
            for type in neutral:
                cur |= filter_types_of_two('types__count', 1) & Q(types__contains=type)
            return cur

        def eff__l2():
            cur = Q(pk__in=[])
            for efftype in not_effective:
                filter_for_efftype = Q(types__contains=efftype)
                for badtype in effective + no_effect:
                    filter_for_efftype &= ~Q(types__contains=badtype)
                cur |= filter_for_efftype
            return cur

        def eff__l4():
            cur = Q(pk__in=[])
            for type1, type2 in combinations(not_effective, 2):
                cur |= Q(types__contains=type1) & Q(types__contains=type2)
            return cur

        def eff__x0():
            cur = Q(pk__in=[])
            for type in no_effect:
                cur |= Q(types__contains=type)
            return cur

        if field == 'types__eff__x4':
            cur |= eff__x4()
        if field == 'types__eff__x2':
            cur |= eff__x4() | eff__x2()
        if field == 'types__eff__x1':
            cur |= eff__x4() | eff__x2() | eff__x1()
        if field == 'types__eff__l1':
            cur |= eff__x0() | eff__l4() | eff__l2() | eff__x1()
        if field == 'types__eff__l2':
            cur |= eff__x0() | eff__l4() | eff__l2()
        if field == 'types__eff__l4':
            cur |= eff__x0() | eff__l4()
        if field == 'types__eff__x0':
            cur |= eff__x0()
        return cur
    return filter_types_of_two(field, term)


def filter_basestats(field, term):
    if field.find('any') > -1:
        return filter_numberfield('basestats__hp', term) \
               | filter_numberfield('basestats__atk', term) \
               | filter_numberfield('basestats__def', term) \
               | filter_numberfield('basestats__spa', term) \
               | filter_numberfield('basestats__spd', term) \
               | filter_numberfield('basestats__spe', term)
    if field.find('all') > -1:
        return filter_numberfield('basestats__hp', term) \
               & filter_numberfield('basestats__atk', term) \
               & filter_numberfield('basestats__def', term) \
               & filter_numberfield('basestats__spa', term) \
               & filter_numberfield('basestats__spd', term) \
               & filter_numberfield('basestats__spe', term)
    if field.find('total') > -1:
        if dots := [i for i in re.finditer('[.]{2}', term)]:
            gte = term[:dots[0].start()].strip()
            lte = term[dots[0].end():].strip()
            if not re.match(regex_number, gte):
                gte = 6
            if not re.match(regex_number, lte):
                lte = 255 * 6
        else:
            gte, lte = term, term
        return Q(**{'basestats__in': RawSQL(
            f"""
            select basestats from pokedex
            where cast(basestats->>'hp' as int) + cast(basestats->>'atk' as int)
             + cast(basestats->>'def' as int) + cast(basestats->>'spa' as int)
             + cast(basestats->>'spd' as int) + cast(basestats->>'spe' as int) between %s and %s
            """, params=[int(gte), int(lte)]
        )})
    return filter_numberfield(field, term)


def filter_abilities(field, term):
    def filter_count(term):
        if term == 1:
            return Q(abilities__in=RawSQL(
                """
                select abilities from pokedex
                where not (abilities ? '1' or abilities ? 'H')
                """, params=()
            ))
        if term == 2:
            return Q(abilities__in=RawSQL(
                """
                select abilities from pokedex
                where (abilities ? '1' or abilities ? 'H') and not (abilities ? '1' and abilities ? 'H')
                """, params=()
            ))
        if term == 3:
            return Q(abilities__in=RawSQL(
                """
                select abilities from pokedex
                where abilities ? '1' and abilities ? 'H'
                """, params=()
            ))

    if field.find('count') > -1:
        cur = Q()
        if dots := [i for i in re.finditer('[.]{2}', term)]:
            gte = term[:dots[0].start()].strip()
            lte = term[dots[0].end():].strip()
            if not re.match(regex_number, gte):
                gte = 1
            if not re.match(regex_number, lte):
                lte = 3
            for i in range(int(gte), int(lte) + 1):
                cur |= filter_count(i)
        else:
            if re.match(regex_number, term):
                cur = filter_count(term)
        return cur
    else:
        return Q(abilities__in=RawSQL(
            """
            select abilities from pokedex
            where abilities->>'0' = %s or abilities->>'1' = %s or abilities->>'H' = %s
            """, params=(term, term, term)
        ))


def filter_learnset(field, term):
    def filter_gen(field, term):
        move_name = field[10:]
        return Q(**{'learnset__in': RawSQL(
            f"""
            select learnset from (select * from pokedex where jsonb_typeof(learnset) <> 'null') as pd
            where learnset @? '$.{move_name} ? (@ like_regex "{term}[LMETSR]")'
            """, params=()
        )})

    def filter_single_move(field, term):
        cur = Q()
        if dots := [i for i in re.finditer('[.]{2}', term)]:
            gte = term[:dots[0].start()].strip()
            lte = term[dots[0].end():].strip()
            if not re.match(regex_number, gte):
                gte = 1
            if not re.match(regex_number, lte):
                lte = 9
            print(gte, lte)
            for i in range(int(gte), int(lte) + 1):
                cur |= filter_gen(field, i)
        else:
            if re.match(regex_number, term):
                cur = filter_gen(field, term)
        return cur

    if field.find('mult') > -1:
        q_object = Q()
        query_filters = PokemoemFilterBackend().get_query_filters(MovesList)
        filter_regexes = [query_filter for query_filter in query_filters.keys()]
        # Make a regex that matches if any of our regexes match.
        combined_regex = "(" + ")|(".join(filter_regexes) + ")"
        parts = field[15:-1].split(',')

        for i, part in enumerate(parts):
            # Get the Q object.
            cur = Q()
            if match := [i for i in re.finditer('=', part)]:
                field = part[:match[0].start()].strip()
                if not re.match(combined_regex, field):
                    continue
                if dunder := [i for i in re.finditer('[_]{2}', field)]:
                    field_cover = field[:dunder[0].start()]
                else:
                    field_cover = field
                field_class = query_filters[field_cover]
                inside_term = part[match[0].end():].strip()

                cur = Q()
                if inside_term == '*':
                    cur = Q(**{field + '__in': RawSQL(f"""
                        select {field} from moves where jsonb_typeof({field}) <> 'null'""", params=[])})
                elif isinstance(field_class, (IntegerField, FloatField)):
                    cur = filter_numberfield(field, inside_term)
                elif isinstance(field_class, (CharField, TextField)):
                    cur = filter_textfield(field, inside_term)
                elif isinstance(field_class, BooleanField):
                    cur = filter_booleanfield(field, inside_term)
                elif isinstance(field_class, JSONField):
                    jsonfield_method = getattr(MovesList, 'jsonfield_method', None)
                    method = jsonfield_method.get(field_cover, lambda x, y: Q())
                    cur = method(field, inside_term)
            q_object &= cur

        moves = Moves.objects.all().filter(q_object)
        print(moves)
        cur = Q(pk__in=[])
        for move in list(moves):
            newfield = 'learnset__' + move.index

            cur |= filter_single_move(newfield, term)
        return cur

def filter_fling(field, term):
    if field.find('basepower') > -1:
        return filter_numberfield(field, term)
    elif field.find('status') > -1:
        return filter_textfield(field, term)
    else:
        return Q()


def filter_naturalgift(field, term):
    if field.find('basepower') > -1:
        return filter_numberfield(field, term)
    elif field.find('type') > -1:
        return filter_textfield(field, term)
    else:
        return Q()


def filter_secondary(field, term):
    if field.find('chance') > -1:
        cur = filter_numberfield('secondary__chance', term)
        if dots := [i for i in re.finditer('[.]{2}', term)]:
            gte = term[:dots[0].start()].strip()
            lte = term[dots[0].end():].strip()
            if not re.match(regex_number, gte):
                gte = 5
            if not re.match(regex_number, lte):
                lte = 50
        else:
            gte, lte = term, term
        if gte <= 10 <= lte:
            cur |= filter_numberfield('secondaries__0__chance', 10)
    else:
        cur = filter_textfield(field, term)
        if term == 'flinch':
            cur |= filter_textfield('secondaries__1__volatileStatus', 'flinch')
    return cur


def filter_drain(field, term):
    if term == 50:
        return Q(drain__0=1)
    elif term == 75:
        return Q(drain__0=3)
    else:
        return Q()


def filter_zmove(field, term):
    cur = filter_numberfield(field + '__basePower', term)

    def find_by_basepower(gte, lte):
        cur = Q()
        zmove_isnull = Q(zmove__in=RawSQL("""
                            select zmove from moves where jsonb_typeof(zmove) = 'null'
                            """, params=[]))
        if 100 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower__lte=55)
        if 120 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower__gte=60, basepower__lte=65)
        if 140 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower__gte=70, basepower__lte=75)
        if 160 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower__gte=80, basepower__lte=85)
        if 175 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower__gte=90, basepower__lte=95)
        if 180 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower=100)
        if 185 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower=110)
        if 190 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower=120)
        if 195 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower=130)
        if 200 in range(gte, lte):
            cur |= zmove_isnull & Q(basepower__gte=140)
        return cur

    if dots := [i for i in re.finditer('[.]{2}', term)]:
        gte = term[:dots[0].start()].strip()
        lte = term[dots[0].end():].strip()
        if not re.match(regex_number, gte):
            gte = 100
        if not re.match(regex_number, lte):
            lte = 200
        cur |= find_by_basepower(int(gte), int(lte))
    else:
        if re.match(regex_number, term):
            cur |= find_by_basepower(int(term), int(term))
    return cur


def filter_maxmove(field, term):
    cur = filter_numberfield(field + '__basePower', term)

    def find_by_basepower(gte, lte):
        cur = Q()
        maxmove_isnull = Q(maxmove__in=RawSQL("""
            select maxmove from moves where jsonb_typeof(maxmove) = 'null'
            """, params=[]))
        if gte <= 70 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower__lte=40)
        if gte <= 75 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower=50)
        if gte <= 80 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower__gte=55, basepower__lte=60)
        if gte <= 85 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower__gte=65, basepower__lte=70)
        if gte <= 90 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower__gte=75, basepower__lte=100)
            cur |= maxmove_isnull & Q(basepower__lte=40) & ~Q(type__in=["Fighting", "Poison"])
        if gte <= 95 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower__gte=110, basepower__lte=140)
        if gte <= 100 <= lte:
            cur |= maxmove_isnull & Q(type__in=["Fighting", "Poison"], basepower__gte=150)
            cur |= maxmove_isnull & Q(basepower=50) & ~Q(type__in=["Fighting", "Poison"])
        if gte <= 110 <= lte:
            cur |= maxmove_isnull & Q(basepower__gte=55, basepower__lte=60) & ~Q(type__in=["Fighting", "Poison"])
        if gte <= 120 <= lte:
            cur |= maxmove_isnull & Q(basepower__gte=65, basepower__lte=70) & ~Q(type__in=["Fighting", "Poison"])
        if gte <= 130 <= lte:
            cur |= maxmove_isnull & Q(basepower__gte=75, basepower__lte=100) & ~Q(type__in=["Fighting", "Poison"])
        if gte <= 140 <= lte:
            cur |= maxmove_isnull & Q(basepower__gte=110, basepower__lte=140) & ~Q(type__in=["Fighting", "Poison"])
        if gte <= 150 <= lte:
            cur |= maxmove_isnull & Q(basepower__gte=150) & ~Q(type__in=["Fighting", "Poison"])
        return cur

    if dots := [i for i in re.finditer('[.]{2}', term)]:
        gte = term[:dots[0].start()].strip()
        lte = term[dots[0].end():].strip()
        if not re.match(regex_number, gte):
            gte = 70
        if not re.match(regex_number, lte):
            lte = 150
        cur |= find_by_basepower(int(gte), int(lte))
    else:
        if re.match(regex_number, term):
            cur |= find_by_basepower(int(term), int(term))
    print(cur)
    return cur


def filter_recoil(field, term):
    if term == 50:
        return Q(recoil__1=2)
    elif term == 33:
        return Q(recoil__1=100)
    elif term == 25:
        return Q(recoil__1=4)
    else:
        return Q()


def filter_multihit(field, term):
    if term == 5:
        return Q(multihit__1=term)
    else:
        return Q(multihit=term)


def filter_ismax(field, term):
    if term == 'true':
        return Q(ismax=True)
    elif term == '':
        return Q(ismax__notnull=True)
    else:
        return Q(ismax=term)


def filter_heal(field, term):
    if term == 50:
        return Q(heal__1=2)
    elif term == 25:
        return Q(heal__1=4)
    else:
        return Q()


def filter_nometronome(field, term):
    metronome_list = Moves.objects.get(name='Metronome').nometronome
    return Q(name__in=metronome_list)


class PokemoemFilterBackend(filters.BaseFilterBackend):
    def get_query_filters(self, view, **kwargs):
        """
        Get filters based on the view's filter_fields.
        """
        fields = getattr(view, 'filter_fields', None)
        query_filters = {field.name: field for field in fields} | {**kwargs}
        return query_filters

    def filter_queryset(self, request, queryset, view):
        """
        Filter terms are set by a ?query=... query parameter.
        """
        query_filters = self.get_query_filters(view)
        filter_regexes = [query_filter for query_filter in query_filters.keys()]
        # Make a regex that matches if any of our regexes match.
        combined_regex = "(" + ")|(".join(filter_regexes) + ")"

        params = request.query_params.get('query', '')
        params = params.replace('\x00', '')  # strip null characters
        print(params)
        if params == '':
            return queryset;

        ops = [-1] + [i.start() for i in re.finditer('[+|~]', params)]
        parts = [params[i+1:j].strip() for i, j in zip_longest(ops, ops[1:])]
        print(ops, parts)

        q_object = Q()

        for i, part in enumerate(parts):
            op = params[ops[i]]

            # Get the Q object.
            cur = Q()
            if not re.findall('[:.]', part) and re.match(regex_pokemon_name, part):
                cur = Q(name__iexact=part) | Q(nameko__iexact=part)

            elif match := [i for i in re.finditer(':', part)]:
                field = part[:match[0].start()].strip()
                if not re.match(combined_regex, field):
                    continue
                if dunder := [i for i in re.finditer('[_]{2}', field)]:
                    field_cover = field[:dunder[0].start()]
                else:
                    field_cover = field
                field_class = query_filters[field_cover]
                term = part[match[0].end():].strip()
                print(field_class, term)

                cur = Q()
                if term == '*':
                    cur = Q(**{field + '__isnull': False})
                elif isinstance(field_class, (IntegerField, FloatField)):
                    cur = filter_numberfield(field, term)
                elif isinstance(field_class, (CharField, TextField)):
                    cur = filter_textfield(field, term)
                elif isinstance(field_class, BooleanField):
                    cur = filter_booleanfield(field, term)
                elif isinstance(field_class, JSONField):
                    jsonfield_method = getattr(view, 'jsonfield_method', None)
                    method = jsonfield_method.get(field_cover, lambda x, y: Q())
                    cur = method(field, term)

            if op == '+':
                q_object = q_object & cur
            elif op == '|':
                q_object = q_object | cur
            else:
                q_object = q_object & ~cur

        return queryset.filter(q_object)


class PokedexList(generics.ListAPIView):
    queryset = Pokedex.objects.all().order_by('formtuple')
    serializer_class = PokedexSerializer
    filter_backends = [PokemoemFilterBackend]
    filter_fields = Pokedex._meta.fields

    jsonfield_method = {
        'types': filter_types,  # text array
        'genderratio': filter_numberfield,  # text(M/F), float dict
        'basestats': filter_basestats,  # text, int dict
        'abilities': filter_abilities,  # text(0/1/H), text dict
        'evos': filter_array_or_null,  # text array
        'egggroups': filter_types_of_two,  # text array
        'otherformes': filter_array_or_null,  # text array
        'formeorder': filter_array_or_null,  # text array
        'tags': filter_array_or_null,  # text array
        'cosmeticformes': filter_array_or_null,  # text array
        'formtuple': filter_types_of_two,  # int array
        'learnset': filter_learnset,  # text, array(text) dict
    }


class PokedexDetail(generics.RetrieveAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer
    lookup_field = 'name'


class AbilitiesList(generics.ListAPIView):
    queryset = Abilities.objects.all()
    serializer_class = AbilitiesSerializer
    filter_backends = [PokemoemFilterBackend]
    filter_fields = Abilities._meta.fields


class AbilitiesDetail(generics.RetrieveAPIView):
    queryset = Abilities.objects.all()
    serializer_class = AbilitiesSerializer
    lookup_field = 'name'


class ItemsList(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    filter_backends = [PokemoemFilterBackend]
    filter_fields = Items._meta.fields

    jsonfield_method = {
        'itemuser': filter_array_or_null,  # text array
        'fling': filter_fling,  # text, text/int dict
        'boosts': filter_numberfield,  # text, int dict
        'naturalgift': filter_naturalgift,  # text, text/int dict
    }


class ItemsDetail(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    lookup_field = 'name'


class MovesList(generics.ListAPIView):
    queryset = Moves.objects.all()
    serializer_class = MovesSerializer
    filter_backends = [PokemoemFilterBackend]
    filter_fields = Moves._meta.fields

    jsonfield_method = {
        'flags': filter_booleanfield,  # text, bool dict
        'secondary': filter_secondary,  # text, int/text dict
        'drain': filter_drain,  # int array
        'boosts': filter_numberfield,  # text, int dict
        'zmove': filter_zmove,  # text, int/text dict
        'multihit': filter_multihit,  # int array or int
        'self': filter_textfield,  # text, text dict
        'selfswitch': filter_isnull,  # bool or text, text dict
        'ignoreimmunity': filter_booleanfield,  # bool or text, bool dict
        'maxmove': filter_maxmove,  # text, int dict
        'recoil': filter_recoil,  # int array
        'selfboost': filter_numberfield,  # text, text, int dict
        'damage': filter_textfield,  # int or text
        'secondaries': filter_secondary,  # dict array (of 2)
        'ohko': filter_isnull,  # bool or text
        'ismax': filter_ismax,  # bool or text
        'heal': filter_heal,   # int array
        'nometronome': filter_nometronome,  # text array
    }


class MovesDetail(generics.RetrieveAPIView):
    queryset = Moves.objects.all()
    serializer_class = MovesSerializer
    lookup_field = 'name'


class NaturesList(generics.ListAPIView):
    queryset = Natures.objects.all()
    serializer_class = NaturesSerializer
    filter_backends = [PokemoemFilterBackend]
    filter_fields = Natures._meta.fields


class NaturesDetail(generics.RetrieveAPIView):
    queryset = Natures.objects.all()
    serializer_class = NaturesSerializer
    lookup_field = 'name'


class TypechartList(generics.ListAPIView):
    queryset = Typechart.objects.all()
    serializer_class = TypechartSerializer
    filter_backends = [PokemoemFilterBackend]
    filter_fields = Typechart._meta.fields

    jsonfield_method = {
        'damagetaken': filter_numberfield,
        'hpivs': filter_isnull,
    }


class TypechartDetail(generics.RetrieveAPIView):
    queryset = Typechart.objects.all()
    serializer_class = TypechartSerializer
    lookup_field = 'name'
