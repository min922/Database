import pymysql
import pandas as pd

def rent_returnfct(lib):
    while True:
        con = pymysql.connect(host='localhost', user='root',
                              password='password', db='librarydb',
                              charset='utf8', autocommit=True,
                              cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()

        sel = input(
            """원하는 작업을 선택해주세요.
1. 책 대출
2. 책 반납
프로그램을 종료하려면 q를 눌러주세요.\n""")

        if sel == "1":
            while True:
                user_name, user_num = input("사용자의 이름과 핸드폰 번호 뒷자리를 입력해주세요.\n").split()
                sql = "select * from userinfo where NAME = '" + user_name + "' and PHONENUM like '_______" + user_num + "'"
                cur.execute(sql)
                rows = cur.fetchall()
                result = pd.DataFrame(rows)
                if len(result) == 0:
                    print("잘못된 회원정보 입니다. 다시 입력해주세요.")
                else:
                    sql = "select AVAILABLE from userinfo where NAME = '" + user_name + "' and PHONENUM like '_______" + user_num + "'"
                    cur.execute(sql)
                    rows = cur.fetchall()
                    user = pd.DataFrame(rows)
                    if int(user["AVAILABLE"]) == 0:
                        print("대출 가능 권수를 넘어 대출이 불가능합니다.")
                        break
                    else:
                        inp = input("대출 할 책의 제목을 입력해주세요.\n")
                        sql = "update librarydb.connect set qty = qty - 1 where libcode = " + str(
                            lib) + " and bookcode in (select bcode from book where title like '%" + inp + "%')"
                        cur.execute(sql)  # 대출하는 책의 재고를 줄임
                        sql = "update librarydb.userinfo set AVAILABLE = AVAILABLE - 1 where NAME = '" + user_name + "' and PHONENUM like '_______" + user_num + "'"
                        cur.execute(sql)  # 대출하는 사용자의 대출 가능 권수를 줄임
                        sql = "select * from userinfo"
                        cur.execute(sql)  # 사용자의 정보를 보여줌
                        rows = cur.fetchall()
                        user = pd.DataFrame(rows)
                        print(user)
                        con.close()
                        break
        elif sel == "2":
            while True:
                user_name, user_num = input("사용자의 이름과 핸드폰 번호 뒷자리를 입력해주세요.\n").split()
                sql = "select * from userinfo where NAME = '" + user_name + "' and PHONENUM like '_______" + user_num + "'"
                cur.execute(sql)
                rows = cur.fetchall()
                result = pd.DataFrame(rows)
                if len(result) == 0:
                    print("잘못된 회원정보 입니다. 다시 입력해주세요.\n")
                else:
                    sql = "select AVAILABLE from userinfo where NAME = '" + user_name + "' and PHONENUM like '_______" + user_num + "'"
                    cur.execute(sql)
                    rows = cur.fetchall()
                    user = pd.DataFrame(rows)
                    if int(user["AVAILABLE"]) > 5:
                        print("대출 오류입니다.")
                        break
                    else:
                        inp = input("반납 할 책의 제목을 입력해주세요.\n")
                        sql = "update librarydb.connect set qty = qty + 1 where libcode = " + str(
                            lib) + " and bookcode in (select bcode from book where title like '%" + inp + "%')"
                        cur.execute(sql)  # 반납하는 책의 재고를 늘임
                        sql = "update librarydb.userinfo set AVAILABLE = AVAILABLE + 1 where NAME = '" + user_name + "' and PHONENUM like '_______" + user_num + "'"
                        cur.execute(sql)  # 반납하는 사용자의 대출 가능 권수를 늘임
                        sql = "select * from userinfo"
                        cur.execute(sql)  # 사용자의 정보를 보여줌
                        rows = cur.fetchall()
                        user = pd.DataFrame(rows)
                        print(user)
                        con.close()
                        break
        elif sel == "q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("다시 입력해주십시오.")
