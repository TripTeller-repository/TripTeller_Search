## 텍스트 입력 후 불용어 제거

기본 흐름:

1. 텍스트 언어 인식 (영어/한국어) `langid`
- 영어일 경우: 불용어 처리 `NLTK`
- 한국어일 경우: `konlpy`를 이용하여 토큰화 후 불용어 및 조사를 제거
2. 불용어 리스트를 불러와서 해당 단어들을 제거
3. 남은 단어 반환: 남은 단어들을 반환하고, 이를 DB 검색을 위해 `%단어%` 형태로 변환

---

### 참고 링크
- [코엔엘파이(KoNLPy) 공식문서](https://konlpy.org/ko/v0.4.3/)
- [파이썬 텍스트마이닝 윈도우에 코엔엘파이 설치 방법](https://blog.naver.com/kimsun2005/223278430054
)
- [토닥토닥 sklearn - 텍스트를 위한 머신러닝 - 불용어 제거](https://wikidocs.net/77135)

-----

