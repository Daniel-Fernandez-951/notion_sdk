from typing import Dict, List, Optional

from .. import session


class BlockIdMissing(Exception):
    info = """\n
    Block ID is required
    Notion API docs: https://developers.notion.com/reference/retrieve-a-block
    """


class BlockRequiresData(Exception):
    info = """\n
    This endpoint requires data not supplied.
    Notion API docs: https://developers.notion.com/reference/block
    """


class Block:
    """
    Notion API's Block object and related endpoints
    """

    def __init__(self,
                 blk_id: Optional[str] = None):

        if blk_id is None:
            raise BlockIdMissing(f"{BlockIdMissing.info}")
        self.id = blk_id
        self.path_root = "https://api.notion.com/v1/blocks/"
        self.path_id = f"{self.path_root + self.id}/"

    def get(self):
        response = session.get(url=self.path_root)
        return response.json()

    def get_children(self,
                     params: Optional[Dict]):
        url = self.path_id + "children"
        if params is not None:
            response = session.get(url=url, params=params)
            return response.json()
        response = session.get(url=url)
        return response.json()

    def patch(self,
              data: Optional[Dict] = None):

        if data is None:
            raise BlockRequiresData(f"{BlockRequiresData.info}")
        response = session.patch(url=self.path_id, data=data)
        return response.json()

    def patch_children(self,
                       data: Optional[Dict[List]] = None):
        if data is None:
            raise BlockRequiresData(f"{BlockRequiresData.info}")
        url = self.path_id + "children"
        response = session.patch(url=url, data=data)
        return response.json()

    def delete(self):
        response = session.delete(url=self.path_id)
        return response.json()
