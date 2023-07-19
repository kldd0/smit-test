import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import api
from app.db.postgres.register import init_db


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    return app

app = create_app()

@app.on_event("startup")
async def startup_event():
    init_db(app)

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["app", "tests"],
        log_level="debug",
    )