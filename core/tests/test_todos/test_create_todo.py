from datetime import datetime, timedelta
from unittest.mock import patch
from uuid import UUID

import pytest
from freezegun import freeze_time

from core.todos.create_todo import init_todo


def test_create_valid_todo() -> None:
    mock_uuid4 = UUID('dcde60f6-eef2-4e77-bf89-c73fccef9f4f')
    with freeze_time("2024-12-12"), patch('uuid.uuid4', return_value=mock_uuid4):

        todo: dict[str, str] = init_todo(name='Learn Flask')

        assert todo == {"name": "Learn Flask",
                        "status": "pending",
                        "id": mock_uuid4,
                        "created_at": datetime(2024, 12, 12)
                        }


def test_create_todo_with_empty_name():
    with pytest.raises(ValueError, match="Task name is required."):
        init_todo(name="")


def test_create_todo_invalid_name():
    with pytest.raises(ValueError, match="Task name is required."):
        init_todo(name="  ")


@pytest.mark.skip(reason="Not implemented yet.")
def test_create_todo_with_all_options():
    with freeze_time("2024-12-12"):
        start_datetime = datetime.now() + timedelta(days=1)
        data = {
            "name": "Learn Flask",
            "description": "Learn Flask in 2025",
            "start_dt": start_datetime,
            "duration": timedelta(minutes=10),
            "estimated_duration": timedelta(minutes=10),
            "type": "workshop",
            "priority": 'critical',
            "status": "pending"
        }

        todo = init_todo(**data)

        assert todo == {**data, "id": 1, "status": "pending", "created_at": datetime(2024, 12, 12)}


def test_create_todo_with_past_start_date():
    pass


def test_create_todo_with_non_positive_duration():
    pass


def test_create_todo_with_non_positive_estimated_duration():
    pass
