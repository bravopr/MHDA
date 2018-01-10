from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllResourcesAvailable(self):
        cursor = self.conn.cursor()
        query = "select * from resources WHERE rqty > 0 order by rname;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesAvailable(self,rname):
        cursor = self.conn.cursor()
        query = "select * from resources WHERE rqty > 0 AND rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self,rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid = %s;"
        cursor.execute (query, (rid,))
        result = cursor.fetchone ()
        return result

    def getResourceByName(self,rname):
        cursor = self.conn.cursor()
        query = "select * from resources where rname = %s;"
        cursor.execute (query, (rname,))
        result = cursor.fetchone ()
        return result

    def getSupplierByResourcesId(self, rid):
        cursor = self.conn.cursor ()
        query = "select rid,uid,uname,ulast,uaddress,ucity,uregion,uzip,ustate,loclat,loclon from (resources natural inner join users)natural inner join useraddress where rid = %s;"
        cursor.execute (query, (rid,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByCategory(self,rcategory):
        cursor = self.conn.cursor ()
        query = "select * from resources where rcategory = %s;"
        cursor.execute (query, (rcategory,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByRegion(self,rregion):
        cursor = self.conn.cursor ()
        query = "select * from resources where rregion = %s;"
        cursor.execute (query, (rregion,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByQty(self, rqty):
        cursor = self.conn.cursor ()
        query = "select * from resources where rqty = %s;"
        cursor.execute (query, (rqty,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByDesc(self, descpercent):
        cursor = self.conn.cursor ()
        query = "select * from resources where descpercent = %s;"
        cursor.execute (query, (descpercent,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByPrice(self, rprice_filter):
        cursor = self.conn.cursor ()
        query = "select * from resources where rprice = %s;"
        cursor.execute (query, (rprice_filter,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByCategoryAndRegion(self, rcategory, rregion):
        cursor = self.conn.cursor ()
        query = "select * from resources where rcategory = %s and rregion = %s;"
        cursor.execute (query, (rcategory,rregion))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getResourceByNameAndRegion(self, rname, rregion):
        cursor = self.conn.cursor ()
        query = "select * from resources where rname = %s and rregion = %s AND rqty > 0;"
        cursor.execute (query, (rname, rregion))
        result = []
        for row in cursor:
            result.append (row)
        return result
