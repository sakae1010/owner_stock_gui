import sqlite3

def create_db(obObj, str):
    # 連接到 SQLite 資料庫
    # 創建一個新表來存儲股票交易資料
    cursor = obObj.cursor()
    # 創建一個新表來存儲股票交易資料
    cursor.execute('''
    # CREATE TABLE IF NOT EXISTS stock_trades (
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     trade_date TEXT NOT NULL,
    #     stock_symbol TEXT NOT NULL,
    #     quantity INTEGER NOT NULL,
    #     price_per_share REAL NOT NULL,
    #     total_cost REAL NOT NULL
    # )
    ''')
    obObj.execute(str)
    # 提交事務
    obObj.commit()
    cursor.close()



