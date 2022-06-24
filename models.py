from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
#from sqlalchemy.orm import relationship
from database import Base

import logging
logger = logging.getLogger(__name__)

class Evento(Base):
    __tablename__ = "eventos"
    #__table_args__ = {'extend_existing': True}
    #__abstract__ = True

    id          = Column('id', Integer, primary_key=True, index=True)
    imagen      = Column('imagen',String)
    titulo      = Column(String, index=True)
    resumen     = Column(String, index=True)
    descripcion = Column(String, index=True)
    fechainicio  = Column(Date)
    fechafin    = Column(Date)
    horainicio  = Column(Time)
    horafin     = Column(Time)
    ciudad      = Column(String)
    direccion   = Column(String)
    asistentes  = Column(Integer)      
    is_active   = Column(Boolean, default=True)
