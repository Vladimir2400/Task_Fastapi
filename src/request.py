from src.database import async_session, TaskTable
from src.schemas import STaskAdd, STask

from sqlalchemy import select, delete


class TaskRequest:
    @classmethod
    async def add_task(cls, data: STaskAdd) -> int:
        async with async_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with async_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            tasks_schemas = [STask(**task_model.__dict__) for task_model in tasks_models]

            return tasks_schemas
