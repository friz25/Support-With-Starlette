from starlette.responses import PlainTextResponse
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse
template = Jinja2Templates(directory='templates')

# async def homepage(request):
#     return PlainTextResponse('Hi Victor Dzeba')

async def homepage(request):
    if request.method == 'POST':
        # print('AAAAAAAA')

        return RedirectResponse(request.url_for('get_support'), status_code=303)
    return template.TemplateResponse('index.html', {"request": request})

async def get_support(request):
    return template.TemplateResponse('support.html', {"request": request})