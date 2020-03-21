'''
Fetch Pokemon list from endpoint on daily basis
'''

from django_extensions.management.jobs import DailyJob
import logging
import requests
import json

logger = logging.getLogger(__name__)
# create file handler which logs even debug messages
logging.basicConfig(filename='spam.log')
logger.debug('This is a debug message')


def getPokemonList():
    url = "https://pokeapi.co/api/v2/pokemon-species/"

    response = requests.request("GET", url)

    try:
        data = json.loads(response.text)["results"]

        pokemonList = [{"name": i["name"], "description": getPokemonDetail(i["url"])} for i in data]
        return pokemonList

    except:
        return {"error": "no results from %s" % url}





def getPokemonDetail(url, lang = "en", translate = False):

    response = requests.request("GET", url)

    try:
        data = json.loads(response.text)["flavor_text_entries"]


        pokemonDescriptions = {
            i["language"]["name"]: (translate(i["flavor_text"]) if translate else i["flavor_text"])
            for i in data
            }

        if lang in (pokemonDescriptions.keys()):
            return pokemonDescriptions[lang]
        else:
            return {"error": "%s not available" % lang}
    
    except:
        return {"error": "no flavor_text_entries from %s" % url}

    


def translate(text):

    '''
    Cannot make more than 5 requests within an hour. Need a handler here
    '''

    url = "https://api.funtranslations.com/translate/shakespeare"

    payload = {'text': text}
    files = [

    ]
    headers = {
    'Content-Type': 'multipart/form-data;'
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files)

    try:
        return json.loads(response.text)["contents"]["translated"]
    
    except:
        return text





def pushPokemonDetailToDb(pokemonData):

    url = "http://127.0.0.1:8000/pokemon/"

    payload = json.dumps(pokemonData)
    headers = {
    'Content-Type': 'application/json'
    }



    # create new record if not exists
    response = requests.request("POST", url, headers=headers, data = payload)

    if response.status_code == 400: 
    # update the existing one otherwise
        response = requests.request("PUT", url, headers=headers, data = payload)

    

class Job(DailyJob):

    help = 'Fetch data from Pokemon v2'

    def execute(self):
        

        for pokemonData in getPokemonList():
            pushPokemonDetailToDb(pokemonData)
