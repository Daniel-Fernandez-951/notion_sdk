from typing import List, Dict, Optional

from .. import session


class DatabaseIdMissing(Exception):
    info = """\n
    Database ID is required.
    Notion API docs: https://developers.notion.com/reference/database
    """
    pass


class Database:
    """
    Notion API Database object and related endpoints
    """

    def __init__(self,
                 db_id: Optional[str] = None):

        if db_id is None:
            raise DatabaseIdMissing(f"{DatabaseIdMissing.info}")

        self.id = db_id
        self.path_root = "https://api.notion.com/v1/databases/"
        self.path_id = f"{self.path_root + self.id}/"

    def get(self):
        response = session.get(self.path_id)
        return response.json()

    def patch(self, data: Dict):
        """
        Updates an existing database based on body parameters:
        Notion API docs: https://developers.notion.com/reference/update-a-database
        :param data: { title:[ {} ], properties:{} }
        :type data: Dict
        :return: Server response
        :rtype: Dict
        """
        response = session.patch(url=self.path_id, data=data)
        return response.json()

    def post(self,
             parent: Dict,
             properties: Dict,
             title: Optional[List] = None):
        data = {"parent": parent,
                "properties": properties}
        if title is not None:
            data.update(f"title: {title}")
        response = session.post(url=self.path_id, data=data)
        return response.json()

    def post_query(self, data: Dict):
        """
        Apply filters similar to Notion UI
        Notion API docs: https://developers.notion.com/reference/post-database-query
        :param data: {filter:{}, sorts:[], start_cursor:str, page_size:int}
        :type data: Dict
        :return: Server response
        :rtype: Dict
        """
        url = self.path_id + "query"
        response = session.post(url=url, data=data)
        return response.json()
