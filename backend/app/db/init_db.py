import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import engine, Base
from app.models import *  # Importar todos los modelos


async def init_db():
    async with engine.begin() as conn:
        # Crear todas las tablas
        await conn.run_sync(Base.metadata.create_all)
        print("Database tables created successfully!")


async def drop_db():
    async with engine.begin() as conn:
        # Eliminar todas las tablas
        await conn.run_sync(Base.metadata.drop_all)
        print("Database tables dropped!")


if __name__ == "__main__":
    asyncio.run(init_db())