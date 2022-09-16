
import requests
import json
from jsonschema import validate
import jsonpath
import random

baseUrlAuthentication = "https://api.kraken.com/0/private/GetWebSocketsToken"
baseUrlAssets = "https://api.kraken.com/0/public/Assets"



def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return str(random.randint(lower, upper))

def test_auth() :
    path = "api/register"
    response = requests.post(url=baseUrlAuthentication)
    responseJson = json.loads(response.text)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
         return response.json()
    assert response.status_code == 200
    #print(responseJson['token'])
    assert response.status_code == 200
    assert type(jsonpath.jsonpath(responseJson,'$.token')[0]) == str

def test_assets() :
    file = open('TestData/assets_schema.json',"r")
    response = requests.get(baseUrlAssets)
    responseJson = json.loads(response.text)
    #print(response.json())
    data = json.loads(file.read())
    schema = data
    is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    #is_valid = validator.validate(responseJson)
    try:
        validate(instance=responseJson, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message