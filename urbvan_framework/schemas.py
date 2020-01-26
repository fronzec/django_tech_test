# coding: utf8
from rest_framework import pagination
from rest_framework.response import Response

from marshmallow import (Schema, fields, pre_dump)


class BaseErrorSchema(Schema):
    """
    Base error schema, it allows a more detailed error messages
        Fields:
            code - the error code
            message - a descriptive message of the error
            field - the field name which causes the error
            app - the name of the application, in which the error occurred
    """
    code = fields.Integer()
    message = fields.String()
    field = fields.String()
    app = fields.String()


class BaseBodyLinkSchema(Schema):
    """
    The base schema for links on paginated responses
    """
    next = fields.String(default=None)
    previous = fields.String(default=None)


class BaseBodySchema(Schema):
    """
    Base body schema for responses
    """
    links = fields.Nested(
        BaseBodyLinkSchema(),
        default=BaseBodyLinkSchema().dump({}).data
    )
    count = fields.Integer()
    results = fields.List(fields.Dict())

    @pre_dump
    def validate_count(self, data):

        count = len(data.get("results", []))
        data['count'] = count

        return data


class BaseResponseSchema(Schema):
    """
    The base response schema which contains the response content or errors
    """
    errors = fields.Nested(BaseErrorSchema, many=True, default=[])
    body = fields.Nested(BaseBodySchema, default={})


class PaginationResponse(pagination.PageNumberPagination):
    """
    Custom paginated response schema
    """
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'body': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            },
            'errors': []
        })
