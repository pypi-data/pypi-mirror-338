from airflow_orjson_serialization.json import ORJson

def test_round_trip():
    json = ORJson()
    data = {"msg": "hello", "value": 42, "한글": True}
    dumped = json.dumps(data)
    loaded = json.loads(dumped)
    assert loaded == data