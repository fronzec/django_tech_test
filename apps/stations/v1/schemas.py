# coding: utf8
from marshmallow import (Schema, fields)

# TODO: 24/01/20 review this schema, review
#       review marshmallow funcitionalaty


class LocationSchema(Schema):
    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()


class StationSchema(Schema):
    id = fields.String()
    # TODO: 24/01/20 add locations
    order = fields.Integer()
    is_active = fields.Boolean()
