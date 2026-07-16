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

# Users Route
@app.get('/users')
def users():
    return {
        "users":['Mohit', 'Rohit', 'Amit'] 
    }