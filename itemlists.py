import pymysql

def sql_exe(query):
    db_conn = pymysql.connect(
        user='staff', 
        passwd='algoalgo-staff', 
        host='34.64.120.154', 
        db='algoalgo', 
        charset='utf8'
    )   

    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute(query)

        result = cursor.fetchall()            

        db_conn.commit()
        db_conn.close()

        return result 
    
    except Exception as ex:
        raise ex

# 소유한 아이템 출력->
def useitem(author):
    sql = "select items from member where discord_id='{str(author)}'"
    try:
        sql_result=sql_exe(sql)
        # 인덱스. 아이템명 : 소유 개수 형식의 리스트 출력해야함
        return "[*] success print item {author}", sql_result
    except Exception as ex:
        return "[!] error finding your info: {ex}"

    