from fastapi import FastAPI

app = FastAPI()

# Home Route 
@app.get('/')
def home():
    return {'message': 'Welcome to Home Page'}

# About Route
@app.get('/about')
def about():
    return {'message': 'Welcome to About Page'}

# # Users Route
# @app.get('/users')
# def users():
#     return {
#         "users":['Mohit', 'Rohit', 'Amit'] 
#     }

# Creating Dynamic URL 

# Path Parameters
# Users Route 
@app.get('/users/{user_id}')
def get_user(user_id: int):
    return {
        'user_id': user_id,
    }

# Single Query Parameters
# Users Route 
@app.get('/users')
def get_user(name: str=None):    # To pass Null value 
    return {
        'Name': name,
    }

@app.get('/products')
def get_user(limit: int=10):    # To pass Default value 
    return {
        'Limit': limit,
    }

# Multiple Query Parameters
@app.get('/items')
def get_user(name: str=None, price: int=0):    # To pass Default value 
    return {
        'Name': name,
        'Price': price,
    }
