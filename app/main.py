from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.router import users
from app.core.orm.database import engine
from app.core.orm import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# TODO: developと本番を分けられるようにする
origins = ['http://localhost:3000']

# TODO: 最終的にセキュリティが最適化されているかを確認する
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

"""
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0', reload=True)
"""
