from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/index.html', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/about.html', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})


@app.get('/contacts.html', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('contacts.html', {'request': request})