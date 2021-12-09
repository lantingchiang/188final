from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()
#dictionary of class to description
classes = {"CIS188": "A great devops class",} 
#dictionary of student to list of classes enrolled in
registrations = {"test": ["CIS188"], }

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

@app.get("/home/{user}", response_class=HTMLResponse)
def home_view(request: Request, user: str = "test"):
    classes_to_return = registrations.get(user)
    if not classes_to_return:
        classes_to_return = []

    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request, "classes": classes_to_return, "user": user}
    )


@app.get("/course-list/{user}", response_class=HTMLResponse)
def course_list_view(request: Request, user:str):
    return TEMPLATES.TemplateResponse(
        "course-list.html",
        {"request": request, "courses": classes, "user": user}
    )


@app.get("/create/{user}")
def add_course(request: Request, user: str):
    return TEMPLATES.TemplateResponse("create-course.html", {"request": request, "user": user})


@app.post("/create/{user}")
def add_course(request: Request, user: str, name: str = Form("name"), description: str = Form("description")):
    if not name or not description:
        raise HTTPException(
            status_code=400, detail="course name or description missing"
        )
    
    classes[name] = description
    print(classes)
    return TEMPLATES.TemplateResponse(
        "message.html",
        {"request": request, "message": f"Added course {name}", "user": user}
    )


@app.get("/drop/{user}/{course}")
def drop_course(request: Request, user: str, course: str):
    if course in registrations[user]:
        registrations[user].remove(course)
        return TEMPLATES.TemplateResponse(
            "message.html", 
            {"request": request, "message": f"Dropped course {course}", "user": user}
        )
    return TEMPLATES.TemplateResponse(
        "message.html", 
        {"request": request, "message": f"You're not in {course}", "user": user}
    )


@app.get("/register/{user}/{course}")
def drop_course(request: Request, user: str, course: str):
    if course in registrations[user]:
        return TEMPLATES.TemplateResponse(
            "message.html", 
            {"request": request, "message": f"You're already in {course}", "user": user}
        )  
    
    registrations[user].append(course)
    return TEMPLATES.TemplateResponse(
        "message.html", 
        {"request": request, "message": f"Registered for course {course}", "user": user}
    )