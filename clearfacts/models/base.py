import re

class BaseModel:

    def parse(self, json):
        for key, value in json.items():
            key = self.camel_to_snake_case(key)
            lower_key = ''.join(e.lower() for e in key if e.isalnum())
            lower_attrs = { k.replace('_', '').lower() : k for k in self.__dict__.keys() }

            if lower_key in lower_attrs.keys():
                key = lower_attrs[lower_key]
                attr_value = getattr(self, key)

                if isinstance(attr_value, BaseModel):
                    setattr(self, key, attr_value.parse(value))
                else:
                    setattr(self, key, value)

        return self
    
    def get_json(self):

        dikt = {}
        for k, v in self.__dict__.items():
            if v:
                if isinstance(v, BaseModel):
                    json = v.get_json()
                    if json: dikt[k] = json
                else:
                    dikt[k] = v

        return dikt if len(dikt) > 0 else None
    
    @staticmethod
    def camel_to_snake_case(name):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    
class Errors(BaseModel):
    
    def __init__(
        self,
        errors=None
    ):
        
        self.errors = errors

    def parse(self, json):
        self.errors = [Error().parse(error) for error in json.get('errors', [])]
        return self

class Error(BaseModel):
    
    def __init__(
        self,
        message=None
    ):
        
        self.message = message