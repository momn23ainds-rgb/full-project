
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import ingest, browse, selection, generation, retrieval

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CT200 Backend")

app.include_router(ingest.router)
app.include_router(browse.router)
app.include_router(selection.router)
app.include_router(generation.router)
app.include_router(retrieval.router)

@app.get("/")
def root():
    return {"message":"CT200 API Running"}
