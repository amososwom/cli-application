import sqlite3

class DbHandler:
    def __init__(self):
        self._conn = sqlite3.connect("./lib/backend/token-trader.db")
        self._cursor = self._conn.cursor()
        self.create_tables()


    def create_tables(self):
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                uid TEXT PRIMARY KEY,
                                uname TEXT,
                                password TEXT
                            );''')

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                trans_id TEXT PRIMARY KEY,
                                trans_uid TEXT,
                                trans_type TEXT,
                                trans_token TEXT,
                                trans_date TEXT DEFAULT CURRENT_DATE,
                                trans_state TEXT DEFAULT '0',
                                FOREIGN KEY (trans_uid) REFERENCES users(uid) ON DELETE CASCADE
                            );''')

        self._cursor.execute('''CREATE TABLE IF NOT EXISTS balances (
                                b_uid TEXT PRIMARY KEY,
                                b_amount TEXT DEFAULT '0',
                                b_token TEXT DEFAULT '0',
                                FOREIGN KEY (b_uid) REFERENCES users(uid) ON DELETE CASCADE
                            );''')
        
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS markets (
                                m_id TEXT PRIMARY KEY,
                                m_uid TEXT,
                                m_token TEXT,
                                m_type TEXT,
                                m_date TEXT,
                                FOREIGN KEY (m_uid) REFERENCES users(uid) ON DELETE CASCADE
                            );''')

        self._conn.commit()

    def insert_records(self, table, data):

        placeholder = ','.join(['?'] * len(data))
        columns = ','.join(data.keys())
        values = tuple(data.values())
        print(values)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholder})"
        
        try:
            self._cursor.execute(query, values)
            self._conn.commit()
            return [{"status": True}]
        
        except sqlite3.Error as e: 
            self._conn.rollback()
            print(f"Error: {str(e)}")
            return [{"status": False}, {"error": str(e)}]
        
    def select_records(self, tables, where = None):


        if not where:
            query = f"SELECT * FROM {tables}"
        else:
            conctinatedkey = ' AND '.join([f"{value} = ? " for value in where.keys()])

            query = f"SELECT * FROM {tables} WHERE {conctinatedkey}"

            conctinatedvalue = tuple(where.values())
            print(query)
            print(conctinatedvalue)

        try: 
            self._cursor.execute(query, conctinatedvalue)
            data = self._cursor.fetchall()
            print(data)

            return data if data else []
        
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


