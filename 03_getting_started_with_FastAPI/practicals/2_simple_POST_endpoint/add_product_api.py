import fastapi
api = fastapi.FastAPI()

products = []

@api.post('/products/add/')
def add_product(product):
    products.append(product)
    print(products)
#OUTPUT
# ["'sock", "'PC", "'mouse", "'jeans", "'sock"]