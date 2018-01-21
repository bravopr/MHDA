from config.dbconfig import pg_config
import psycopg2
from handler.PaymentInfoHandler import PaymentInfoHandler
import os
from urllib import parse

class UserDAO:
    def __init__(self):
        '''
        parse.uses_netloc.append ("postgres")
        url = parse.urlparse (os.environ["DATABASE_URL"])

        self.conn = psycopg2.connect (
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
        '''
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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

    def getMaxID(self):
        cursor = self.conn.cursor()
        query = "select max(uid) from users;"
        cursor.execute (query)
        maxid = cursor.fetchone ()
        if (maxid is 0) or (maxid is None):
            return 1;

        return maxid[0]

    def delete(self, uid):
        cursor = self.conn.cursor ()
        # From Table UsersAddress
        query = "delete from useraddress where uid = %s;"
        cursor.execute (query, (uid,))
        # From Table Users
        query2 = "delete from users where uid = %s;"
        cursor.execute (query2, (uid,))
        #Delete payment info of user
        #PaymentInfoHandler ().deletePaymentInfo (uid)
        return uid

    def insert(self, uname, ulast, utype, uaddress, ucity, uregion, uzip, ustate, loclat, loclon):
        cursor = self.conn.cursor ()
        #Insert into Table Users
        maxID = UserDAO.getMaxID (self)
        uid = maxID + 1
        query = "insert into users(uid, uname, ulast, utype) values (%s, %s, %s, %s) ;"
        cursor.execute (query, (uid, uname, ulast, utype,))

        # Insert into Table UsersAddress
        queryUA = "insert into useraddress(uid, uaddress, ucity, uregion, uzip, ustate, loclat, loclon)"
        queryUAp2 = "values (%s, %s, %s, %s, %s, %s, %s, %s) ;"
        querytotalUA = queryUA + queryUAp2
        cursor.execute (querytotalUA, (uid, uaddress, ucity, uregion, uzip, ustate, loclat, loclon,))
        self.conn.commit ()
        return uid

    def update(self, uid, uname, ulast, utype, uaddress, ucity, uregion, uzip, ustate, loclat, loclon):
        cursor = self.conn.cursor ()
        # Insert into Table Users
        query = "update users set uname = %s, ulast = %s, utype = %s where uid = %s ;"
        cursor.execute (query, ( uname, ulast, utype, uid,))

        # Insert into Table UsersAddress
        query2 = "update useraddress set uaddress = %s, ucity = %s, uregion = %s, uzip = %s, ustate = %s, loclat = %s, loclon = %s where uid = %s"
        cursor.execute (query2, ( uaddress, ucity, uregion, uzip, ustate, loclat, loclon, uid,))
        self.conn.commit ()
        return uid
