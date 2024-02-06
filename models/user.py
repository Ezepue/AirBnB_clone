#!/usr/bin/env python3
"""User class Module"""

from models.base_model import BaseModel

class User(BaseModel):
	"""
	Initializes instances of User.
	"""
	email: str = ""
	password: str = ""
	first_name: str = ""
	last_name: str = ""
