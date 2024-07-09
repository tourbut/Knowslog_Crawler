# Knowslog_Crawler
AI관련 포스팅 및 뉴스 수집

## 프로세스
- 주제 관련 게시글 수집 > 한국어 번역,요약 > 임베딩 및 벡터 저장 > 일단위 요약 페이지 작성(Markdown)


## 수집 대상
- https://www.bloomberg.com/
- https://www.marktechpost.com/
- https://www.theguardian.com
- https://arstechnica.com
- https://news.google.com/

## 기능 정의
- 사용자 정보
    - 관심 키워드 CRUD
    - 이메일 수신여부
    - 이메일 주소
    - 디스코드 등록 여부
    - LLM 모델 선택
    - LLM API 키
- 관심 키워드 뉴스검색어 생성(LLM)
- 뉴스 검색
- 검색 결과 번역(CRUD)
- 검색 결과 요약(CRUD)
- 디스코드 발송 
- 사용자 메일 수신여부 CRUD
- 메일 발송
- 디스코드 채팅 메시지로 입력 받은 내용 수행
    - 사용자 정보 체크, API 키 암호화 등록
    - url인경우 해당 url 내용 번역 및 요약(CRUD)
    - html인 경우 그대로 번역 및 요약(CRUD)
    - medium post인 경우 medium 크롤러 사용, 번역 및 요약(CRUD) 
    - 데이터 베이스 기반 사용자 질의 응답
    - 블로그 포스팅 작성
    - 사용자 관심 키워드 저장