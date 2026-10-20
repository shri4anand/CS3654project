from fastapi import FastAPI

app = FastAPI(title="CS3654 Backend")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}
