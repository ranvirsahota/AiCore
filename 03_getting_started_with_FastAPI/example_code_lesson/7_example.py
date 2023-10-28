import fastapi
import uvicorn
import json
api = fastapi.FastAPI()

@api.post('/send/process_data')
def process_data(x: int, y: int):

    if y == 0:
        return fastapi.Response(content=json.dumps({"error" : "y cannot be zero"}),
                                media_type='application/json',
                                status_code=400)
    return x / y

uvicorn.run(api, port=8000, host='127.0.0.1')