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


##### Force fetch

Otherwise this is a scheduled job

```
python manage.py runjobs daily
```


### Workflow
Pokemon sent in the request will be checked against the local database first. If not found, a renewal will be 

# To do list (automated testing)
- create/update new pokemon api testing
- add logging in daily job
- automated test for daily fetch
- redefine exceptions in daily job