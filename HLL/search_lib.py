import pymysql
import pandas as pd

def searchlibfct(lib):
    while True:
        con = pymysql.connect(host='localhost', user='root', password='password',
                              db='librarydb', charset='utf8',
                              autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()

        sel = input("""도서 재고를 검색하려는 도서관 명을 입력해주십시오.
검색을 종료하려면 q를 눌러주십시오.\n""")

        if sel == "q":
            print("검색을 종료합니다.")
            break
        else:
            sql = "select lname, title, author, qty from connect, library, book where libcode = lcode and bookcode = bcode and lname like '%" + sel + "%'"
            cur.execute(sql)
            rows = cur.fetchall()
            result = pd.DataFrame(rows)
            if len(result) == 0:
                print("검색어에 해당하는 도서관이 없습니다.")
            else:
                for i in range(len(result)):
                    result = result.rename(columns={'lname': "도서관 명", "title": "제목", "author": "저자", 'qty': "재고"})
                    print(result.loc[i])
                    print("")


