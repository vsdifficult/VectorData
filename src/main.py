from fastapi import FastAPI
from pydantic import BaseModel
from database import VectorDatabase
import uvicorn
app = FastAPI()
db = VectorDatabase()

class Texts(BaseModel):
    texts: list[str]

@app.on_event("startup")
async def startup_event():
    # Загрузка текстов из файла при старте приложения
    try:
        await db.load_texts('./data/texts.json') 
        print("Тексты загружены из файла.")
    except FileNotFoundError:
        print("Файл с текстами не найден. База данных будет пустой.")

@app.post("/add_texts/")
async def add_texts(texts: Texts):
    await db.add_texts(texts.texts)
    await db.save_texts('./data/texts.json')
    return {"message": "Тексты добавлены"}

@app.get("/search/")
async def search(query: str):
    results = await db.search(query)
    return results
if __name__ == "__main__": 
    uvicorn.run(app=app, host="0.0.0.0", port=8000)