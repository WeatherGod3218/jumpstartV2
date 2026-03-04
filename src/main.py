"""
Jumpstart V2
Used for the Dashboard seen upon entering DSP Floor 3
Authors: Eli Mares,Nikolai Strong, Will Hellinger,
V1 Authors: Beckett Jenen
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from api import endpoints

app: FastAPI = FastAPI()
app.include_router(endpoints.router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates: Jinja2Templates = Jinja2Templates(directory="templates")