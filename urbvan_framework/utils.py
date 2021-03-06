# coding: utf8
from .schemas import (BaseResponseSchema, BaseBodySchema)


def render_response_error(errors={}):
    """
    This method allow creates an error response
    """
    list_errors = []
    for key, value in errors.items():

        if type(value) is list:
            value = {"message": value[0]}

        value.update({"field": key})
        list_errors.append(value)

    response = {"errors": list_errors}

    response = BaseResponseSchema().dump(response).data
    return response


def render_to_response(body={}):
    """
    This method allow creates response body
    """
    response = {}
    response = BaseBodySchema().dump({
        "results": [body]
    }).data
    response = BaseResponseSchema().dump({
        "body": response
    }).data

    return response
