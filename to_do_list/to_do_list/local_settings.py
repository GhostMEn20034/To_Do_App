from pathlib import Path
import json
import os
from django.core.exceptions import ImproperlyConfigured

# reads json with config for database


class JsonReader:
    def __init__(self, path):
        self.path = path
        self.settings = Path(__file__).resolve().parent

    def file_opener(self, path):
        with open(os.path.join(self.settings, path)) as secrets_file:
            secrets = json.load(secrets_file)
            return secrets

    def get_secret(self, setting):
        """Get secret setting or fail with ImproperlyConfigured"""
        secrets = self.file_opener(self.path)
        try:
            return secrets[setting]
        except KeyError:
            raise ImproperlyConfigured("Set the {} setting".format(setting))