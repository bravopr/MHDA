from config.dbconfig import pg_config
import psycopg2
import os
from urllib import parse

class PaymentInfoDAO:
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
    def getAllPaymentInfo(self):
        cursor = self.conn.cursor ()
        query = "select * from paymentinfo;"
        cursor.execute (query)
        result = []
        for row in cursor:
            result.append (row)
        return result

    def getPaymentInfoByUserID(self, uid):
        cursor = self.conn.cursor ()
        query = "select * from paymentinfo where uid = %s;"
        cursor.execute (query, (uid,))
        result = cursor.fetchone ()
        return result

    def getPaymentInfoByCCNumber(self, ccnumber):
        cursor = self.conn.cursor ()
        query = "select * from paymentinfo where ccnumber = %s;"
        cursor.execute (query, (ccnumber,))
        result = cursor.fetchone ()
        return result

    def insert(self, uid, ccnumber, ccv, validdate, expdate):
        cursor = self.conn.cursor ()
        query = "insert into paymentinfo(uid,ccnumber,ccv,validdate,expdate) values (%s, %s, %s, %s, %s);"
        cursor.execute (query,(uid, ccnumber, ccv, validdate, expdate,))
        self.conn.commit ()
        return uid

    def update(self, uid, ccnumber, ccv, validdate, expdate):
        cursor = self.conn.cursor ()
        query = "update paymentinfo set ccnumber = %s,ccv = %s,validdate = %s,expdate = %s where uid = %s;"
        cursor.execute (query, (ccnumber, ccv, validdate, expdate,uid,))
        self.conn.commit ()
        return uid

    def delete(self, uid):
        cursor = self.conn.cursor ()
        query = "delete from paymentinfo where uid = %s;"
        cursor.execute (query, (uid,))
        self.conn.commit ()
        return uid