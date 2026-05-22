from fastapi import FastAPI # class
from app.models import load_model_scaler # function
from app.schema import Cardio # class

app = FastAPI() # Object instance of FastAPI

model, scaler = load_model_scaler()

# request methods
# ------------------
# post (create/insert), get(read/retrive/select), put(update), delete(remove)

@app.get('/')
def home():
    return 'Welcome to cardiovascular disease prediction system'