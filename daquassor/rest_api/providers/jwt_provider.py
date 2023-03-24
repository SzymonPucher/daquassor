import time
from typing import Dict, Union
import datetime as dt

import jwt

from daquassor.rest_api.models.user import User


class JWTProvider:
    def __init__(
        self, jwt_secret: str, jwt_algorithm: str, token_ttl_in_seconds: int = 3600
    ):
        self.jwt_secret = jwt_secret
        self.jwt_algorithm = jwt_algorithm
        self.token_ttl_in_seconds = token_ttl_in_seconds

    def sign_jwt(self, user: User) -> Dict[str, str]:
        payload = user.get_public_info()
        payload["expires"] = time.time() + self.token_ttl_in_seconds
        return jwt.encode(payload, self.jwt_secret, algorithm=self.jwt_algorithm)

    def decode_jwt(self, token: str) -> Union[dict, None]:
        try:
            decoded_token = jwt.decode(
                token, self.jwt_secret, algorithms=[self.jwt_algorithm]
            )

            if decoded_token.get("expires", dt.datetime.min) <= time.time():
                raise ValueError("Expired JWT token.")

            return decoded_token
        except jwt.exceptions.InvalidSignatureError:
            raise ValueError("Invalid JWT token.")
