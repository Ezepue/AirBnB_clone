#!/usr/bin/env python3
"""Amenity class Module"""

from models.base_model import BaseModel

class Amenity(BaseModel):
	"""
	This class Initializes amenity instances
	"""
	
	name: str = ""
