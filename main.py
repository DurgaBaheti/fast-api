from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'example': 'this is an example', 'data': 1234567890}

@app.get('/random')
async def get_random():
    rn: int = random.randint(0, 100)
    return {'number': rn, 'limit': 100}

@app.get('/random/{limit}')
async def get_random(limit: int):
    rn: int = random.randint(0, limit)
    return {'number': rn, 'limit': limit}

@app.get('/deepfake/{data}')
async def get_data(data: int):
    if data < 18:
        return {'success': 'ready to vote'}
    else: 
        return {'success': 'not ready to vote'}