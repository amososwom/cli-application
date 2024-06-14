import sqlite3

from utils import * 


class DbHandler:
    def __init__(self):
        self._conn = sqlite3.connect("./lib/backend/token-trader.db")
        self._cursor = self._conn.cursor()
        self.setup()


    def setup(self):
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS decentralized (
                                token_id INTEGER PRIMARY KEY,
                                token_name TEXT,
                                token_sys TEXT,
                                token_qty INTEGER,
                                token_price INTEGER 
                            );''')
        
        self._cursor.execute('''INSERT OR IGNORE INTO decentralized (token_id, token_name, 
                                token_sys, token_qty, token_price) VALUES('7902',
                                'SHIBAINU','SHI',56200,320
                             );''')
        
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                uid TEXT PRIMARY KEY,
                                uname TEXT COLLATE NOCASE,
                                password TEXT
                            );''')

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                trans_id TEXT PRIMARY KEY,
                                trans_uid TEXT,
                                trans_type TEXT,
                                trans_token TEXT,
                                trans_date TEXT DEFAULT CURRENT_DATE,
                                trans_state TEXT DEFAULT '0',
                                FOREIGN KEY (trans_uid) REFERENCES users(uid) 
                            );''')

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS balances (
                                b_uid TEXT PRIMARY KEY,
                                b_amount INTEGER DEFAULT 0,
                                b_token INTEGER DEFAULT 0,
                                FOREIGN KEY (b_uid) REFERENCES users(uid) ON DELETE CASCADE
                            );''')
        
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS markets (
                                m_id TEXT PRIMARY KEY,
                                m_uid TEXT,
                                m_token INTEGER,
                                m_price INTEGER,
                                m_type INTEGER,
                                m_date TEXT DEFAULT CURRENT_DATE,
                                FOREIGN KEY (m_uid) REFERENCES users(uid) ON DELETE CASCADE
                            );''')

        self._conn.commit()

    def insert_records(self, table, data):

        placeholder = ','.join(['?'] * len(data))
        columns = ','.join(data.keys())
        values = tuple(data.values())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholder})"
        
        try:
            self._cursor.execute(query, values)
            self._conn.commit()
            return [{"status": True}]
        
        except sqlite3.Error as e: 
            self._conn.rollback()
            print(f"Error: {str(e)}")
            return [{"status": False}, {"error": str(e)}]
        
    def select_records(self, table, where=None):
        if not where:
            query = f"SELECT * FROM {table}"
            conctinatedvalue = ()
        else:
            conctinatedkey = ' AND '.join([f"{key} = ?" for key in where.keys()])
            query = f"SELECT * FROM {table} WHERE {conctinatedkey}"
            conctinatedvalue = tuple(where.values())

        
        try:
            self._cursor.execute(query, conctinatedvalue)
            data = self._cursor.fetchall()

            columns = [description[0] for description in self._cursor.description]

            result = []
            for row in data:
                row_dict = dict(zip(columns, row))
                result.append(row_dict)

            return result if result else []
        
        except sqlite3.Error as e:
            print(f"Error: {str(e)}")
            return []
    
    def update_records(self, table, data, where = None):

        if not where:
            return [{"status": False}, {"error": "A where Clause is needed"}]
        
        conctinatedkey = ', '.join([f"{key} = ? " for key in data.keys()])
        conctinatedvalue = ' AND '.join([f"{value} = ? " for value in where.keys()])
        query = f"UPDATE {table} SET {conctinatedkey} WHERE {conctinatedvalue}"

        values = tuple(data.values()) + tuple(where.values())

        try: 
            self._cursor.execute(query, values)
            self._conn.commit()

            return [{"status": True}]

        except sqlite3.Error as e: 
            self._conn.rollback()
            return [{"status": False}, {"error": str(e)}]
        
    def delete_records(self, table, where = None):

        if not where:
            return [{"status": False}, {"error": "A where Clause is needed"}]

        conctinatedvalue = ' AND '.join([f"{value} = ? " for value in where.keys()])
        print(conctinatedvalue)
        query = f"DELETE FROM {table} WHERE {conctinatedvalue}"

        values = tuple(where.values())

        try: 
            self._cursor.execute(query, values)
            self._conn.commit()

            return [{"status": True}]

        except sqlite3.Error as e: 
            self._conn.rollback()
            return [{"status": False}, {"error": str(e)}]
        
    def close_connection(self):
        self._cursor.close()
        self._conn.close()
        info.print_info("Connection Closed Successfully")
        
