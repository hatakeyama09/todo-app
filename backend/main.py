from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ===== データモデル =====

# レスポンス用 Todo
class Todo(BaseModel):
    id: int
    title: str
    completed: bool


# リクエスト用（Todo作成時）
class TodoCreate(BaseModel):
    title: str


# ===== 仮データ（DBの代わり） =====

todos: list[Todo] = []
next_id = 1


@app.get("/todos", response_model=list[Todo])
def get_todos():
    return todos
