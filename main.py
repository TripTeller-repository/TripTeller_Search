from konlpy.tag import Okt
from fastapi import FastAPI
from pydantic import BaseModel
import java_config

java_config.configure_java()

okt = Okt()

app = FastAPI()
print(okt.pos("너는 바보양 졸려죽겠쓰~~"))
class TextData(BaseModel):
    text: str

@app.post('/analyze')
def analyze_text(data: TextData):
    # if not jpype.isJVMStarted():
    #     java_config.configure_java()
    
    # Process the text and get tokens
    tokens = okt.morphs(data.text)
    return {"tokens": tokens}