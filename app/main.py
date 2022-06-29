import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import users_router, auth_router, spots_router
from app.core.sqlalchemy.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [os.environ['FRONTEND_ORIGIN']]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
    allow_headers=['*'],
)

app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(spots_router.router)

"""
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0', reload=True)
"""
