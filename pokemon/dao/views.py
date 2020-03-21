from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PokemonSerializer
from .models import Pokemon

class PokemonView(APIView):
    '''
    API to display Pokemon serialized data
    '''

    def get(self, request, pk):
        pokemons = Pokemon.objects.filter(pk=pk)
        serializer = PokemonSerializer(pokemons, many = True)

        return Response(serializer.data)
