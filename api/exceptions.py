"""
File to create  customm exceptions.
"""

from rest_framework import exceptions
from rest_framework import status

class DataNotFound(exceptions.APIException):
    status_code = status.HTTP_404_NOT_FOUND
    response  =  "Record does not exist!"

class PermissionDenied(exceptions.APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    response = "Sorry! You are not Authorized to view this page!"

class BadRequest(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    response = "Provided data is invalid! Please check entered values and try again!"

class NoContent(exceptions.APIException):
    status_code = status.HTTP_204_NO_CONTENT
    response = "Record deleted successfully!"

class Created(exceptions.APIException):
    status_code = status.HTTP_201_CREATED
    response = "Record created successfully!"