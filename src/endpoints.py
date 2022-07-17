from starlette.endpoints import HTTPEndpoint
from starlette.responses import PlainTextResponse
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from config.database import database
from .models import support

template = Jinja2Templates(directory='templates')

# async def homepage(request):
#     return PlainTextResponse('Hi Victor Dzeba')

async def homepage(request):
    if request.method == 'POST':
        # print('AAAAAAAA')
        form = await request.form()
        query = support.insert().values(
            username=form['username'],
            email=form['email'],
            message=form['message']
        )
        await database.execute(query)
        return RedirectResponse(request.url_for('get_support'), status_code=303)
    return template.TemplateResponse('index.html', {"request": request})

async def get_support(request):
    query = support.select()
    results = await database.fetch_all(query)
    return template.TemplateResponse('support.html', {"request": request, "results": results})

class Home(HTTPEndpoint):
    """ Реализуем через классы """
    async def get(self, request):
        return template.TemplateResponse('index.html', {"request": request})

    async def post(self, request):
        form = await request.form()
        query = support.insert().values(
            username=form['username'],
            email=form['email'],
            message=form['message']
        )
        await database.execute(query)
        return RedirectResponse(request.url_for('get_support'), status_code=303)