from fastapi import FastAPI

app = FastAPI(
    title="Fitness Tracker",
    summary="A fitness tracker API",
    version="0.0.1",
    docs_url="/swagger",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
