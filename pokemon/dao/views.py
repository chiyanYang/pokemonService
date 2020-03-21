from django.shortcuts import render

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
        pokemons = Pokemon.objects.filter(pk=pk)
        serializer = PokemonSerializer(pokemons, many = True)

        return Response(serializer.data)

    # create a new pokemon
    def post(self, request):
        '''

        '''
        data = JSONParser().parse(request)

        serializer = PokemonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
