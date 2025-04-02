from __future__ import annotations

import functools
from unittest.mock import patch

from mockgcp.storage.client import MockClient


def mock_storage(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with patch("google.cloud.storage.Client", MockClient):
            return func(*args, **kwargs)

    return wrapper
