from fastapi import FastAPI, status, HTTPException, Depends, Header
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

# -------------- Creating Dynamic URL ---------------

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

# @app.get('/products')
# def get_user(limit: int=10):    # To pass Default value 
#     return {
#         'Limit': limit,
#     }

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
class Product(BaseModel):
    id: int
    name: str
    price: int
    
@app.post('/products')
def create_product(product:Product):
    products.append(product)
    return {
        "message": "User Created Successfully",
        "data": product
    }

@app.put('/products/{product_id}')
def update_product(product_id: int, updated_product: Product, notify: bool = False):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {
                "message": "Data updated successfully",
                "notify": notify,
                "data": updated_product
            }
    return {"error": "Product not found with this id!!.."}


# -------------- Response Models & Hiding Sensitive Data --------------------
class Login_User(BaseModel):
    user_name: str
    email: str
    password: str

class LoginResponse(BaseModel):
    user_name: str
    email: str

@app.get('/login_user', response_model = LoginResponse)
def get_login_user():
    return {
        "user_name":"Mohit",
        "email": 'xyz@gmail.com', 
        "password": "123456"
    }

# Creating APIs in a professional way
@app.post('/create_new_user', status_code=status.HTTP_201_CREATED)
def create_new_user():
    return {
        'message': 'User Created Successfully'
    }

@app.get('/get_new_users')
def get_new_users():
    return {
        'status': 'Success',
        'message': 'User Fetched Successfully',
        'data': {
            'Name': 'Mohit', 
            'Age': 27
        }
    }
    
@app.get('/get_new_user/{user_id}')
def get_new_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404, 
            detail="User Not Found"
        )
    else:
        return {
            'id': 1,
            'Name': 'Rohit'
        }   

#-------------- Dependency Injection ----------------

# def common_logic():
#     return {
#         'message': 'Common Logic Executed'
#     }

# @app.get('/home')
# def home(data = Depends(common_logic)):
#     return data

# def get_current_user():
#     return {
#         'user': 'Mohit'
#     }

# @app.get('/profile')
# def profile(user = Depends(get_current_user)):
#     return user

# @app.get('/dashboard')
# def dashboard(user = Depends(get_current_user)):
#     return user

def verify_user(token:str = Header(None)):
    if token != 'mysecrettoken':
        raise HTTPException(
            status_code=401,
            detail = 'Unauthorized'
        )
    return {
        'user': 'Authorised User'
    }

@app.get('/secure-data')
def secure_data(user = Depends(verify_user)):
    return{
        'message': 'Secure Data Accessed',
        'user': user
    }





