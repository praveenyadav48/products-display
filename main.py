from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import LocalSession,engine
from models import Base, Product

Base.metadata.create_all(engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )


@app.get('/products', response_class=HTMLResponse)
def products(req: Request):
    db = LocalSession()

    products = db.query(Product).all()

    db.close()


    return  templates.TemplateResponse(
        request=req,
        name="product.html",
        context={"products": products}
    )