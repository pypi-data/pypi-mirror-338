import os
import base64
import binascii
import jwt

from starlette.authentication import (AuthenticationBackend,
                                      AuthenticationError,
                                      SimpleUser,
                                      AuthCredentials)
from starlette.middleware.authentication import AuthenticationMiddleware
from litepolis_database_example import DatabaseActor
from litepolis import get_config

from .utils import verify_user_credentials

DEFAULT_CONFIG = {
    "secret_key": "your-secret-key"
}


class JWTAuth(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return None

        auth = request.headers.get("Authorization")
        if not auth:
            return None

        try:
            scheme, token = auth.split()
            if scheme.lower() != "bearer":
                return None
        except ValueError:
            return None

        try:
            if ("PYTEST_CURRENT_TEST" not in os.environ and
                "PYTEST_VERSION" not in os.environ):
                # Replace with actual service name and key
                package_name = os.path.dirname(
                    os.path.dirname(__file__)
                )
                secret_key = get_config(package_name, "secret_key")
            else:
                # Running under Pytest: Use default values
                print("Running under Pytest. Using default configuration.") # Optional debug msg
                secret_key = DEFAULT_CONFIG["secret_key"]
            payload = jwt.decode(token, secret_key, algorithms=["HS256"]) # Replace "your-secret-key" with your actual secret key
            email = payload.get("email")
            if email:
                return AuthCredentials(["authenticated"]), SimpleUser(email)
            else:
                raise AuthenticationError("Invalid token: missing email")
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Invalid token: expired")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid token")


def add_middleware(app):
    app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())
    return app
