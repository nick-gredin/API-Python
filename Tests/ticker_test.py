
import requests
import json
from jsonschema import validate
import jsonpath
import random

tradeName = "XBTUSD"
baseUrlAuthentication = "https://api.kraken.com/0/private/GetWebSocketsToken"
baseUrlSpread = "https://api.kraken.com/0/public/Ticker?pair="+tradeName


def test_spread() :
    file = open('TestData/ticker_schema.json',"r")
    response = requests.get(baseUrlSpread)
    responseJson = json.loads(response.text)
    #print(response.json())
    data = json.loads(file.read())
    schema = data
    responseStr = json.dumps(responseJson)
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

def test_this_valid_tere_no_correct_trade_name() :
    response = requests.get(baseUrlSpread)
    responseJson = json.loads(response.text)
    responseStr = json.dumps(responseJson)
    #print(responseStr)
    assert response.status_code == 200
    assert (tradeName in responseStr), "Given Trade name: "+tradeName+" is not in Response"
    #assert jsonpath.jsonpath(responseJson,'$.result')[0] == "XBTUSD"
    
