import pymysql
import pandas as pd

def searchfct(lib):
    while True:
        con = pymysql.connect(host='localhost', user='root', password='password',
                              db='librarydb', charset='utf8',
                              autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()

        sel = input("""어떤 것으로 찾으시겠습니까?
1. 책 제목
2. 저자
검색을 종료하려면 q를 눌러주십시오.\n""")

        if sel == "1":
            search_title = input("찾고 싶은 책의 제목을 입력해주세요.")
            sql = "select title, author, qty from book, connect where bcode = bookcode and libcode = " + str(
                lib) + " and title like '%" + search_title + "%'"
            cur.execute(sql)  # 검색하고자 하는 책의 제목, 저자, 해당 도서관에서의 재고를 보여줌
            rows = cur.fetchall()
            result = pd.DataFrame(rows)
            if len(result) == 0:
                print("검색 결과가 없습니다.")
            else:
                for i in range(len(result)):
                    result = result.rename(columns={'title': "책 제목", "author": "저자", 'qty': "재고"})                    
                    print(result.loc[i])
                    print("")

            con.close()
        elif sel == "2":
            search_author = input("찾고 싶은 책의 저자를 입력해주세요.")
            sql = "select title, author, qty from book, connect where bcode = bookcode and libcode = " + str(
                lib) + " and author like '%" + search_author + "%'"
            cur.execute(sql)  # 검색하고자 하는 책의 제목, 저자, 해당 도서관에서의 재고를 보여줌
            rows = cur.fetchall()
            result = pd.DataFrame(rows)
            if len(result) == 0:
                print("검색 결과가 없습니다.")
            else:
                for i in range(len(result)):
                    result = result.rename(columns={'title': "책 제목", "author": "저자", 'qty': "재고"})
                    print(result.loc[i])
                    print("")

            con.close()
        elif sel == "q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("다시 입력해주세요.")
