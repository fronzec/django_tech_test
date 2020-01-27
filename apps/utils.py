# coding: utf8
from datetime import datetime
from uuid import uuid4


# TODO: 26/01/2020 Review this method
def create_id(prefix):
    """
    Create an id based on the given prefix, it appends custom information to generate
    an id
    Fields:
            id -- A must not empty prefix used to create the id
    """
    id_base = "{} {} {} {} {} {} {} {}"
    now = datetime.utcnow()
    id_base = id_base.format(
        prefix,
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        str(uuid4())[:8]
    )
    return id_base
