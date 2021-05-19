from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import time

from user_handler import UserDataHandler
from jwt_auth_handler import signJWT, JWTBearer

app = FastAPI()
user_handler = UserDataHandler()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login(user = Body(...)):
    if user_handler.authenticate_user(user):
        return signJWT(user['email'])
    return {
        "error": "Wrong login details!"
    }

@app.post("/register")
def register(user = Body(...)):
    if user_handler.check_user(user):
        return {
            "error": "User Email already exists."
        }
    user_handler.add_user(user)
    return signJWT(user['email'])

@app.post("/changePassword", dependencies=[Depends(JWTBearer())])
def changePassword(user = Body(...)):
    if user_handler.authenticate_user(user):
        user_handler.modify_user(user)
        return signJWT(user['email'])
    return {
        "error": "User does not exist."
    }

@app.get("/")
def read_root():
    return {"Hello": "World"}

# -H 'Authorization: Bearer <jwt>'
@app.get("/model", dependencies=[Depends(JWTBearer())])
def score_model(item_id: int):
    return {"item_id": item_id, "q": "some item"}

@app.get('/time')
def get_current_time():
    return {'time': time.time()}

# sudo kill -9 `sudo lsof -t -i:8000`
if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, debug=True)