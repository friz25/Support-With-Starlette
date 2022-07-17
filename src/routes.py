from starlette.routing import Route
from src.endpoints import homepage, get_support

routes = [
    Route('/', homepage, methods=['GET', 'POST']),
    Route('/support', get_support, name='get_support'),
]