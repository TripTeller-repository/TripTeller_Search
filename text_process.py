import langid
from konlpy.tag import Okt
from nltk.corpus import stopwords
import nltk
import spacy

nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))

# 한국어 불용어 목록 (간단한 예시 => 파일 불러오기로 바꿀 예정)
korean_stopwords = set(["은", "는", "이", "가", "을", "를", "의", "에서", "에", "와", "과"])

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

# 텍스트 처리 과정
def process_text(text):
        lang = detect_language(text)

        if lang == 'en' :
                filtered_tokens = remove_stopwords_en(text)
        elif lang == 'ko':
                tokens = okt.morphs(text)
                filtered_tokens = remove_stopwords_ko(tokens)
        else:
                return {"error":"Unsupported language"}
        
        # DB 검색 용으로 변환된 단어들 메인 서버에 반환
        search_keywords = "%" + "%".join(filtered_tokens) + "%"

        return {"filtered_tokens": filtered_tokens, "search_keywords": search_keywords}
        