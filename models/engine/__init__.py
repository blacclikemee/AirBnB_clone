#!/usr/bin/python3
"""Creating an instance of FileStorage called storage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
