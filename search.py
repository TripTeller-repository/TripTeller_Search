from konlpy.tag import Okt
from fastapi import FastAPI
from pydantic import BaseModel
import java_config

java_config.configure_java()

app = FastAPI()
okt = Okt()

class TextData(BaseModel):
    text: str

@app.post('/analyze')
def analyze_text(data: TextData):
    tokens = okt.morphs(data.text)
    return {"tokens": tokens}