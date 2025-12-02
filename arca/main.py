from fastapi import FastAPI

app = FastAPI(title="ARCA Compliance API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
