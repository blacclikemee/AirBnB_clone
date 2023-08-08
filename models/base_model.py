#!/usr/bin/python3
"""Class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """Implementation of Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """
            Initialises the BaseModel attributes

            Attributes:
            self
            id: id of the model
            created_at: Datetime representing when the Model was created
            updated_at: DAtetime representing when an object is changed

            Returns:
            None
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
            Function that prints  print: [<class name>] (<self.id>)
            <self.__dict__>
        """
        return"[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Method that saves the updated time"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
