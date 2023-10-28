import fastapi
import uvicorn
api = fastapi.FastAPI()

@api.get('/test/calculate')
def calculate(x: int, y: int): # integer type hints define the default type of the arguments.
    return x + y

uvicorn.run(api, port=8000, host='127.0.0.1')