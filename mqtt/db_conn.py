import pymysql

class Database():
    def __init__(self):
        # self.db_class = Database()
        self.db = pymysql.connect(host='<데이터베이스 이름>',
                                  user='<사용자 id>',
                                  password='<PASSWD>',
                                  db='silver_db',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def executeAll(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def commit(self):
        self.db.commit()

    def select(self, table):
        sql = "SELECT * FROM silver_db." + table
        row = self.executeAll(sql)
        return row

    def select_s_id(self, table, s_id):
        sql = "SELECT * FROM silver_db." + table + " where s_id=" + s_id
        row = self.executeAll(sql)
        return row

    def insert_fire(self, table, a, b, c):
        sql = "INSERT INTO silver_db." + table + "(w_id, s_id, f_detect ) VALUES ('%d', '%d', '%s')" % (
        a, b, c)
        self.execute(sql)
        self.commit()

    def insert_heartRate(self, table, a, b, c):
        sql = "INSERT INTO silver_db." + table + "(w_id, s_id, h_rate ) VALUES ('%d', '%d', '%s')" % (
        a, b, c)
        self.execute(sql)
        self.commit()

    def insert_dht(self, table, a, b, c, d):
        sql = "INSERT INTO silver_db." + table + "(w_id, s_id, dht_temp, dht_humi ) VALUES ('%d', '%d', '%s', '%s')" % (
        a, b, c, d)
        self.execute(sql)
        self.commit()
