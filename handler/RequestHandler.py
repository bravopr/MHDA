from flask import jsonify
from dao.RequestDAO import RequestDAO


class RequestHandler:

    def build_req_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getAllRequest(self):
        dao = RequestDAO()
        request_list = dao.getAllRequest()
        result_list = []
        for row in request_list:
            result = self.build_req_dict(row)
            result_list.append(result)
        return jsonify(result_list)


    def getRequestById(self, uid):
        dao = RequestDAO()
        row = dao.getRequestById(uid)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            result = self.build_req_dict(row)
        return jsonify(result)
