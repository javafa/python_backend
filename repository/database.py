from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import config


DB_URL = f"mysql+mysqlconnector://{config.db['user']}:{config.db['password']}@{config.db['host']}:{config.db['port']}/{config.db['database']}?charset=utf8mb4&collation=utf8mb4_general_ci"

engine = create_engine(DB_URL, convert_unicode=False, pool_size=30, pool_recycle=500, max_overflow=30)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def sessionScope():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()