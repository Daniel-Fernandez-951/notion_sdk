import requests
from typing import Dict, Optional

from .. import session

class SearchRequiresData(Exception):
    info = """\n
    Search data is required.
    Notion API docs: https://api.notion.com/v1/search
    """


class Search:
    """
    Notion API's Search object and related endpoints
    """
    def __init__(self):
        self.path_root = "https://api.notion.com/v1/search/"

    def post(self,
             data: Optional[Dict] = None):
        if data is None:
            raise SearchRequiresData(f"{SearchRequiresData.info}")
        response = session.post(url=self.path_root)
        return response.json()
