from fastapi import FastAPI

from persistence_is_key.api import health

app = FastAPI(title="My Webapp")
app.include_router(health.router)
