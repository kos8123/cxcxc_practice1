from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class model(BaseModel):
    key: str

app = FastAPI()

@app.get("/api/test")
async def HelloWorld():
    return "Hello World"

@app.post("/api/test")
async def test(cxcxc: model):
    if cxcxc.key == "cxcxc":
        return {"message": "Succeeded"}
    else:
        return {"message": "Failed"}
    
        


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
