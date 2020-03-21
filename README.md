# pokemonService
pokemonService for children for TrueLayer


### Installation & Setup
- Create a virtual environment and `pip` install all required libraries using the following commands

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Once complete, you can check if django has been successfully installed
```
pip list
```


### Starting the server

```
cd ./pokemon
python manage.py runserver
```

### Endpoint

##### API detail view

```
http://127.0.0.1:8000/pokemon/<pokemonname>
```

##### Create pokemon (POST method)

```
http://127.0.0.1:8000/pokemon/
```

Sample request

```
{
    "name": "pokemonName",
    "description": "pokemonDescription"
}
```

cURL

```
curl --location --request POST 'http://127.0.0.1:8000/pokemon/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name": "api test",
	"description": "api desc"
}'
```