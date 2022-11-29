from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from src.ConnectStorage import storageConnect

app = FastAPI()

@app.get("/")
def read_files():
    storageConnect.log_download()
    return "Download was successful"
