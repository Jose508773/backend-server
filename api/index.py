from fastapi import FastAPI, HTTPException      # FastAPI = the framework; HTTPException for error responses
from fastapi.middleware.cors import CORSMiddleware  # needed so browsers on other domains can call us
from pydantic import BaseModel 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # whitelist App B's domain; use ["*"] for "anyone" (less safe)
    allow_methods=["*"],                          # allow GET, POST, etc.
    allow_headers=["*"],                          # allow any request headers
)

class input_incoming(BaseModel):
    a: float
    b: float
    

class output_outgoing(BaseModel):
    result: float
    

@app.get("/")
def root():
    return {"message": "online the server is working"}

@app.get("/api/online")
def online():
    return {"message": "online the server is working hello howdy whats your name"}


#
#@app.post("/api/add", response_model=output_outgoing)
#def take_input(request: Request, response: Response):




    
    
