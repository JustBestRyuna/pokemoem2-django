"""pokemoem2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dex_api.views import PokedexList, PokedexDetail, AbilitiesList, AbilitiesDetail, \
                          ItemsList, ItemsDetail, MovesList, MovesDetail, \
                          NaturesList, NaturesDetail, TypechartList, TypechartDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dex_api/pokedex/', PokedexList.as_view(), name='pokedex'),
    path('dex_api/pokedex/<slug:index>', PokedexDetail.as_view(), name='pokedex'),
    path('dex_api/abilities/', AbilitiesList.as_view(), name='abilities'),
    path('dex_api/abilities/<slug:index>', AbilitiesDetail.as_view(), name='abilities'),
    path('dex_api/items/', ItemsList.as_view(), name='items'),
    path('dex_api/items/<slug:index>', ItemsDetail.as_view(), name='items'),
    path('dex_api/moves/', MovesList.as_view(), name='moves'),
    path('dex_api/moves/<slug:index>', MovesDetail.as_view(), name='moves'),
    path('dex_api/natures/', NaturesList.as_view(), name='natures'),
    path('dex_api/natures/<slug:index>', NaturesDetail.as_view(), name='natures'),
    path('dex_api/typechart/', TypechartList.as_view(), name='typechart'),
    path('dex_api/typechart/<slug:index>', TypechartDetail.as_view(), name='typechart'),
]
