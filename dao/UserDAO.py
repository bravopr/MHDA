from config.dbconfig import pg_config
import psycopg2
import os
from urllib import parse

class UserDAO:
    def __init__(self):
        parse.uses_netloc.append ("postgres")
        url = parse.urlparse (os.environ["postgres://kpdzooxfutqlrm:ce242d41c1020de6e60a20b96ba8352dd36b8846f227d0121e97441b93a5614f@ec2-54-221-251-195.compute-1.amazonaws.com:5432/ddr77pabo2btb2"])

        conn = psycopg2.connect (
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        #connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
        #                                                    pg_config['user'],
        #                                                    pg_config['passwd'])
        #self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join useraddress;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join useraddress where uType = 'supplier';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCustomers(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join useraddress where uType = 'customer';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
            cursor = self.conn.cursor()
            query = "select * from users natural inner join useraddress where uid = %s;"
            cursor.execute(query, (uid,))
            result = cursor.fetchone()
            return result

    def getSupplierById(self, uid):
            cursor = self.conn.cursor()
            query = "select * from users natural inner join useraddress where uid = %s AND uType = 'supplier';"
            cursor.execute(query, (uid,))
            result = cursor.fetchone()
            return result

    def getCustomerById(self, uid):
            cursor = self.conn.cursor()
            query = "select * from users natural inner join useraddress where uType = 'customer' AND uid = %s;"
            cursor.execute(query, (uid,))
            result = cursor.fetchone()
            return result

    #hay q implementar
    def getResourcesBySupplierId(self, uid):
            cursor = self.conn.cursor()
            query = "select uid, rid, rname, rprice, descpercent, rcategory,rqty, rregion from resources natural inner join users where uid = %s"
            cursor.execute (query, (uid,))
            result = []
            for row in cursor:
                result.append (row)
            return result

    # hay q implementar
    def getSuppliersByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join useraddress where utype = 'supplier' AND ucity = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByName(self, uname):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where uname = %s;"
        cursor.execute (query, (uname,))
        result = cursor.fetchone ()
        return result

    def getUserByLastname(self, ulast):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where ulast = %s;"
        cursor.execute (query, (ulast,))
        result = cursor.fetchone ()
        return result

    def getUserByType(self,utype):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where utype = %s;"
        cursor.execute (query, (utype,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getUserByCity(self, ucity):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where ucity = %s;"
        cursor.execute (query, (ucity,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getUserByRegion(self, uregion):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where uregion = %s;"
        cursor.execute (query, (uregion,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getUserByZip(self, uzip):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where uzip = %s;"
        cursor.execute (query, (uzip,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getUserByState(self, ustate):
        cursor = self.conn.cursor ()
        query = "select * from users natural inner join useraddress where ustate = %s;"
        cursor.execute (query, (ustate,))
        result = []
        for row in cursor:
            result.append (row)
        return result
