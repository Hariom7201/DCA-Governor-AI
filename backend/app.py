from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DCA-Governor AI Backend Running"}
