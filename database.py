import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlmodel import SQLModel

SQLALCHEMY_DATABASE_URL = "postgresql://%s:%s@%s:%s/%s" % (os.environ["BBDD_USER"], \
                                                           os.environ["BBDD_PASSWORD"], \
                                                           os.environ["BBDD_HOST"], \
                                                           os.environ["BBDD_PORT"], \
                                                           os.environ["BBDD_DATABASE"])

dbschema='public'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'options': '-csearch_path={}'.format(dbschema)})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
