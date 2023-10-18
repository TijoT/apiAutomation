*** Settings ***
Library  RequestsLibrary

*** Variables ***
${BaseUrl}  https://thetestingworldapi.com/

*** Test Cases ***
TC_001_GetRequest

	# create sesssion SessionName with base url
	Create Session  Get_Student_Details  ${BaseUrl}

	# send a get request with relative url; Get request is deprecated;
	${response}=  GET On Session  Get_Student_Details  api/studentsDetails

	Log To Console  ${response.status_code}
