from typing import Optional
from fastapi import FastAPI, Body, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# Sample data
my_posts = [{"title": "Post 1", "content": "This is the content of post 1", "id": 1,
             "published": True, "rating": 5},
            {"title": "Post 2", "content": "This is the content of post 2", "id": 2,
             "published": True, "rating": 4}]


# Function to find a single post
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


# Function to get index of a post by id
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Root path


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


# Retrieving all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# Creating a new post
@app.post("/post", status_code=status.HTTP_201_CREATED)
def post(new_post: Post):

    # to convert the new_post pydantic model as a dictionary
    # new_post.dict() method is deprecated
    post_dict = new_post.model_dump()
    post_dict['id'] = randrange(1000)

    my_posts.append(post_dict)

    return {"data": post_dict}


# Retrieving a single post
@app.get("/post/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)

    # if post is not found return a 404 response
    # if not post:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"message": f"Post with id {id} was not found"}

    # using HTTPException
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {
                            id} was not found")

    return {"data": post}


# Deleting a post
@app.delete("/post/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    post = find_post(id)

    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {
                            id} was not found")

    my_posts.remove(post)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Updating a post
@app.put("/post/{id}")
def update_post(id: int, post: Post):
    index = find_post_index(id)

    # if post is not found return a 404 response
    if not index:
        raise HTTPException(status_code=404, detail=f"Post with id {
                            id} was not found")

    # convert the post pydantic model as a dictionary
    post_dict = post.model_dump()

    # update the post
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"data": post_dict}
