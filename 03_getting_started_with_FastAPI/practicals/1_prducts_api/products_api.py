import fastapi

api = fastapi.FastAPI()

@api.get('/products/all')
def all():
    return { 
    1: {    'name': 't-shirt',   'price': 19.99,    'category': 'clothes'},
    2: {    'name': 'stickers',  'price': 1.99,     'category': 'accessories'},
    3: {    'name': 'mug',       'price': 9.99,     'category': 'kitchenware'},
    4: {    'name': 'hoodie',    'price': 29.99,    'category': 'clothes'},
    5: {    'name': 'cap',       'price': 14.99,    'category': 'accessories'}
    }

@api.get('/products/{product_id}')
def read_products(product_id: int):
    return await all()[product_id]