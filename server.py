from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from repository import models
from repository.database import engine

from router import router_user, router_root

import config
import uvicorn

app = FastAPI(
    title="Flow9 REST Sample",
    description="RESTful API 테스트를 위한 페이지 입니다. (데이터가 주기적으로 삭제됩니다)",
    version="0.1.0",
)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

# home
# app.include_router(
#     router_root.router,
#     tags=["root"],
#     responses={404: {"description": "File Not found"}},
# )

# user
app.include_router(
    router_user.router,
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "File Not found"}},
)

# start server
if __name__ == '__main__' :
    print("[Started] REST sample")
    print("[Started] address="+config.server['address']+":"+str(config.server['port']))
    uvicorn.run(app, 
        host=config.server['address'], 
        port=config.server['port'], 
        log_level=config.server['log_level'], 
        proxy_headers=True,
        forwarded_allow_ips="*")
