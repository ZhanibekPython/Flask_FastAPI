from typing import List

from fastapi import FastAPI, HTTPException

from moduls import Task

app = FastAPI()

tasks: List[Task] = []


@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    return tasks


@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}/", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    task_to_update = next((t for t in tasks if t.id == task_id), None)
    if task_to_update is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_to_update.title = updated_task.title
    task_to_update.description = updated_task.description
    task_to_update.status = updated_task.status
    return task_to_update


@app.delete("/tasks/{task_id}/", response_model=Task)
def delete_task(task_id: int):
    task_to_delete = next((t for t in tasks if t.id == task_id), None)
    if task_to_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task_to_delete)
    return task_to_delete
