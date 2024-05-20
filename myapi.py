import uvicorn
from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional

app = FastAPI()

students = {
    1: {'name': 'sharon', 'age': 19}
}

@app.get("/")
async def index():
    return {"message": "Welcome to the Student API!"}

@app.get("/students/{student_id}")
def get_student(student_id: Optional[int] = None):
    return students[student_id]

if __name__ == "__main__":
    uvicorn.run("myapi:app", host="0.0.0.0", port=8000, reload=True)
