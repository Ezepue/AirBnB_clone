#!/usr/bin/env python3
"""Initializes package"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel

storage = FileStorage()
storage.reload()
