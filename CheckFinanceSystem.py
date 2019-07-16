import pymysql
import pandas as pd
import os


def cls():
    print("\n" * 100)


# now, to clear the screen

def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s


class maintSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        cls()
        obj1 = inputdSwitch()
        print("1. 회사입력   2.시세입력   3.코스피입력   ")
        obj1.switch(input("input: "))

    def case_2(self):
        cls()
        obj1 = delSwitch()
        print("1. 회사삭제  2.시세삭제   3.코스피삭제   ")
        obj1.switch(input("input: "))

    def case_3(self):
        cls()
        obj1 = updatedSwitch()
        print("1. 회사수정    2.시세수정     3.코스피수정   ")
        obj1.switch(input("input: "))

    def case_4(self):
        cls()
        obj1 = searchdSwitch()
        print("1. 회사검색    2.시세검색     3.코스피검색   ")
        obj1.switch(input("input: "))


class inputdSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        cls()
        try:
            print("회사 입력 (ISIN, 회사이름, 시가총액, 시가총액 순위)")
            data = input("input: ")
            data = data.split(',')
            sql = "insert into company values (%s, %s, %s, %s)"

            curs.execute(sql, (int(data[0]), data[1], int(data[2]), int(data[3])))
            conn.commit()

            SQL = "select * from company where ISIN=%s" % int(data[0])
            df = pd.read_sql(SQL, conn)
            print(df)
            print("성공 1")
            print()
        finally:
            conn.close()

    def case_2(self):
        cls()
        try:
            print("시세 입력 (MP날짜, 종가, 전일비, 시가, 고가, 저가, 거래량, ISO)")
            data = input("input: ")
            data = data.split(',')
            sql = "INSERT INTO daymarkepprice(MP날짜,종가,전일비,시가,고가, 저가,거래량,ISO) values(%s, %s, %s, %s, %s, %s, %s, %s)"

            curs.execute(sql, (data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])
                               , int(data[6]), int(data[7])))
            conn.commit()
            sql = """select C.회사이름, C.ISIN, D.MP날짜, D.종가, D.전일비, D.고가, D.저가, D.거래량 from company C inner join daymarkepprice D where 
                       C.ISIN =D.ISO and D.MP날짜='%s' """ % data[0]
            df = pd.read_sql(sql, conn)
            print(df)
            print("성공 1")
        finally:
            conn.close()

    def case_3(self):
        try:
            print("코스피 입력(날짜, 체결가, 전일비, 등락률)")
            data = input("input: ")
            data = data.split(',')
            sql = "INSERT INTO cospi values(%s, %s, %s, %s)"

            curs.execute(sql, (data[0], float(data[1]), float(data[2]), float(data[3])))
            conn.commit()
            sql = "select * from cospi where CP날짜='%s'" % data[0]
            df = pd.read_sql(sql, conn)
            print(df)
            print("성공 1")
        finally:
            conn.close()


class delSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        cls()
        try:
            print("회사 삭세 (ISIN)")
            data = int(input("input: "))
            sql = "delete from company where ISIN=%s"
            curs.execute(sql, data)
            conn.commit()
            print("성공 1")
        finally:
            conn.close()

    def case_2(self):
        cls()
        try:
            print("시세 삭제 (ISO, MP날짜)")
            data = input("input: ")
            data = data.split(',')
            sql = "delete from daymarkepprice where ISO=%s and MP날짜=%s"
            curs.execute(sql, (int(data[0]), data[1]))
            conn.commit()
            print("성공 1")
        finally:
            conn.close()

    def case_3(self):
        try:
            print("코스피 삭제(날짜입력)")
            data = input("input: ")
            data = data.split(',')
            sql = "delete from cospi where CP날짜=%s"
            curs.execute(sql, (data[0]))
            conn.commit()
            print("성공 1")
        finally:
            conn.close()


class updatedSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        cls()
        try:
            print("회사 수정 (ISIN, [CompanyName, 시가총액, 시가총액 순위])")
            data = input("input: ")
            data = data.split(',')
            sql = "update company set 회사이름=%s, 시가총액=%s, `시가총액 순위`=%s where ISIN=%s"
            curs.execute(sql, (data[1], int(data[2]), int(data[3]), int(data[0])))
            conn.commit()
            SQL = "select * from company where ISIN=%s" % int(data[0])
            df = pd.read_sql(SQL, conn)
            print(df)
            print("성공 1")
            print()

        finally:
            conn.close()

    def case_2(self):
        cls()
        try:
            print("시세 수정 (MP날짜, 종가, 전일비, 시가, 고가, 저가, 거래량, ISO)")
            data = input("input: ")
            data = data.split(',')
            sql = "update daymarkepprice set MP날짜=%s, 종가=%s, 전일비=%s, 시가=%s, 고가=%s, 저가=%s, 거래량=%s where ISO=%s"
            curs.execute(sql, (data[0], int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])
                               , int(data[6]), int(data[7])))
            conn.commit()
            sql = """select C.회사이름, C.ISIN, D.MP날짜, D.종가, D.전일비, D.고가, D.저가, D.거래량 from company C inner join daymarkepprice D where 
                                   C.ISIN =D.ISO and D.MP날짜='%s'and D.ISO=%s """ % (data[0], int(data[7]))
            df = pd.read_sql(sql, conn)
            print(df)
            print("성공 1")
        finally:
            conn.close()

    def case_3(self):
        cls()
        try:
            print("코스피 수정(날짜, 체결가, 전일비, 등락률 입력)")
            data = input("input: ")
            data = data.split(',')
            sql = "update cospi set CP날짜=%s, `코스피 체결가`=%s, `코스피 전일비`=%s, `코스피 등락률`=%s where CP날짜=%s"
            curs.execute(sql, (data[0], float(data[1]), float(data[2]), float(data[3]), (data[0])))
            conn.commit()
            sql = "select * from cospi where CP날짜='%s'" % data[0]
            df = pd.read_sql(sql, conn)
            print(df)
            print("성공 1")
        finally:
            conn.close()


class searchdSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        cls()
        try:
            print("*******한 회사를 조회********")
            m1 = input("조회할 종목코드 입력: ")
            SQL = "select * from company where ISIN="
            df = pd.read_sql(SQL + m1, conn)
            print(df)
            print()
        finally:
            conn.close()

    def case_2(self):
        cls()
        print("1. 하나의 회사 시세를 날짜별로 조회")
        print("2. 어떤 하루 회사들의 시세들 중에서 최고 최저의 시세를 조회")
        print("3. 두 회사의 시세 정보 비교 조회")
        print("4. 날짜 별 종가의 평균, 최대 종가 조회")
        obj1 = searchdPriceSwitch()
        obj1.switch(input("input: "))

    def case_3(self):
        cls()
        print("1.어떤 하루의 코스피를 조회(오늘의 증시)")
        print("2.최고 최저 코스피 조회")
        obj1 = searchCospidSwitch()
        obj1.switch(input("input: "))


class searchdPriceSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        cls()
        try:
            print("하나의 회사 시세를 날짜별로 조회")
            data = input("회사이름 입력: ")
            data = data.split(',')
            sql = """select C.회사이름, C.ISIN, D.MP날짜, D.종가, D.전일비, D.고가, D.저가, D.거래량 from company C inner join daymarkepprice D where 
            (select C.ISIN where 회사이름='%s')=D.ISO order by MP날짜 desc""" % data[0]
            df = pd.read_sql(sql, conn)
            print(df)
            print()
            conn.commit()
        finally:
            conn.close()

    def case_2(self):
        cls()
        try:
            print("어떤 하루 회사들의 시세들 중에서 최고 최저의 시세를 조회")
            data = input("날짜입력(XXXX-XX-XX) : ")
            print(data)
            sql = """SELECT C.회사이름, C.ISIN, D.MP날짜, max(D.종가) as MAX종가 from company C inner join daymarkepprice D where D.MP날짜='%s' and C.ISIN=D.ISO and D.종가=(select  MAX(D.종가) from daymarkepprice  D where D.MP날짜='%s')
    """ % (data, data)
            sql1 = """SELECT C.회사이름, C.ISIN, D.MP날짜, min(D.종가) as MIN종가 from company C inner join daymarkepprice D where D.MP날짜='%s' and C.ISIN=D.ISO and D.종가=(select  min(D.종가) from daymarkepprice  D where D.MP날짜='%s')
            """ % (data, data)
            df = pd.read_sql(sql, conn)
            print(df)
            df = pd.read_sql(sql1, conn)
            print(df)
            print()
        finally:
            conn.close()

    def case_3(self):
        cls()
        try:
            print("두 회사의 시세 정보 비교 조회")
            company1 = input("첫번째 회사의 회사이름 입력: ")
            company2 = input("두번째 회사의 회사이름 입력: ")
            data = input("종가, 고가, 저가, 거래량중에 선택: ")
            data1 = data
            sql = """select D1.MP날짜, C1.회사이름, C1.ISIN, D1.%s, c2.회사이름, C2.ISIN, D2.%s from company C1 , company C2 inner join daymarkepprice D1, daymarkepprice D2 where C1.회사이름='%s' and C2.회사이름='%s' and D1.MP날짜=D2.MP날짜 and c1.ISIN=D1.ISO and c2.ISIN=D2.ISO""" % (
                data, data1, company1, company2)
            df = pd.read_sql(sql, conn)
            print(df)
            print()
        finally:
            conn.close()

    def case_4(self):
        cls()
        try:
            print("날짜 별 종가의 평균, 최대 종가 조회")
            sql = """select D.ISO, C.회사이름, avg(D.종가) as AVG종가, max(D.종가) as MAX종가 from company C inner join daymarkepprice D where C.ISIN=D.ISO group by D.ISO
    """
            df = pd.read_sql(sql, conn)
            print(df)
            print()
        finally:
            conn.close()


class searchCospidSwitch:
    def switch(self, arg):
        self.case_name = "case_" + str(arg)
        self.case = getattr(self, self.case_name, lambda: "default")
        return self.case()

    def case_1(self):
        try:
            print("어떤 하루의 코스피를 조회(오늘의 증시)")
            data = input("CP날짜(XXXX-XX-XX) : ")
            sql = "select * from cospi where CP날짜='%s'" % data
            df = pd.read_sql(sql, conn)
            print(df)
        finally:
            conn.close()

    def case_2(self):
        try:
            print("최고 최저 코스피 조회")
            sql = """select C.CP날짜, max(C.`코스피 체결가`) as `MAX코스피체결가`, D.CP날짜, min(D.`코스피 체결가`) as `MIN코스피체결가`  
                from cospi C , cospi D
                where C.`코스피 체결가`=(select  MAX(`코스피 체결가`) from cospi  F)
                and D.`코스피 체결가`=(select  min(`코스피 체결가`) from cospi E)"""

            df = pd.read_sql(sql, conn)
            print(df)
            # sql = "select CP날짜,min(`코스피 체결가`) as `MIN코스피 체결가` from cospi C where `코스피 체결가`=(select  MIN(`코스피 체결가`) from cospi  D)"
            # df = pd.read_sql(sql, conn)
            # print(df)
        finally:
            conn.close()


obj = maintSwitch()

ip = 0
print("------------------------------------------------------------")
print("------------------------금융 프로그램-----------------------")
print("------------------------------------------------------------")

while (True):
    conn = pymysql.connect(host='localhost', user='root', password='사용자의 비밀번호를 입력하세요..',
                           db='finance', charset='utf8')
    curs = conn.cursor()
    print("1. 입력       2.삭제       3.수정       4.조회       5.종료 ")
    ip = input("시작: ")
    if ip == "5":
        break
    obj.switch(ip)

conn.close()
