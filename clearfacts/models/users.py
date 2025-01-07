from .base import BaseModel

class UserInfo(BaseModel):

    def __init__(self,
        sub=None,
        username=None,
        email=None,
        name=None,
        family_name=None,
        given_name=None,
        locale=None,
        preferred_username=None,
        accountant_id=None,
        accountant_name=None,
        accountant_vat_number=None,
        accountant_features=None,
        type=None
    ):

        super().__init__()

        self.sub = sub
        self.username = username
        self.email = email
        self.name = name
        self.family_name = family_name
        self.given_name = given_name
        self.locale = locale
        self.preferred_username = preferred_username
        self.accountant_id = accountant_id
        self.accountant_name = accountant_name
        self.accountant_vat_number = accountant_vat_number
        self.accountant_features = accountant_features
        self.type = type