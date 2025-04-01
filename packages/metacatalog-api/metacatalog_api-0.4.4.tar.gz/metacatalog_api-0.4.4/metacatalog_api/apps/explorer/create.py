from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from metacatalog_api import core
from metacatalog_api.server import server

create_router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent / 'templates')


@create_router.get('/page/create_metadata.html')
def new_entry_page(request: Request):
    return templates.TemplateResponse(request=request, name="page_create_metadata.html", context={"path": server.app_prefix})

@create_router.get('/create/entries.html')
def new_entry(request: Request):
    return templates.TemplateResponse(request=request, name="add_entry.html", context={"path": server.app_prefix})


@create_router.get("/utils/leaflet_draw.html")
def leaflet_draw(request: Request, geom: str = 'marker'):
    if geom.lower() == 'marker':
        return templates.TemplateResponse(request=request, name="leaflet_marker.html", context={})
    elif geom.lower() == 'extent':
        return templates.TemplateResponse(request=request, name="leaflet_extent.html", context={})


@create_router.get('/create/authors.html')
def new_author(request: Request):
    return templates.TemplateResponse(request=request, name="author.html", context={"path": server.app_prefix})


@create_router.get('/create/details.html')
def new_details(request: Request):
    return templates.TemplateResponse(request=request, name="details.html", context={"path": server.app_prefix})


@create_router.get('/create/datasources.html')
def new_datasource(request: Request):
    # load the datasource types
    types = core.datatypes()
    return templates.TemplateResponse(request=request, name="add_datasource.html", context={"types": types, "path": server.app_prefix})
