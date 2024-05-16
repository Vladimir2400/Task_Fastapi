from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.database import create_tables, delete_tables

from src.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Бд очищена")
    await create_tables()
    print("Бд готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)

app.include_router(router)