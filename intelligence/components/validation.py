from pydantic import BaseModel, ValidationError
import json


class Intel(BaseModel):
    timestamp: str
    signal_id: str
    entity_id: str
    reported_lat: float
    reported_lon: float
    signal_type: str
    priority_level: int


def field_test(data):
    try:
        Intel(**data)
        return data
    except ValidationError:
        return False



def convert_to_dict(data):
    try:
        data = json.loads(data)
        return data
    except json.decoder.JSONDecodeError:
        return False




# x = {"timestamp": "2026-03-16T10:19:42.892708+00:00",
#      "signal_id": "f10a518e-070d-43e6-b195-26cabdc9c324", "entity_id": "TGT-010",
#      "reported_lat": 31.883817,
#      "reported_lon": 34.599941, "signal_type": "HUMINT", "priority_level": 3}
#
# print(field_test(x))