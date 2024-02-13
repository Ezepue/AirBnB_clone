import uuid
from datetime import datetime
import models

class BaseModel:
    """
    The base class for all other models
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes instances of BaseModel.
        """
        if kwargs:
            attr = kwargs.copy()
            del attr['__class__']
            attr['created_at'] = datetime.strptime(attr['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            attr['updated_at'] = datetime.strptime(attr['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in attr.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute 'updated_at' with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        """
        attr = self.__dict__.copy()
        attr['__class__'] = self.__class__.__name__
        if not isinstance(attr['created_at'], str):
            attr['created_at'] = attr['created_at'].isoformat()
        if not isinstance(attr['updated_at'], str):
            attr['updated_at'] = attr['updated_at'].isoformat()
        return attr
