from fastapi import FastAPI
import uvicorn
import time

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "q": "some item"}

@app.get('/time')
def get_current_time():
    return {'time': time.time()}

# sudo kill -9 `sudo lsof -t -i:8000`
if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, debug=True)