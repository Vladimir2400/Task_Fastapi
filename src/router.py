from typing import Annotated

from fastapi import APIRouter, Depends

from src.request import TaskRequest
from src.schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"],
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()],
                   ) -> STaskId:
    task_id = await TaskRequest.add_task(task)
    return {"add": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRequest.get_tasks()
    return tasks
