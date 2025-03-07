import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.conn.row_factory = sqlite3.Row
            return self.conn
        except Error as e:
            print("Błąd połączenia:", e)
        return None

    def close(self):
        if self.conn:
            self.conn.close()

    def execute_query(self, query, params=None):
        try:
            cur = self.conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            self.conn.commit()
            return cur
        except Error as e:
            print("Błąd wykonania zapytania:", e)
            return None

    def create_tables(self, tables_sql):
        for sql in tables_sql:
            self.execute_query(sql)

    def insert_record(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cur = self.execute_query(query, tuple(data.values()))
        return cur.lastrowid if cur else None

    def fetch_combobox_values(self, table, column):
        query = f"SELECT DISTINCT {column} FROM {table}"
        cur = self.execute_query(query)
        if cur:
            rows = cur.fetchall()
            return [row[column] for row in rows]
        return []

    def count_records(self, table):
        query = f"SELECT COUNT(*) as count FROM {table}"
        cur = self.execute_query(query)
        if cur:
            row = cur.fetchone()
            return row["count"]
        return 0
