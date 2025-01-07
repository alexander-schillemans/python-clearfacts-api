from .base import APIMethod
from clearfacts.models.users import UserInfo
from clearfacts.models.base import Error
from clearfacts.constants.errors import APIError

class UserMethods(APIMethod):

    def get_info(self):
        status, headers, response = self.api.get('userinfo', base=self.api.oauth2_server_url)
        if status != 200:
            raise APIError(Error().parse(response))
        return UserInfo().parse(response)