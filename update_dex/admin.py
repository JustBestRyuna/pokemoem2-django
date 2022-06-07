from django.contrib import admin

from .models import Pokedex


class PokedexAdmin(admin.ModelAdmin):
    list_display = ("name", "nameko",)


admin.site.register(Pokedex, PokedexAdmin)
