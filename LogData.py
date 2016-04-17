import sqlite3
import sys
import json

class LogData():
    def __init__(self):
        self.conn = sqlite3.connect('loggeddata.db')
        self.cursor = self.conn.cursor()
        self.conn.execute('CREATE TABLE IF NOT EXISTS LoggedData(datetime , action TEXT)')

    def add_data(self, action):
        self.cursor.execute("INSERT INTO LoggedData (datetime, action) VALUES (CURRENT_TIMESTAMP, ?)", [action])
        self.commit()

    def print_data(self):
        row = self.cursor.execute("SELECT action, datetime FROM LoggedData")
        for col in row:
            print(col)

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.conn.close()


    def get_data(self):
        self.cursor.execute("SELECT action, datetime FROM LoggedData")
        record = self.cursor.fetchall()
        l = []
        for r in record:
            d = {'action' : r[0],
                 'time' : r[1]}
            l.append(d)

        return json.dumps({"record": l})

    def get_json(self):
        pass

if __name__ == "__main__":
    logdata = LogData()
    logdata.print_data()
    print(logdata.get_data())