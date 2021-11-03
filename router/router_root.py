from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from controller import shop

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>RESTful Sample</title>
        </head>
        <body>
            <h1>REST API를 테스트하기 위한 페이지입니다.</h1>
        </body>
    </html>
    """

@router.get("/health")
async def health():
    return {"status" : "ok"}