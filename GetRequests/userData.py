"""
Perform API get requests
Base url: https://reqres.in/
"""
import json
from http import HTTPStatus

import requests
from jsonpath import jsonpath

baseUrl = 'https://reqres.in'
relativeQueryAllUsers = '/api/users?page=2'
relativeQueryAUser = '/api/users/2'  # user ID= 2

# send get request for all users
response = requests.get(baseUrl + relativeQueryAllUsers)

# content & header information
print(response.content)
print(response.headers)  # encoding, request time..

if HTTPStatus.OK.value != response.status_code:
    # raise error when response code is not 200 'OK'
    raise 'API request is not success'


# fetch response header
requestDateTime = response.headers.get('Date')
serverName = response.headers.get('Server')

# fetch cookies
savedCookies = response.cookies

# fetch encoding
encodingType = response.encoding

# fetch elapsed time
elapsedTime = response.elapsed

# convert response content to json / dict
jsonResponse = json.loads(response.text)

# fetch value using jsonpath -> return value is list
totalPage = jsonpath(jsonResponse, 'total_pages')
print(totalPage[0])

# usual dict access: jsonResponse['data'][2]['first_name']
thirdFirstName = jsonpath(jsonResponse, 'data[2].first_name')

# print all first names
allData = jsonpath(jsonResponse, 'data')[0]
totalData = len(allData)
for idx in range(totalData):
    firstName = jsonpath(jsonResponse, f'data[{idx}].first_name')[0]
    print(firstName)