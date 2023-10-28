import fastapi
import uvicorn
api = fastapi.FastAPI()

@api.get('/test/calculate')
def calculate(x: int, y: int):
    if y == 0:
        return fastapi.Response(content='y cannot be zero', status_code=400)
    return x / y

uvicorn.run(api, port=8000, host='127.0.0.1')