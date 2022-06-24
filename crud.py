from sqlalchemy.orm import Session, exc
from models import Evento
import models, schemas
exceptions = exc.sa_exc

def get_event(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Evento).offset(skip).limit(limit).all()
        
    except exceptions.SQLAlchemyError as e:
        print("ERROR: %s" % e)

def get_event_by_id(db: Session, id: int):
    try:
        return db.query(models.Evento).filter(models.Evento.id == id).first()
    except exceptions.SQLAlchemyError as e:
        print("ERROR: %s" % e)