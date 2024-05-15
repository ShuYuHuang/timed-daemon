from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class APIRequest(BaseModel):
    key: str

@app.post("/call_api")
def call_api(api_request: APIRequest):
    key=api_request.key
    return {"key": key}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)