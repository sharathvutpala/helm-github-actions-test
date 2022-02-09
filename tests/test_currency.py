import json
from fastapi.testclient import TestClient
import json
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from api.currency  import app

client = TestClient(app)

def test_curency():
    response = client.get("/currency/USD")
    data1 = jsonable_encoder(response)

    assert "message" not in response.json[errors]
