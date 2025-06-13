# GLOBAL IMPORT:
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from datetime import datetime

import uvicorn
# GLOBAL IMPORT END.


# FastAPI activation:
app = FastAPI()
# FastAPI activation END.


# Product development status and version selector:
DEV_STATUS = True  # True = development, False = production

PROJECT_VERSION = "1.0"


@app.get("/server/main_page", response_class=HTMLResponse)
async def get_main_page(request: Request):

    static_ver = datetime.now().timestamp() if DEV_STATUS else PROJECT_VERSION

    return templates.TemplateResponse("module_1_main.html", {
        "request": request,
        "static_ver": static_ver,
    })

# Product development status and version selector END.


# Монтируем короткий путь


# Монтируем длинный абсолютный путь для клиента (например, чтобы работали превью в IDE)

# Шаблоны




if __name__ == "__main__":
    uvicorn.run("main:app")
