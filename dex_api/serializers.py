from rest_framework import serializers

from update_dex.models import Pokedex, Abilities, Items, Moves, Natures, Typechart


class PokedexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokedex
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PokedexSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']
        query_params = request.GET
        display_fields = query_params.get('display')
        if display_fields:
            self.Meta.fields = display_fields.split(',')


class AbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abilities
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AbilitiesSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']
        query_params = request.GET
        display_fields = query_params.get('display')
        if display_fields:
            self.Meta.fields = display_fields.split(',')


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ItemsSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']
        query_params = request.GET
        display_fields = query_params.get('display')
        if display_fields:
            self.Meta.fields = display_fields.split(',')


class MovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moves
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MovesSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']
        query_params = request.GET
        display_fields = query_params.get('display')
        if display_fields:
            self.Meta.fields = display_fields.split(',')


class NaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Natures
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NaturesSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']
        query_params = request.GET
        display_fields = query_params.get('display')
        if display_fields:
            self.Meta.fields = display_fields.split(',')


class TypechartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typechart
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TypechartSerializer, self).__init__(*args, **kwargs)
        request = self.context['request']
        query_params = request.GET
        display_fields = query_params.get('display')
        if display_fields:
            self.Meta.fields = display_fields.split(',')
