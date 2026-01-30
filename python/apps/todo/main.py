import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from task import Task
from priority import Priority
from severity import Severity
from status import Status


# =========================
# App initialization
# =========================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# File storage config
# =========================

TASKS_FILE = Path("tasks.json")


# =========================
# Request model (from frontend)
# =========================

class TaskCreateRequest(BaseModel):
    name: str = Field(min_length=1)
    description: str
    status: str
    priority: str
    severity: str
    time_given: int = Field(gt=0)


# =========================
# Utility functions
# =========================

def parse_enum(enum_cls, value: str):
    try:
        return enum_cls[value.upper()]
    except KeyError:
        raise ValueError(f"Invalid {enum_cls.__name__}: {value}")


def save_task_to_file(task: Task):
    task_data = {
        "name": task.name,
        "description": task.description,
        "status": task.status.name,
        "priority": task.priority.name,
        "severity": task.severity.name,
        "time_given": task.time_given
    }

    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

    tasks.append(task_data)

    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# =========================
# API endpoints
# =========================

@app.post("/tasks")
def create_task(request: TaskCreateRequest):
    try:
        status = parse_enum(Status, request.status)
        priority = parse_enum(Priority, request.priority)
        severity = parse_enum(Severity, request.severity)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    task = Task(
        name=request.name,
        description=request.description,
        status=status,
        priority=priority,
        severity=severity,
        time_given=request.time_given
    )

    save_task_to_file(task)

    return {
        "message": "Task created and stored successfully",
        "task": {
            "name": task.name,
            "description": task.description,
            "status": task.status.name,
            "priority": task.priority.name,
            "severity": task.severity.name,
            "time_given": task.time_given
        }
    }


@app.get("/tasks")
def get_tasks():
    if not TASKS_FILE.exists():
        return []

    with open(TASKS_FILE, "r") as f:
        return json.load(f)
