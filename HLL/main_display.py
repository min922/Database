import pymysql
import pandas as pd

from rent_return import *
from search import *
from search_lib import *
from edit_user import *

lib = int(input("현재 계신 도서관의 코드를 입력해주세요.\n"))

while True:
    main_sel = input(
    """사서님, 원하는 작업을 선택해 주세요.
1. 대여 및 반납 처리
2. 책 검색
3. 도서관 재고 검색
4. 사용자 정보 수정
프로그램을 종료하시려면 q를 눌러주세요.\n""")
    
    if main_sel == "1":
        rent_returnfct(lib)
    elif main_sel == "2":
        searchfct(lib)
    elif main_sel == "3":
        searchlibfct(lib)
    elif main_sel == "4":
        userinfofct(lib)
    elif main_sel == "q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("다시 입력해주십시오.")
        
