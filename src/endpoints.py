from starlette.responses import PlainTextResponse

async def homepage(request):
    return PlainTextResponse('Hi Victor Dzeba')