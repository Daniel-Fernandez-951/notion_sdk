import pytest

from src.notion_sdk.access.database import Database, DatabaseIdMissing


def test_dummy():
    assert 0 is 0


def test_database_id_missing_exception():
    with pytest.raises(DatabaseIdMissing):
        assert Database()
