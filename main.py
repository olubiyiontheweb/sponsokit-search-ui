from fastapi import FastAPI

sponsok_search_ui = FastAPI()


@sponsok_search_ui.get("/")
async def root():
    return {"message": "FastAPI initial setup works"}
