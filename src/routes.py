from starlette.routing import Route

from src.endpoints import homepage

routes = [
    Route('/', homepage)
]