from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/verse/html", response_class=HTMLResponse)
def get_verse(request: Request):
    return templates.TemplateResponse("verse.html", {"request": request})