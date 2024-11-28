from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts."}


@app.post("/post")
def post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}
