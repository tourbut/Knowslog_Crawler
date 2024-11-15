import oracledb


# Oracle DB에 연결
connection = oracledb.connect(
    user="NHIMC_APP",
    password="nhimc_dev1104",
    dsn="192.168.3.171:1521/NHIMCDEV"
)


# 커서 생성
cursor = connection.cursor()

# SQL 쿼리 실행
cursor.execute("""
               SELECT A1.USID                                 -- 사용자ID
     , A1.USER_NM                              -- 사용자명
  , A1.USER_ENGL_NM                         -- 사용자영문명
  , A1.PW                                   -- 비밀번호
  FROM AZCMMUSER A1
 WHERE A1.USID = '204415' -- 사번 넣어줄것
   AND TO_CHAR(SYSDATE, 'YYYYMMDD') BETWEEN A1.USER_STR_DY AND A1.USER_END_DY
               """)
rows = cursor.fetchall()

# 결과 출력
for row in rows:
    print(row)

# 연결 해제
cursor.close()
connection.close()
