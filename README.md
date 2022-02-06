# :: Suulgo Project ::
- 술고 = "코딩하다 지친 당신... 술GO?"라는 컨셉의 위코더 매칭(위코드 내 커뮤니티, 매칭서비스, 약속잡기 등) 서비스
- 실제 유저들을 가입시켜 정상적으로 서비스가 동작하는 것을 확인하였습니다.
- 개발은 초기 세팅부터 직접 구현했으며 MVP를 따라 최소 이용가능한 제품단위로 개발을 진행하였습니다.
- [술고 사이트 시영상](https://www.youtube.com/watch?v=AnpIbkjwnLs&feature=youtu.be)

## [팀 소개]
### Front-end
[Suulgo- Frontend Repo](https://github.com/wecode-bootcamp-korea/27-2nd-SUULGO-frontend)

### Back-end
😎 김은찬 - 상세페이지 뷰(유저정보봔한), 약속(미팅)요청 뷰, 매칭리스트(매칭포인트가 가장 높은순으로 회원 리스트 반환) <br/>
🍗 길동화 - 소셜로그인 뷰(회원가입/로그인), 마이페이지 뷰(본인정보 반환), AWS 서버 배포<br/>
👻 유현이 - 회원리스트 뷰(술종류에 맞는 유저 리스트반환), 설문조사뷰(로그인 직후 서베이에 항목 db저장)<br/>

### 개발 기간
2021.12.13 ~ 2021.12.24

## [기술 스택]
### 사용 기술
Django, Python, MySQL, jwt, bcrypt, AWS(EC2, RDS), Git, Notion(kanban)

### ERD
<img width="1018" src="https://user-images.githubusercontent.com/92412962/147327052-61887084-fbcc-4f9e-b9f1-2305610e0ef1.png">

## Reference
- [API Document](https://documenter.getpostman.com/view/18513651/UVRAK7eQ#c2444f8b-25dd-4a80-b8f0-9ff4873558f8)
- 이 프로젝트는 [숨고](https://soomgo.com/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.

<br />

# :: Refactoring ::
- 2022.2.2 : 매칭알고리즘을 평균 가중치가 아닌 개인별 가중치로 로직 변경
