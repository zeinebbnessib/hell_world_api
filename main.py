from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet(name: str = "there"):
    return {"message": f"Hello, {name}!"}
