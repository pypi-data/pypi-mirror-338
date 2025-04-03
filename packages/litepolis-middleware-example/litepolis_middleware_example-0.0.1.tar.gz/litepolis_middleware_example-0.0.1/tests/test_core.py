import unittest
import base64
import jwt
import time
from litepolis_database_example import DatabaseActor
from fastapi import FastAPI, APIRouter, Depends
from fastapi.testclient import TestClient
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.authentication import requires
from litepolis_middleware_example.utils import verify_user_credentials
from litepolis_middleware_example.core import add_middleware, DEFAULT_CONFIG

class TestVerifyUserCredentials(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_user = DatabaseActor.create_user(email="alice@example.com", password="securepassword123")

    @classmethod
    def tearDownClass(cls):
        DatabaseActor.delete_user(cls.test_user.id)

    def test_correct_credentials(self):
        test_email = "alice@example.com"
        correct_password = "securepassword123"
        self.assertTrue(verify_user_credentials(test_email, correct_password))

    def test_incorrect_password(self):
        test_email = "alice@example.com"
        incorrect_password = "wrongpassword"
        self.assertFalse(verify_user_credentials(test_email, incorrect_password))

    def test_nonexistent_email(self):
        nonexistent_email = "nosuchuser@example.com"
        correct_password = "securepassword123"
        self.assertFalse(verify_user_credentials(nonexistent_email, correct_password))


class TestMiddlewareIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = FastAPI()
        cls.app = add_middleware(cls.app)

        @cls.app.get("/protected")
        @requires("authenticated")
        async def protected_route(request: Request):
            return JSONResponse({
                "message": "Hello, authenticated user!",
                "user": request.user.username
            })

        cls.client = TestClient(cls.app)
        cls.test_user = DatabaseActor.create_user(
            email="test_middleware@example.com",
            password="middlewarepassword"
        )

    @classmethod
    def tearDownClass(cls):
        DatabaseActor.delete_user(cls.test_user.id)

    def test_valid_credentials_middleware(self):
        email = "test_middleware@example.com"
        password = "middlewarepassword"
        token = self.create_jwt(email)
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Hello, authenticated user!")
        self.assertEqual(response.json()["user"], email)

    def test_invalid_credentials_middleware(self):
        email = "test_middleware@example.com"
        token = "wrongpassword"
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 400)

    def test_no_credentials_middleware(self):
        response = self.client.get("/protected")
        self.assertEqual(response.status_code, 403)

    # Add JWT tests here
    def create_jwt(self, email: str,
                   secret_key: str = DEFAULT_CONFIG["secret_key"],
                   algorithm: str = "HS256", expiration_time: int = 3600):
        payload = {
            "email": email,
            "exp": int(time.time()) + expiration_time
        }
        token = jwt.encode(payload, secret_key, algorithm=algorithm)
        return token

    def test_jwt_authentication_success(self):
        email = "test_middleware@example.com"
        token = self.create_jwt(email)
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Hello, authenticated user!")
        self.assertEqual(response.json()["user"], email)

    def test_jwt_authentication_failure_invalid_token(self):
        headers = {"Authorization": "Bearer invalid-token"}
        response = self.client.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 400)

    def test_jwt_authentication_failure_expired_token(self):
        email = "test_middleware@example.com"
        expired_token = self.create_jwt(email, expiration_time=-1)  # Expired immediately
        headers = {"Authorization": f"Bearer {expired_token}"}
        response = self.client.get("/protected", headers=headers)
        self.assertEqual(response.status_code, 400)

    def test_jwt_authentication_failure_missing_header(self):
        response = self.client.get("/protected")
        self.assertEqual(response.status_code, 403)