from typing import List, Union

from pydantic import BaseModel


class EventoBase(BaseModel):
    titulo: str



class EventoCreate(EventoBase):
    titulo: str


class Evento(EventoBase):
    id: int    

    class Config:
        orm_mode = True

