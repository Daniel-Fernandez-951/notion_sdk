from typing import Optional

from .. import session


class UserIdMissing(Exception):
    info = """\n
    User ID is required.
    Notion API docs: https://developers.notion.com/reference/get-user
    """


class User:
    """
    Notion API's User object and related endpoints
    """

    def __init__(self,
                 user_id: Optional[str] = None):
        if user_id is None:
            raise UserIdMissing(f"{UserIdMissing.info}")
        self.user_id = user_id
        self.path_root = "https://api.notion.com/v1/users/"
        self.path_id = self.path_root + self.user_id

    def get(self):
        response = session.get(url=self.path_id)
        return response.json()

    def get_all(self):
        response = session.get(url=self.path_root)
        return response.json()

    def get_bot_token(self):
        url = self.path_root + "me"
        response = session.get(url=url)
        return response.json()
