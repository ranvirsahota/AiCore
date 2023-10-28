import fastapi

router = fastapi.APIRouter()

@router.post('/order/')
def order(item: str, quantity: int):
    print(f'Order received for {quantity} of {item}')