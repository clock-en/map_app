import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import users_router, auth_router, spots_router, comments_router
from app.core.sqlalchemy.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [os.environ['FRONTEND_ORIGIN']]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['Content-Type', 'X-Amz-Date', 'Authorization',
                   'X-Api-Key', 'X-Amz-Security-Token', 'X-Token'],
)

app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(spots_router.router)
app.include_router(comments_router.router)

"""
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0', reload=True)
"""
