
from urllib import request
import requests
import json
from jsonschema import validate
import jsonpath
import random

tradeName = "XBTUSD"
baseUrlAuthentication = "https://api.kraken.com/0/private/GetWebSocketsToken"
baseUrlSpread = "https://api.kraken.com/0/public/Trades?pair="+tradeName


def test_spread() :
    file = open('TestData/trades_schema.json',"r")
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
    
def test_there_is_no_trade_name_this_is_valid_failing() :
    #file = open('TestData/trades_schema.json',"r")
    response = requests.get(baseUrlSpread)
    responseJson = json.loads(response.text)
    responseStr = json.dumps(responseJson)
    #print(responseStr)
    #data = json.loads(file.read())
    #schema = data
    #is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    assert response.status_code == 200
    assert (tradeName in responseStr), "Given Trade name: "+tradeName+" is not in Response"
    #assert jsonpath.jsonpath(responseJson,'$.result')[0] == "XBTUSD"
   
   
