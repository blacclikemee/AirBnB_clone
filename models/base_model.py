#!/usr/bin/python3
"""Class BaseModel"""

import uuid
from datetime import datetime

class BaseModel:
    """Implementation of Class BaseModel"""
    def __init__(self, id, created_at, updated_at):
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

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    save(self):
        """Method to save the updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""



