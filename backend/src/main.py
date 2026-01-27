from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, todos
from .core.database import create_db_and_tables

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'PATCH'],
    allow_headers=['*'],
)

@app.on_event('startup')
def on_startup():
    create_db_and_tables()

app.include_router(auth.router)
app.include_router(todos.router)

@app.get('/')
def root():
    return {'status': 'online'}