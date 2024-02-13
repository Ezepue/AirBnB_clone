#!/usr/bin/env python3

"""State class Module"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Initializes instances of State.
    """
    name: str = ""
