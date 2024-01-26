import pytest
from unittest.mock import MagicMock, create_autospec
from aiogram import Router


@pytest.fixture
def router_mock():
    router = create_autospec(Router, instance=True)
    router.message = MagicMock()
    return router