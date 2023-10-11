"""
Perform API put request
"""


import json
from http import HTTPStatus

import requests
from jsonpath import jsonpath

# use existing userId in the user. A random user Id is generated after a post request.
# The same random Id cannot be used with put request.

userId = '2'
baseUrl = 'https://reqres.in'
relativeQueryAUser = f'/api/users/{userId}'

# send get request
response = requests.get(baseUrl + relativeQueryAUser)

# Get current details with content & header information
print(json.loads(response.text))

# put request on the user ID
userDetail = {
    "name": "Testing for fun",
    "job": "Learner"
}

jsonContent = json.dumps(userDetail)
putUrl = baseUrl + relativeQueryAUser

# put request
putResponse = requests.put(putUrl, jsonContent)

if HTTPStatus.OK.value != putResponse.status_code:
    # raise error when response code is not 200 'OK'
    raise 'API put request is not success'

# convert the response to json so as to get the user ID
jsonRespone = json.loads(putResponse.text)

# get updated time
updatedAt = jsonpath(jsonRespone, 'updatedAt')[0]

# get request on the user ID to verify the update
getResponse = requests.get(baseUrl + relativeQueryAUser)

# convert the response to json so as to get the user ID
jsonResponse = json.loads(getResponse.text)

# get updated user name
updatedName = jsonpath(jsonRespone, 'name')[0]
