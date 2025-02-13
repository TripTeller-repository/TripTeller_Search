import langid
from konlpy.tag import Okt
from nltk.corpus import stopwords
import nltk
import re
import json

nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))

# 한국어 불용어 목록
with open('stopwords.json', 'r',  encoding='utf-8') as file:
        korean_stopwords = json.load(file)["stopwords"]

# KoNLPy Okt
okt = Okt()

# 영어 처리
def remove_stopwords_en(text):
        tokens = text.split()
        return [word for word in tokens if word.lower() not in english_stopwords]

# 한국어 처리
def remove_stopwords_ko(tokens):
        return [word for word in tokens if word not in korean_stopwords]

# 언어 감지 함수
def detect_language(text):
        lang, _ = langid.classify(text)
        return lang

# 특수문자 제거 함수
def remove_special_chars(tokens):
    cleaned_tokens = [] 

    for token in tokens:

        # 특수문자 제거
        cleaned_token = re.sub(r'[^가-힣a-zA-Z0-9]', '', token)
        
        # 디버깅 출력
        # print(f"Original token: {token} -> Cleaned token: {cleaned_token}")
        
        # 특수문자가 제거된 값이 비어있지 않으면 리스트에 추가
        if cleaned_token:  
            cleaned_tokens.append(cleaned_token)
    
    return cleaned_tokens

# 텍스트 처리 과정
def process_text(text):
        lang = detect_language(text)

        if lang == 'en' :
                filtered_tokens = remove_stopwords_en(text)
                removed_tokens = remove_special_chars(filtered_tokens)
        elif lang == 'ko':
                tokens = okt.morphs(text)
                filtered_tokens = remove_stopwords_ko(tokens)
                removed_tokens = remove_special_chars(filtered_tokens)
        else:
                return {"error":"Unsupported language"}
        
        # DB 검색용으로 변환된 단어들 메인 서버에 반환
        search_keywords = "%" + "%".join(removed_tokens) + "%"

        return {"filtered_tokens": removed_tokens, "search_keywords": search_keywords}
        