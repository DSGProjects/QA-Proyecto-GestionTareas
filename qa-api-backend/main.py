from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

posts = []

class Post(BaseModel):
    title: str
    body: str
    userId: int

@app.post("/posts")
def create_post(post: Post):
    new_post = post.dict()
    new_post["id"] = len(posts) + 1
    posts.append(new_post)
    return new_post

@app.get("/posts")
def get_all_posts():
    return posts

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"error": "Post not found"}

@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            return {"message": "Post deleted"}
    return {"error": "Post not found"}

@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: Post):
    for post in posts:
        if post["id"] == post_id:
            post["title"] = updated_post.title
            post["body"] = updated_post.body
            post["userId"] = updated_post.userId
            return post
    return {"error": "Post not found"}

