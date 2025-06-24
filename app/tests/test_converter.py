import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_supported_currencies():
    """
    Test the /supported-currencies endpoint returns 200 and expected keys.
    """
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/supported-currencies")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "supported_currencies" in json_data
    assert isinstance(json_data["supported_currencies"], list)
