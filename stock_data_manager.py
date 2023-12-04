import sqlite3

def create_db(obObj, str):
    # 連接到 SQLite 資料庫
    # 創建一個新表來存儲股票交易資料
    cursor = obObj.cursor()

    obObj.execute(str)
    # 提交事務
    obObj.commit()
    cursor.close()



