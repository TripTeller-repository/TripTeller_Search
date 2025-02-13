from konlpy.tag import Okt
from fastapi import FastAPI
from pydantic import BaseModel
import text_process

okt = Okt()

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.get('/')
def health_check():
    return {"status":"ok"}

@app.post('/text-processing')
def process_text(data: TextData):
    result = text_process.process_text(data.text)
    if "error" in result:
        return {"error": result["error"]}
    
    # print(result)
    return result