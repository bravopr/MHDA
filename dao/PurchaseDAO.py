from config.dbconfig import pg_config
import psycopg2
import os
from urllib import parse

class PurchaseDAO:
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

    def getAllPurchase(self):
        cursor = self.conn.cursor ()
        query = "select * from purchase;"
        cursor.execute (query)
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getPurchaseBypurId(self, purid):
        cursor = self.conn.cursor ()
        query = "select * from purchase where purid = %s;"
        cursor.execute (query, (purid,))
        result = cursor.fetchone ()
        return result

    def getPurchaseByResourcesId(self, rid):
        cursor = self.conn.cursor ()
        query = "select * from purchase where rid = %s;"
        cursor.execute (query, (rid,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getPurchaseByReqID(self, reqid):
        cursor = self.conn.cursor ()
        query = "select * from purchase where reqid = %s;"
        cursor.execute (query, (reqid,))
        result = cursor.fetchone ()
        return result

    def getPurchaseByUser(self, uid):
        cursor = self.conn.cursor ()
        query = "select * from purchase where uid = %s;"
        cursor.execute (query, (uid,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getPurchaseByPrice(self, purprice):
        cursor = self.conn.cursor ()
        query = "select * from purchase where purprice = %s;"
        cursor.execute (query, (purprice,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getPurchaseByCarrier(self, carrier):
        cursor = self.conn.cursor ()
        query = "select * from purchase where carrier = %s;"
        cursor.execute (query, (carrier,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getPurchaseByStatus(self, purstatus):
        cursor = self.conn.cursor ()
        query = "select * from purchase where purstatus = %s;"
        cursor.execute (query, (purstatus,))
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getMaxID(self):
        cursor = self.conn.cursor()
        query = "select max(purid) from purchase;"
        cursor.execute (query)
        maxid = cursor.fetchone ()
        if (maxid is 0) or (maxid is None):
            return 1;

        return maxid[0]

    def insert(self, rid, reqid, uid, purdate, purprice, purqty, expdeliverydate, carrier, purstatus):
        cursor = self.conn.cursor ()
        maxID = PurchaseDAO.getMaxID (self)
        purid = maxID + 1
        query = "insert into purchase(purid, rid, reqid, uid, purdate, purprice, purqty, expdeliverydate, carrier, purstatus)"
        queryp2 = "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ;"
        querytotal = query + queryp2
        cursor.execute (querytotal, (purid, rid, reqid, uid, purdate, purprice, purqty, expdeliverydate, carrier, purstatus,))
        self.conn.commit ()
        return purid

    def update(self, purid, rid, reqid, uid, purdate, purprice, purqty, expdeliverydate, carrier, purstatus):
        cursor = self.conn.cursor ()
        query = "update purchase set rid = %s, reqid = %s, uid = %s, purdate = %s, purprice = %s, purqty = %s, expdeliverydate = %s, carrier = %s, purstatus = %s"
        filter = "where purid = %s;"
        querytotal = query+ filter
        cursor.execute (querytotal,(rid, reqid, uid, purdate, purprice, purqty, expdeliverydate, carrier, purstatus,purid,))
        self.conn.commit ()
        return purid

    def delete(self, purid):
        cursor = self.conn.cursor ()
        query = "delete from purchase where purid = %s;"
        cursor.execute (query, (purid,))
        self.conn.commit ()
        return purid
