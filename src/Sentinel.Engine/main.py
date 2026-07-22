from fastapi import FastAPI

app = FastAPI(
    title="Sentinel Engine API",
    description="Trading Engine for the Sentinel Platform",
    version="0.2.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Sentinel Engine"
    }


@app.get("/api/v1/health")
def health():
    return {
        "status": "Healthy",
        "service": "Sentinel.Engine",
        "version": "0.2.0"
    }