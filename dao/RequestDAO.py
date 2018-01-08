from config.dbconfig import pg_config
import psycopg2

class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor ()
        query = "select * from request;"
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