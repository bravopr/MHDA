from config.dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):

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

    '''
    def getPartsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select pid, pname, pmaterial, pcolor, pprice, qty from parts natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    
    def getSuppliersByCity(self, city):
        cursor = self.conn.cursor()
        query = "select * from supplier where scity = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    '''