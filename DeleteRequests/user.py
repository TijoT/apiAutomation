"""
Perform API delete requests
"""

import json
from http import HTTPStatus

import requests
from jsonpath import jsonpath

baseUrl = 'https://reqres.in'
deleteUserUrl = '/api/users/2'

# send delete request
response = requests.delete(baseUrl + deleteUserUrl)

if HTTPStatus.NO_CONTENT.value != response.status_code:
    # if delete was success, then response code is '200'.
    # Here the user is not available, so response code is '204'
    raise 'API delete request is not success'
