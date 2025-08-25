from typing import TypedDict
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str=Field(description="the title of the linkedin post")
    content:str=Field(description="The main content of the linkedin post")

class BlogState(TypedDict):
    topic:str
    blog:Blog