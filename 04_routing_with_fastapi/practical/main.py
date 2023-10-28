import fastapi
import menu
import order

api = fastapi.FastAPI()

def configure_routing():
    api.include_router(menu.router)
    api.include_router(order.router)


configure_routing()
