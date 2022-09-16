# Pytest - API testing with Python `requests`


#### Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.

#### The `requests` module allows you to send HTTP requests using Python.

## Getting started

* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`

To ensure all dependencies are resolved in a CI environment, in one go, add them to a `requirements.txt` file.
* Then run the following command : `pip install -r requirements.txt`

By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files.

Pytest requires the test method names to start with `test`. All other method names will be ignored even if we explicitly ask to run those methods.

A sample test below :

```python
def test_auth() :
    path = "api/register"
    response = requests.post(url=baseUrlAuthentication)
    responseJson = json.loads(response.text)
    response.raise_for_status()  # raises exception when not a 2xx response
    if response.status_code != 204:
         return response.json()
    assert response.status_code == 200
    print(responseJson['token'])
    assert response.status_code == 200
    assert type(jsonpath.jsonpath(responseJson,'$.token')[0]) == str

```
## Running tests

If your tests are contained inside a folder 'Tests', then run the following command : `pytest Tests` 
                                +++++++++++++++++++++++
++++++Be aware two test will be failing because Trade Name is not in a response.++++++
                                ++++++++++++++++++++++
To generate xml results, run the following command : `pytest Tests --junitxml="result.xml"`

For more on Pytest, go [here.](https://docs.pytest.org/en/stable/)
