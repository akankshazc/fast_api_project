from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "Post 1", "content": "This is the content of post 1", "id": 1,
             "published": True, "rating": 5},
            {"title": "Post 2", "content": "This is the content of post 2", "id": 2,
             "published": True, "rating": 4}]


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/post")
def post(new_post: Post):

    # automatic validating the request body
    print(new_post)

    # to print the new_post pydantic model as a dictionary
    # new_post.dict() method is deprecated
    return {"data": new_post.model_dump()}
