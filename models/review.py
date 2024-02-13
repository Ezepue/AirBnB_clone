#!/usr/bin/env python3

"""Review class Module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Initializes instances of Review.
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
