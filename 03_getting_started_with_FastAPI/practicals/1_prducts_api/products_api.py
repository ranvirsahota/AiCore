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
def get_product(product_id: int):
    return all()[product_id]

@api.get('/products/by_category/{category}')
def by_category(category: str):
    products = all()
    return dict(product for product in products.items()
                            if filter_category('clothes', product))


def filter_category(category, product):
    return product[1]['category'] == category