from fastapi import FastAPI

from app.database.health import check_database_connection

app = FastAPI(
    title="Sentinel Engine API",
    description="Trading Engine for the Sentinel Platform",
    version="0.4.0"
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
        "version": "0.3.0",
        "database": db_status
    }