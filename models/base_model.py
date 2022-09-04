#!/usr/bin/pythn3
"""
base class file
"""

import uuid
from datetime import datetime
import models
from json import JSONEncoder


class BaseModel:
    """
    =========
    BaseModel
    =========
    """

    def __init__(self, *args, **kwargs):
        """initialize the instance of the class"""
        if Kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    value = date.strptime(
                            value,
                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue
                setattr(self, key, vlaue)
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = date.now()
                models.storage.new(self)
                
                def save(self):
                    """save new informations to the class object"""
                    self.updated_at = datetime.now()
                    models.storage.save()

                    def to_dict(self):
                        """return dictionary representation of the instance"""
                        dict_repr = {}
                        for key, value in self.__dict__.items():
                            dict_repr[key] = vlaue.strtime('%Y-%m-%dT%H:%M:%S.%f')
                            dict_repr["__class__.__name__
                            return dict_repr

                            def __str__(self):
                            """return the string formated message when instance is called"""
                            clName = self.__class__.__name
                            return "[{}] ({}) {}".format(clName, self.id, self.__dict__)


                            class BaseModelEncoder(JSONEncoder):

                            """JSON Encoder for BaseModel
                            """


                            def default(self, o):
                            """ default"""
                            if isinstance(o.to_dict()
                            return super().default(o)
