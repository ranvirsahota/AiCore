import fastapi

router = fastapi.APIRouter()

@router.get('/menu/')
def menu():
    return {'menu': ['pizza', 'pasta', 'salad', 'soup']}