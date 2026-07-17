from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ----------------------Get Method---------------------------
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
def get_items(name: str=None, price: int=0):    # To pass Default value 
    return {
        'Name': name,
        'Price': price,
    }

# ------------------------- Post method ----------------------------
# @app.post('/create-user')
# def create_user(user:dict):
#     return {
#         'message': 'User created successfully',
#         'data': user
#     }

# @app.post('/create-user')
# def create_user(name:str, age:int):
#     return {
#         'Name': name,
#         'Age': age
#     }

# Using Pydantic 
# Simple post method doesn't provide validation in fastAPI, so we use pydantic basemodel for this purpose  

# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# @app.post('/create-user')
# def create_user(user:User):
#     return {
#         'message': 'User created successfully',
#         'data': user
#     }

# Nested pydantic BaseModel
class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post('/create-user')
def create_user(user: User):
    return user

# ------Path + Query Parameters + Body Combo ------------
# PUT /product/101?notify=true
# {
#    "name": "Salt",
#    "price": 24
# }

products = []
Class Product(BaseModel):
    name: str
    price: int

@app.post('/products')
def create_product(product:Product):
    products.append(product)
    return {
        "message": "User Created Successfully",
        "data": user
    }
    
    



