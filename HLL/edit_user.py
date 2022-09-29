import pymysql
import pandas as pd

def userinfofct(lib):
    while True:
        con = pymysql.connect(host='localhost', user='root', password='password',
                              db='librarydb', charset='utf8',
                              autocommit=True, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()

        sel = input("""수정하려는 사용자의 ID를 입력해주세요.
수정을 종료하려면 q를 눌러주십시오.\n""")

        if sel == "q":
            print("수정을 종료합니다.")
            break
        else:
            sql = "select * from userinfo where ID like '" + sel + "'"
            cur.execute(sql)
            rows = cur.fetchall()
            result = pd.DataFrame(rows)
            if len(result) == 0:
                print("입력한 ID에 해당하는 회원이 없습니다.")
            else:
                while True:
                    edit = input("""어떤 정보를 수정하시겠습니까?
1. ID
2. 이름
3. 휴대폰 번호
종료하려면 q를 눌러주세요.\n""")
                    if edit == "1":
                        new_edit = input("변경 할 아이디를 입력해주세요.")
                        sql = "update userinfo set ID = '" + new_edit + "' where ID like '" + sel + "'"
                        cur.execute(sql)
                        sel = new_edit
                        sql = "select * from userinfo"
                        cur.execute(sql)
                        rows = cur.fetchall()
                        user = pd.DataFrame(rows)
                        print(user)
                        con.close()
                        break
                    elif edit == "2":
                        new_edit = input("변경 할 이름을 입력해주세요.")
                        sql = "update userinfo set NAME = '" + new_edit + "' where ID like '" + sel + "'"
                        cur.execute(sql)
                        sql = "select * from userinfo"
                        cur.execute(sql)
                        rows = cur.fetchall()
                        user = pd.DataFrame(rows)
                        print(user)
                        con.close()
                        break
                    elif edit == "3":
                        new_edit = input("변경 할 휴대폰 번호를 입력해주세요.")
                        sql = "update userinfo set PHONENUM = '" + new_edit + "' where ID like '" + sel + "'"
                        cur.execute(sql)
                        sql = "select * from userinfo"
                        cur.execute(sql)
                        rows = cur.fetchall()
                        user = pd.DataFrame(rows)
                        print(user)
                        con.close()
                        break
                    elif sel == "q":
                        print("프로그램을 종료합니다.")
                        break
                    else:
                        print("다시 입력 해주세요.")
