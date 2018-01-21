from config.dbconfig import pg_config
import psycopg2
import os
from urllib import parse

class RequestDAO:
    def __init__(self):

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
        '''
    def getAllRequestSortingByName(self):
        cursor = self.conn.cursor ()
        query = "select req.reqid ,req.rid ,r.rname,req.uid,req.reqtype,req.reqdate,req.expdeliverydate,req.carrier,req.reqstatus,req.rqty from resources r, request as req WHERE r.rid=req.rid order by rname;"
        cursor.execute (query)
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getRequestSortingByName(self,rname):
        cursor = self.conn.cursor ()
        query = "select req.reqid ,req.rid ,r.rname,req.uid,req.reqtype,req.reqdate,req.expdeliverydate,req.carrier,req.reqstatus,req.rqty from resources r, request as req WHERE r.rid=req.rid AND rname = %s order by rname;"
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

    def getMaxID(self):
        cursor = self.conn.cursor()
        query = "select max(reqid) from request;"
        cursor.execute (query)
        maxid = cursor.fetchone ()
        if (maxid is 0) or (maxid is None):
            return 1;

        return maxid[0]

    def insert(self, rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus):
        cursor = self.conn.cursor ()
        maxID = RequestDAO.getMaxID (self)
        reqid = maxID + 1
        query = "insert into request(reqid, rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus)"
        queryp2 = "values (%s, %s, %s, %s, %s, %s, %s, %s, %s) ;"
        querytotal = query + queryp2
        cursor.execute (querytotal,(reqid, rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus,))
        self.conn.commit ()
        return reqid

    def update(self, reqid, rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus):
        cursor = self.conn.cursor ()
        query = "update request set rid = %s, uid = %s, rqty = %s, reqtype = %s, reqdate = %s, expdeliverydate = %s, carrier = %s, reqstatus = %s"
        filter = "where reqid = %s;"
        querytotal = query + filter
        cursor.execute (querytotal,
                        ( rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus,reqid,))
        self.conn.commit ()
        return reqid

    def delete(self, reqid):
        cursor = self.conn.cursor ()
        query = "delete from request where reqid = %s;"
        cursor.execute (query, (reqid,))
        self.conn.commit ()
        return reqid
