#!/usr/bin/env python3
"""City class Module"""

from models.base_model import BaseModel

class City(BaseModel):
	"""
	Initializes city instances
	"""
	
	state_id: str = ""
	name: str = ""
