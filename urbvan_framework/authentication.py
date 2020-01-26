# coding: utf8
from rest_framework import authentication


class CustomTokenAuthentication(authentication.TokenAuthentication):
    """
    Custom token authentication for the app, this means the prefix for token
    it must be Urbvan instead of default prefix
    """
    keyword = 'Urbvan'
