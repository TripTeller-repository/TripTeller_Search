from konlpy.tag import Okt
from fastapi import FastAPI, HTTPException
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
    try:
        result = text_process.process_text(data.text)
        if "error" in result:
            raise HTTPException(status_code=400, detail=f"Error processing text: {result['error']}")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")