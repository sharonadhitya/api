from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional

app = FastAPI()

students = {
    1: {'name': 'sharon', 'age': 19}
}

@app.get("/")
def index():
    return {"message": "Welcome to the Student API!"}

@app.get("/students/{student_id}")
def get_student(student_id: Optional[int] = None):
    return students[student_id]
