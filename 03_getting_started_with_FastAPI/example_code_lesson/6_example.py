import fastapi
import uvicorn
import json
api = fastapi.FastAPI()

@api.get('/test/calculate')
def calculate(x: int, y: int):
    if y == 0:
        return fastapi.Response(content=json.dumps({"error" : "y cannot be zero"}),
                                media_type='application/json',
                                status_code=400)
    return x / y

uvicorn.run(api, port=8000, host='127.0.0.1')