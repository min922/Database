# Database

## MySQL DB정보
- book table : 책의 제목과 저자, 그리고 pk인 책의 code를 나타냄.
- library table : 부천시 도서관의 이름, 주소, pk인 도서관의 code를 나타냄.
- connect table : 각 도서관이 보유하고 있는 책들의 수량을 나타냄. book table과 library table을 연결해줌. 
- userinfo table : 사용자의 정보를 저장함. ID를 pk로 가짐.

## HLL(Python에서 DB접근, 사서 전용 프로그램) 
### main_display.py
- #### 메인 프로그램
- 사용자에게 입력을 받아서 프로그램을 실행 할 수 있게 함. 
- 처음에 사용자(사서)가 근무하는 도서관의 코드를 입력 받은 후에 다른 작업들을 수행함.

### rent_return.py
- #### 도서 대여 및 반납 프로그램
- while문 안에서 데이터베이스와 연결을 해준 후 사용자에게 대출이나 반납 입력을 받음. 
- 사용자에게 이름과 휴대폰번호 뒷자리를 입력받아 회원 정보가 없다면 메시지를 띄우고 있다면 해당 사용자의 대출 가능 권수를 조회함. 
- 사용자가 존재하고 대출을 할 수 있다면 대출할 책의 제목을 입력받은 후 대출하는 책의 해당 도서관의 재고를 줄이고, 대출하는 회원의 대출 가능 권수를 줄인 후 사용자가 확인할 수 있도록 사용자의 정보를 보여준 후 종료함. 
- 반납의 경우 대출와 유사한 알고리즘을 이용함. 차이점은 반납하는 책의 재고를 늘리고, 회원의 대출 가능 권 수를 늘인다는 점임.

### search.py
- #### 도서 검색 프로그램
- 책 제목이나 저자로 검색할 수 있음. 
- 사용자가 책 제목으로 검색을 하려고 한다면 제목을 입력받고 sql문을 이용하여 메인 프로그램에서 입력받은 사용자의 도서관 코드와 같은 도서관에서의 해당 책의 정보를 보여줌. 
- like와 와일드카드를 이용하여 책의 전체 제목을 입력하지 않아도 검색이 가능하도록 만듦. 
- dataframe의 rename을 이용하여 사용자가 보기 편하게 column의 이름을 바꾸어줌. 만약 검색 결과가 없다면 메시지를 띄워줌. 
- 저자로 검색하는 프로그램도 위와 동일한 알고리즘을 사용함.

### search_lib.py
- #### 도서관 재고 검색 프로그램
- search.py와 동일한 알고리즘을 사용하여 입력받은 도서관에 있는 전체 도서의 재고를 보여줌.

### edit_user.py
- #### 회원 정보 수정 프로그램
- 사용자에게 회원의 id를 입력 받아서 회원의 정보를 수정함. 
- 만약 id가 회원 정보 데이터 베이스 상에 존재하지 않는다면 오류 메시지를 출력함. 
- 사용자에게 수정하고 싶은 정보를 입력받은 후 update를 이용하여 처음에 입력받은 id와 일치하는 회원의 정보를 수정함. 아이디, 이름, 휴대폰 번호를 수정할 수 있음. 

## Web (web언어에서 DB접근, 회원 전용 프로그램)

## app.js 
- #### ejs파일들을 연결 및 실행
- 기본 환경을 구축한 후 mysql과 node js를 연결해줌.

## main_dp.ejs 
- #### 메인 화면
- 간단한 메인 화면을 구현함. href를 이용하여 클릭시 해당 페이지로 넘어갈 수 있도록 함. 

## sign_up.ejs
- #### 회원 등록 구현
- 사용자가 입력한 정보들을 form태그를 이용해 post형식으로 DB에 보내줌.
- app.js 회원 등록 : 처음에 sign_up.ejs를 보여줌. 그 후 사용자가 입력한 데이터를 post형식으로 받음. 첫 번째 sql_check1는 ID의 중복 여부를 검사함. 
만약 sql_check1의 수행 결과가 있다면 중복된 아이디가 있는 것이므로 alert를 띄운 후 다시 원래 페이지로 돌아갈 수 있도록 함. 
sql_check1의 수행결과가 없다면 사용 가능한 ID를 입력한 것이므로 sql을 이용하여 사용자가 입력한 정보를 데이터베이스에 insert함. 
그리고 모든 사람이 5권씩 기본으로 빌릴수 있게 하기 위하여 마지막 AVAILABLE필드에는 5를 넣어둠. 
그리고 등록이 성공하면 성공 했다는 alert를 띄우고 다시 sign_up.ejs 화면을 보여줌.

## research.ejs
- #### 도서 검색 구현
- form을 이용하여 사용자에게 검색을 할 수 있게 만듦. 사용자의 입력 데이터는 post형식을 이용하여 전달함. 그리고 사용자가 검색한 결과를 app.js에서 전달받은 results라는 변수로 받아서 forEach문을 이용하여 데이터를 출력해줌.
- app.js 도서 검색 : 검색 전에는 데이터가 없어야하므로 search_val에 nothing을 입력한 sql문의 result를 출력해줌. 그리고 사용자가 검색 버튼을 누른다면 post형식으로 데이터를 받음. 
ejs의 select에서 받은 변수가 title이면 제목으로 검색을 하고 author이면 저자로 검색을 하는 if문을 만들어줌. 

## libsearch.ejs
- #### 도서관 검색 구현
- 도서 검색 화면과 동일한 알고리즘 사용

## myinfo.ejs 
- #### 내 정보 확인 구현
- 사용자에게 form으로 정보 확인용 id와 휴대폰 번호 뒷 네자리를 입력받아 본인의 정보를 조회할 수 있게 함. app.js에서 results로 데이터를 전달받아 forEach문을 이용하여 데이터를 출력함.
- app.js 내 정보 확인 : 처음에는 아무것도 띄우지 않기 위해 데이터베이스에 존재하지 않는 nothing을 입력해줌. 
그리고 사용자에게 입력받은 데이터를 post형태로 받아 ID와 핸드폰 번호가 일치하는 정보를 select해줌. 
만약 result가 없다면 해당하는 회원이 없는 것이므로 if문을 이용하여 회원 정보가 존재하지 않는다는 alert를 띄워주고 그게 아니라면 myinfo.ejs에 result를 전달해줌. 
