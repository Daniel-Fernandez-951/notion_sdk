import requests
from typing import Dict, Optional

from .. import session


class PageIdMissing(Exception):
    info = """\n
    Page ID is required.
    Notion API docs: https://developers.notion.com/reference/retrieve-a-page
    """
    pass


class PropertyIdMissing(Exception):
    info = """\n
    Property ID is required.
    Notion API docs: https://developers.notion.com/reference/retrieve-a-page-property
    """


class EndpointRequiresData(Exception):
    info = f"""\n
    This endpoint requires data not supplied.
    Notion API docs: https://developers.notion.com/reference/\
    """

    def info_out(self):
        return self.info


class Page:
    """
    Notion API Pages object and related endpoints
    """

    def __init__(self,
                 pg_id: Optional[str]):

        if pg_id is None:
            raise PageIdMissing(f"{PageIdMissing.info}")

        self.id = pg_id
        self.path_root = "https://api.notion.com/v1/pages/"
        self.path_id = f"{self.path_root + self.id}/"

    def get(self):
        response = session.get(url=self.path_id)
        return response.json()

    def get_item(self,
                 property_id: Optional[str] = None,
                 params: Optional[Dict] = None):
        if property_id is None:
            raise PropertyIdMissing(f"{PropertyIdMissing.info}")
        url = self.path_id + "properties/" + property_id
        if params is not None:
            response = session.get(url=url, params=params)
            return response.json()
        response = session.get(url=url)
        return response.json()

    def patch(self, data: Dict = None):
        if data is None:
            raise EndpointRequiresData(f"{EndpointRequiresData.info}")
        response = session.patch(url=self.path_id, data=data)
        return response.json()

    def post(self, data: Dict = None):
        if data is None:
            raise EndpointRequiresData(f"{EndpointRequiresData.info}")
        response = session.post(url=self.path_id, data=data)
        return response.json()
