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



class Validation:

    def convert_to_dict(self,data):
        try:
            data = json.loads(data)
            return True ,data
        except json.decoder.JSONDecodeError:
            return False ,'json.decoder.JSONDecodeError'


    def field_test(self,data):
        try:
            Intel(**data)
            return True, data
        except ValidationError:
            return False , 'ValidationError'

    def full_inspection(self,event):
        dict_data = self.convert_to_dict(event)
        if dict_data[0]:
            data_correct = self.field_test(dict_data[1])
            return data_correct
        return dict_data






# x = {"timestamp": "2026-03-16T10:19:42.892708+00:00",
#      "signal_id": "f10a518e-070d-43e6-b195-26cabdc9c324", "entity_id": "TGT-010",
#      "reported_lat": 31.883817,
#      "reported_lon": 34.599941, "signal_type": "HUMINT", "priority_level": 3}
#
# y = "gsfghgs"


