
import keyword
from pyparsing import results
import requests
import json
from jsonschema import validate
import jsonpath
import random

baseUrlAuthentication = "https://api.kraken.com/0/private/GetWebSocketsToken"
baseUrlBook = "https://api.kraken.com/0/public/Depth?pair=XBTUSD"
count = 4
params = {'count': count}

def test_book() :
    file = open('TestData/book_schema.json',"r")
    response = requests.get(baseUrlBook)
    responseJson = json.loads(response.text)
    print(response.json())
    data = json.loads(file.read())
    schema = data
    is_valid = validate(instance=responseJson, schema=schema)
    print(data)
    print(is_valid)
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
    

def test_book_count() :
    #file = open('TestData/trades_schema.json',"r")
    response = requests.get(baseUrlBook, params=params)
    responseJson = json.loads(response.text)
    responseStr = json.dumps(responseJson)
    print(responseStr)
    #data = json.loads(file.read())
    #schema = data
    #is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    assert response.status_code == 200
    #assert (tradeName in responseStr), "Given Trade name: "+tradeName+" is not in Response"
    #assert jsonpath.jsonpath(responseJson,'$.result')[0] == "XBTUSD"
#keyword
#def validate_book_ask_should_be_positive(self, response):
#    assert response['ask\[1]'] > 0

def test_book_elaps() :
   #file = open('TestData/trades_schema.json',"r")
    response = requests.get(baseUrlBook, timeout=5)
    responseJson = json.loads(response.text)
    #responseStr = json.dumps(responseJson)
    #print("======================")
    #print(response.elapsed)
    #print("======================")
    #assert (response.elapsed.total_seconds). = 0000.2, "Request was  delayed"
    #data = json.loads(file.read())
    #schema = data
    #is_valid = validate(instance=responseJson, schema=schema)
    #print(data)
    #print(is_valid)
    assert response.status_code == 200
    #assert (tradeName in responseStr), "Given Trade name: "+tradeName+" is not in Response"
    #assert jsonpath.jsonpath(responseJson,'$.result')[0] == "XBTUSD"
    #keyword
    #def validate_book_ask_should_be_positive(self, response):
    #    assert response['ask\[1]'] > 0