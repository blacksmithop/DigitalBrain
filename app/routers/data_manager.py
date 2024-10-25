from fastapi import APIRouter, Request

from app import Category, DeleteCategory, load_knowledge_data

router = APIRouter()


@router.post("/load_knowledge_data", tags=["Knowledge"])
async def load_data(request: Request):
    dataset = load_knowledge_data()
    return dataset


@router.post("/add_category", tags=["Knowledge"])
async def add_category(payload: Category):
    print(f"Received payload for category {payload.name}")
    return 200


@router.delete("/delete_category", tags=["Knowledge"])
async def dlete_category(payload: DeleteCategory):
    print(f"Deleting category {payload.id}")
    return 200
