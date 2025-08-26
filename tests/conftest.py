import pytest
from config import settings

@pytest.fixture(scope="session")
def app_settings():
    """Fixture cung cấp đối tượng cài đặt cho các bài kiểm thử."""
    return settings
