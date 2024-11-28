from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts."}


@app.post("/post")
def post(new_post: Post):

    # automatic validating the request body
    print(new_post)

    # to print the new_post pydantic model as a dictionary
    # new_post.dict() method is deprecated
    return {"data": new_post.model_dump()}
