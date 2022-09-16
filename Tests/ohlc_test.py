
import requests
import json
from jsonschema import validate
import jsonpath
import random

baseUrlAuthentication = "https://api.kraken.com/0/private/GetWebSocketsToken"
baseUrlOhlc = "https://api.kraken.com/0/public/OHLC?pair=XBTUSD"
params= {'interval': 15}

def test_ohlc() :
    file = open('TestData/ohlc_schema.json',"r")
    response = requests.get(baseUrlOhlc,)
    responseJson = json.loads(response.text)
    responseStr = json.dumps(responseJson)
   
    data = json.loads(file.read())
    schema = data
    #is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    assert response.status_code == 200
    #print(responseStr)
    try:
        validate(instance=responseJson, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        #print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message
    
def test_ohlc_with_params() :
    file = open('TestData/ohlc_schema.json',"r")
    response = requests.get(baseUrlOhlc,params=params)
    responseJson = json.loads(response.text)
    responseStr = json.dumps(responseJson)
   
    data = json.loads(file.read())
    schema = data
    #is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    assert response.status_code == 200
    #print(responseStr)
    