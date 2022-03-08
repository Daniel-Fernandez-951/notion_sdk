"""

Make SESSION here (requests) from https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python

"""
import os
import requests
from .__version__ import __notion_api_version__
from dotenv import load_dotenv

load_dotenv()

NOTION_INTEGRATION_SECRET = os.getenv('NOTION_SECRET', None)
CONTENT_TYPE = "application/json"
NOTION_VERSION = __notion_api_version__


# NOTION_INTEGRATION_SECRET = os.environ.get('NOTION_SECRET', None)


class NotionIntegrationKeyMissing(Exception):
    pass


if NOTION_INTEGRATION_SECRET is None:
    raise NotionIntegrationKeyMissing(
        """
        All endpoints require API Secret and integration allowed on workspace
        See "https://developers.notion.com/docs/authorization" for more
        information on authentication, integration, and approval by workspace.
        """
    )

session = requests.Session()
session.headers = {
    "Authorization": "Bearer" + " " + NOTION_INTEGRATION_SECRET,
    "Content-Type": CONTENT_TYPE,
    "Notion-Version": NOTION_VERSION
}

# TODO: Review for removal
try:
    from .notion import NotionAPI
    from .access.database import Database
except ImportError as e:
    print(e)
