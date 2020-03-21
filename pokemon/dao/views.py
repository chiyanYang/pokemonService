from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import PokemonSerializer
from .models import Pokemon

class PokemonAPIView(APIView):
    '''
    API to handle Pokemon serialized data
    '''

    # display the detail api view based on pokemon primary key
    def get(self, request, pk):
        # pokemons = Pokemon.objects.filter(pk=pk)

        pokemons = get_object_or_404(Pokemon.objects, pk = pk)
        serializer = PokemonSerializer(pokemons, many = False)

        return Response(serializer.data)

    # create a new pokemon
    def post(self, request):
        '''
        create/update a pokemon
        '''
        

        data = JSONParser().parse(request)
        serializer = PokemonSerializer(data = data)

        # create a new pokemon
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)

        return JsonResponse(serializer.errors, status = 400)


    # update an existing pokemon
    def put(self, request, pk):
        

        # get the instance
        pokemon = get_object_or_404(Pokemon.objects.all(), pk = pk)

        data = JSONParser().parse(request)
        serializer = PokemonSerializer(pokemon, data = data)

        # update the pokemon
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)