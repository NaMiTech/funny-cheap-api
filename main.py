#from fastapi import FastAPI
from pyexpat import model
from typing import Union
import logging
import time
import os

from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("LOG_LEVEL", "DEBUG"))

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


ch = logging.StreamHandler()
ch.setFormatter(formatter)


logger.addHandler(ch)

from fastapi import FastAPI, Header, HTTPException, Request, Depends

# Configuración de la base de datos
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def on_startup():
    logger.info("Start funny")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/evento/{evento_id}")
def read_item(evento_id: int, db: Session = Depends(get_db)):
    evento = crud.get_event_by_id(db, id=evento_id)
    if evento is None: 
        raise HTTPException(status_code=404, detail="El evento ya no esta disponible")
    return evento

@app.get("/eventos/")
def get_eventos(db: Session = Depends(get_db)):
    eventos =  crud.get_event(db)
    #eventos = models.get_eventos()
    if eventos is None:
        raise HTTPException(status_code=404, detail="No hay eventos")

    return eventos

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("Consulta: %s - %s - %s" % (request.url, request.client.host, str(process_time)))    
    return response