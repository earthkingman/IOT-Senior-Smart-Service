import pymysql

class Database():
    def __init__(self):
        # self.db_class = Database()
        self.db = pymysql.connect(host='',
                                  user='',
                                  password='',
                                  db='',
                                  charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
 
    def executeAll(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchall()
        return row
    
    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def commit(self):
        self.db.commit()

    def select(self,table):
         sql = "SELECT * FROM silver_db."+table+";"
         row = self.executeAll(sql)
         return row


    def distinctselect(self,table):
         sql = " SELECT DISTINCT s_id FROM silver_db."+table+";"    
         row = self.executeAll(sql)
         return row

    def select_s_id(self,table,s_id):
         sql = "SELECT * FROM silver_db."+table+" where s_id="+s_id+";"
         row = self.executeAll(sql)
         return row


    def delete_fire(self,table,s_id):
         sql = "delete  FROM silver_db."+table+" where s_id="+s_id+";"
         row = self.executeAll(sql)
         self.commit()  
         return row


    def insert(self,table,a,b,c,d):
        sql = "INSERT INTO silver_db."+table+"(w_id, s_id, message, m_type ) VALUES ('%d', '%d', '%s','%s');" % (a, b, c,d)
        self.execute(sql)
        self.commit()
        
    
    def insert_register(self,a,b,c,d,e,f):
        sql = "INSERT INTO silver_db.silver(s_name, s_yymmdd, s_address, s_image, s_cautions, s_tel) VALUES ('%s', '%s', '%s','%s','%s','%s');" % (a, b, c,d,e,f)
        print(sql)
        self.execute(sql)
        self.commit()
    
    def db_close(self):
        self.db.close()