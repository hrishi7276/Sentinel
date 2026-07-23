from fastapi import FastAPI
from app.routers import symbol_router
from app.database.health import check_database_connection
from app.core.exception_handlers import register_exception_handlers

app = FastAPI(
    title="Sentinel Engine API",
    description="Trading Engine for the Sentinel Platform",
    version="0.5.0"
)

register_exception_handlers(app)

app.include_router(
    symbol_router.router,
    prefix="/api/v1",
)
@app.get("/")
def root():
    return {
        "message": "Welcome to Sentinel Engine"
    }


@app.get("/api/v1/health")
def health():

    db_status = "Healthy" if check_database_connection() else "Unhealthy"

    return {
        "status": "Healthy",
        "service": "Sentinel.Engine",
        "version": "0.5.0",
        "database": db_status
    }