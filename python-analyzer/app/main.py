from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Task Analyzer", version="0.1.0")

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    createdAt: Optional[datetime] = None
    dueAt: Optional[datetime] = None

class AnalysisResult(BaseModel):
    total: int
    completed: int
    pending: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalysisResult)
def analyze(tasks: List[Task]):
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    pending = total - completed
    return AnalysisResult(total=total, completed=completed, pending=pending)
