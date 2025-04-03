# LitePolis Middleware Example: JWT Authentication

This repository was generated using the LitePolis command-line interface:
```bash
litepolis-cli create middleware litepolis-middleware-example
```

> :warning: **Naming Convention:** Always keep the prefix "litepolis-middleware-" in your project directory name and "litepolis_middleware_" in your Python package directory name. This ensures the LitePolis package manager can recognize and integrate your middleware during deployment.

## What is LitePolis Middleware?

Middleware in LitePolis acts like a gatekeeper or processor for incoming requests to your web application. It can perform tasks like:

* Authentication & Authorization (like this JWT example!)
* Logging requests
* Modifying request/response headers
* Data validation
* Rate limiting
* And much more!

By building custom middleware, you can encapsulate reusable logic and keep your main application code clean.

## How to use
Add middleware to your LitePolis application:
```bash
litepolis-cli deploy add-deps litepolis-middleware-example
```

Add the middleware to FastAPI routes:
```python
from fastapi import FastAPI, Depends, Request
from starlette.responses import JSONResponse
from starlette.authentication import requires
# Other necessary imports for your application logic

app = FastAPI() # Your FastAPI app instance managed by LitePolis

# ... other app setup

@app.get("/users/me")
@requires("authenticated") # Apply the decorator here
async def read_current_user(request: Request):
    # This endpoint is now protected.
    # Code here will only execute if the middleware successfully authenticates the request.
    user_email = request.user.identity # Access the authenticated user's identity (email in this case)
    # Or access other properties if the middleware returns a different user object type
    # user_display_name = request.user.display_name

    return JSONResponse({
        "message": f"Hello, authenticated user!",
        "email": user_email,
        # ... return other relevant user data
    })

@app.get("/public-data")
async def read_public_data():
    # This endpoint is *not* protected by the @requires decorator
    return {"message": "This data is available to everyone."}

# ... other endpoints
```

## Tutorial: From Template to Middleware

Prerequisites: Install the LitePolis command-line tool:
```bash
pip install litepolis
```

Let's walk through the process of creating this middleware example.

**Step 1: Create Your Middleware Project**

```bash
# Replace 'your-middleware-name' with your desired name
litepolis-cli create middleware litepolis-middleware-example
cd litepolis-middleware-example
```

**Step 2: Understand the Project Structure**

Your generated project will have the following key files and directories:

* **`setup.py`**: Configures your Python package (name, version, dependencies). You'll edit this before publishing.
* **`requirements.txt`**: Lists development/testing dependencies.
* **`litepolis_middleware_example/`**: This is your actual Python package directory.
    * **`__init__.py`**: Makes the directory a Python package and exports key components (like `add_middleware` and `DEFAULT_CONFIG`).
    * **`core.py`**: **The heart of your middleware.** Contains the main logic, including the `add_middleware` function and default configuration (`DEFAULT_CONFIG`).
    * **`utils.py`**: (Optional) For helper functions used by your middleware. In this example, it has `verify_user_credentials`.
* **`tests/`**: Contains unit and integration tests for your middleware.
    * **`test_core.py`**: Tests the functionality defined in `core.py`.
    * **`test_exports.py`**: Ensures necessary components are correctly exported, DO NOT EDIT.
    * **`utils.py`**: Test utilities.
* **`README.md`**: (This file!) Documentation for your middleware.
* **`LICENSE`**: Your project's license file.

**Step 3: Implement Middleware Logic (`core.py`)**

Open `litepolis_middleware_example/core.py`. This is where the magic happens.

* **`add_middleware(app)` function:** This function is **essential**. LitePolis calls this function to add your middleware to a FastAPI application instance (`app`). You use `app.add_middleware(...)` here.
    * In this example, it adds Starlette's `AuthenticationMiddleware` and provides our custom `JWTAuth` backend.
* **Middleware Backend Class (e.g., `JWTAuth`):** This class contains the core logic executed for each request.
    * It typically inherits from `starlette.authentication.AuthenticationBackend`.
    * The `authenticate(self, request)` method is crucial. It inspects the incoming `request` (e.g., checks headers for a token), validates credentials, and returns `AuthCredentials` and a user object (like `SimpleUser`) upon success, or `None` otherwise.
    * Our example `JWTAuth` looks for a `Bearer` token in the `Authorization` header, decodes it using a secret key, and extracts the user's email.

**Step 4: Define Configuration (`core.py`)**

* **`DEFAULT_CONFIG` Dictionary:** Define default configuration values for your middleware here. These values are registered with LitePolis when your middleware is deployed.
    * Example: `DEFAULT_CONFIG = {"secret_key": "your-default-secret"}`.
* **Accessing Configuration:** Inside your middleware (like in `JWTAuth.authenticate`), you need to access the *active* configuration, which might override the defaults. Use the pattern shown in `core.py` which checks `os.environ` to determine if running under Pytest (use `DEFAULT_CONFIG`) or in a live environment (use `litepolis.get_config`).

```py
import os

# Define default values suitable for the testing environment
DEFAULT_TEST_CONFIG = {
    "secret_key": "your-default-secret"
    # Add other necessary default test config values here
}

# Check if running under Pytest
if "PYTEST_CURRENT_TEST" not in os.environ and "PYTEST_VERSION" not in os.environ:
    # NOT running under Pytest: Fetch from live source (replace with actual logic)
    print("Fetching configuration from live LitePolis...")
    secret_key = get_config("litepolis_middleware_example", "secret_key")
else:
    # Running under Pytest: Use default test values
    print("Running under Pytest. Using default test configuration.")
    secret_key = DEFAULT_TEST_CONFIG["secret_key"]

# Use the determined configuration values
print(f"UI Refresh Interval: {refresh_interval}")
print(f"Show Notifications: {show_notifications}")
```

**Step 5: Write Tests (`tests/test_core.py`)**

Testing is crucial! Open `tests/test_core.py`.

* Use `fastapi.testclient.TestClient` to make simulated requests to a test FastAPI app instance that includes your middleware.
* Write tests for different scenarios:
    * Valid authentication (e.g., correct JWT).
    * Invalid authentication (e.g., bad token, expired token).
    * Missing credentials.
* Ensure your tests cover the logic in your middleware backend (`JWTAuth`) and any helper functions (`verify_user_credentials`).
* Run tests using `pytest` in your terminal.

**Step 6: Package Your Middleware (`setup.py`)**

Before sharing, configure `setup.py`:

* **`name`**: Change `litepolis-middleware-example` to your unique package name (e.g., `litepolis-middleware-myauth`). Remember the prefix!
* **`version`**: Set an initial version (e.g., `"0.1.0"`).
* **`author`, `url`, `description`**: Update these fields.
* **`install_requires`**: List *runtime* dependencies needed by your middleware (e.g., `pyjwt`, `litepolis`). `sqlmodel` is listed in the example.

**Step 7: Publish**
To make your middleware easily installable, publish it to the Python Package Index (PyPI). Follow standard Python packaging guides for this.
