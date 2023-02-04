from typing import List
from typing import Dict
from typing import Optional
from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    description:Union[str, None] = None
    price: float
    tax: Union[float, None] = None

sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str, str] = {'username': 'Nobuhiro',}


app = FastAPI()


origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/items/")
async def create_item(item:Item):
    return item

@app.get("/")
async def index():
    return sample_dict

@app.get("/countries/")
async def index(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}