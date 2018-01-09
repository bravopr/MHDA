from config.dbconfig import pg_config
import psycopg2

class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequestSortingByName(self):
        cursor = self.conn.cursor ()
        query = "select req.reqid ,req.rid ,r.rname,req.uid,req.reqtype,req.reqdate,req.expdeliverydate,req.carrier,req.reqstatus,req.rqty from resources r, request as req WHERE r.rid=req.rid order by rname;"
        cursor.execute (query)
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getRequestById(self, reqid):
        cursor = self.conn.cursor ()
        query = "select * from request where reqid = %s;"
        cursor.execute (query, (reqid,))
        result = cursor.fetchone ()
        return result

    def getRequestByResourcesId(self, rid):
        cursor = self.conn.cursor ()
        query = "select * from request where rid = %s;"
        cursor.execute (query, (rid,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getRequestByUser(self, uid):
        cursor = self.conn.cursor ()
        query = "select * from request where uid = %s;"
        cursor.execute (query, (uid,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getRequestByType(self, reqtype):
        cursor = self.conn.cursor ()
        query = "select * from request where reqtype = %s;"
        cursor.execute (query, (reqtype,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getRequestByCarrier(self, carrier):
        cursor = self.conn.cursor ()
        query = "select * from request where carrier = %s;"
        cursor.execute (query, (carrier,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getRequestByStatus(self, reqstatus):
        cursor = self.conn.cursor ()
        query = "select * from request where reqstatus = %s;"
        cursor.execute (query, (reqstatus,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getAllRequestSortingByResourceName(self):
        cursor = self.conn.cursor ()
        query = "select * from request order by rid;"
        cursor.execute (query)
        result = []
        for row in cursor:
            result.append (row)
        return result
