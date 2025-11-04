from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return ({"response":"400. Ok."})