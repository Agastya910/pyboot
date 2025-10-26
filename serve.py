from fastapi import FastAPI
from iris_summary import show_summary_dict

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Iris API alive"}


@app.get("/iris")
def iris_stats():
    return show_summary_dict()
