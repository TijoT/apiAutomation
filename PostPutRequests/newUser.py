"""
Perform API post (new) requests
"""


import json
from http import HTTPStatus

import requests
from jsonpath import jsonpath

baseUrl = 'https://reqres.in'
postUserUrl = '/api/users'

userDetail = {
    "name": "Testing for fun",
    "job": "Learner"
}

jsonContent = json.dumps(userDetail)
postUrl = baseUrl + postUserUrl

# post request
response = requests.post(postUrl, jsonContent)


if HTTPStatus.CREATED.value != response.status_code:
    # response code should be '201' for create.
    raise 'API post request is not success'

# response header
print(f'Cryptic data with creation details: {response.headers}')

# convert the response to json so as to get the user ID
jsonRespone = json.loads(response.text)

# get created user id
userId = jsonpath(jsonRespone, 'id')[0]

