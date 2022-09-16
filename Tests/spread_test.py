
import requests
import json
from jsonschema import validate
import jsonpath
import random

baseUrlAuthentication = "https://api.kraken.com/0/private/GetWebSocketsToken"
baseUrlSpread = "https://api.kraken.com/0/public/Spread?pair=XBTUSD"


def test_spread() :
    file = open('TestData/spread_schema.json',"r")
    response = requests.get(baseUrlSpread)
    responseJson = json.loads(response.text)
    #print(response.json())
    data = json.loads(file.read())
    schema = data
    #is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    assert response.status_code == 200
    try:
        validate(instance=responseJson, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message
    #is_valid = validator.validate(responseJson)
    