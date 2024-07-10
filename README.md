# 영화 리뷰 사이트

## 🖥️ 프로젝트 소개
사용자가 입력한 리뷰데이터를 분석하여 자동으로 별점을 부여하여 리뷰를 등록하는 사이트

## 🕰️ 개발 기간
* 2023.9.1 - 2023.12.13

### 🧑‍🤝‍🧑 맴버구성
 - 손기완(조장) : 모델 구현 및 튜닝, 팀 일정 조율
 - 한진우 : ppt 및 보고서 문서 작성
 - 이태경 : 웹 페이지 디자인 및 구현
 - 조민지 : 서버 구현, 데이터 통신 및 처리
   
### ⚙️ 개발 환경
- `Python 3.11.5`
- `jQuery 3.6.4`
- `tensorflow 2.15.0`
- **IDE** : Visual Studio Code (1.84.2)
- **Framework** : Flask (2.2.2)

## 📌 주요 기능
#### 프론트앤드
- DB값 검증
   -어ㅓㄹ
- ID찾기, PW찾기
- 로그인 시 쿠키(Cookie) 및 세션(Session) 생성
#### 회원가입 - <a href="https://github.com/chaehyuenwoo/SpringBoot-Project-MEGABOX/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Member)" >상세보기 - WIKI 이동</a>
- 주소 API 연동
- ID 중복 체크
#### 마이 페이지 - <a href="https://github.com/chaehyuenwoo/SpringBoot-Project-MEGABOX/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Member)" >상세보기 - WIKI 이동</a>
- 주소 API 연동
- 회원정보 변경

#### 영화 예매 - <a href="https://github.com/chaehyuenwoo/SpringBoot-Project-MEGABOX/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(%EC%98%81%ED%99%94-%EC%98%88%EB%A7%A4)" >상세보기 - WIKI 이동</a>
- 영화 선택(날짜 지정)
- 영화관 선택(대분류/소분류 선택) 및 시간 선택
- 좌석 선택
- 결제 페이지
- 예매 완료
#### 메인 페이지 - <a href="https://github.com/chaehyuenwoo/SpringBoot-Project-MEGABOX/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(%EB%A9%94%EC%9D%B8-Page)" >상세보기 - WIKI 이동</a>
- YouTube API 연동
- 메인 포스터(영화) 이미지 슬라이드(CSS)
#### 1대1문의 및 공지사항 - <a href="" >상세보기 - WIKI 이동</a> 
- 글 작성, 읽기, 수정, 삭제(CRUD)

#### 관리자 페이지 
- 영화관 추가(대분류, 소분류)
- 영화 추가(상영시간 및 상영관 설정)
