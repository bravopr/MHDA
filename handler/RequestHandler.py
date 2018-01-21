from flask import jsonify
from dao.RequestDAO import RequestDAO


class RequestHandler:

    def build_req_dict(self, row):
        result = {}
        result['reqid'] = row[0]
        result['rid'] = row[1]
        result['uid'] = row[2]
        result['reqtype'] = row[3]
        result['reqdate'] = row[4]
        result['expdeliverydate'] = row[5]
        result['carrier'] = row[6]
        result['reqstatus'] = row[7]
        result['rqty'] = row[8]
        return result

    def build_req_dict2(self, reqid,rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus):
        result = {}
        result['reqid'] = reqid
        result['rid'] = rid
        result['uid'] = uid
        result['rqty'] = rqty
        result['reqtype'] = reqtype
        result['reqdate'] = reqdate
        result['expdeliverydate'] = expdeliverydate
        result['carrier'] = carrier
        result['reqstatus'] = reqstatus
        return result

    def build_allreq_dict(self, row):
        result = {}
        result['reqid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['uid'] = row[3]
        result['reqtype'] = row[4]
        result['reqdate'] = row[5]
        result['expdeliverydate'] = row[6]
        result['carrier'] = row[7]
        result['reqstatus'] = row[8]
        result['rqty'] = row[9]
        return result

    def getAllRequestSortingByName(self):
        dao = RequestDAO()
        request_list = dao.getAllRequestSortingByName()
        result_list = []
        for row in request_list:
            result = self.build_allreq_dict(row)
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

    def getRequestByResourcesId(self, rid):
        dao = RequestDAO ()
        request_list = dao.getRequestByResourcesId (rid)
        result_list = []
        for row in request_list:
            result = self.build_req_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getRequestByUser(self, uid):
        dao = RequestDAO ()
        request_list = dao.getRequestByUser (uid)
        result_list = []
        for row in request_list:
            result = self.build_req_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getRequestByType(self, reqtype):
        dao = RequestDAO ()
        request_list = dao.getRequestByType (reqtype)
        result_list = []
        for row in request_list:
            result = self.build_req_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getRequestByCarrier(self, carrier):
        dao = RequestDAO ()
        request_list = dao.getRequestByCarrier (carrier)
        result_list = []
        for row in request_list:
            result = self.build_req_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getRequestByStatus(self, reqstatus):
        dao = RequestDAO ()
        request_list = dao.getRequestByStatus (reqstatus)
        result_list = []
        for row in request_list:
            result = self.build_req_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getRequestSortingByName(self, rname):
        dao = RequestDAO ()
        request_list = dao.getRequestSortingByName (rname)
        result_list = []
        for row in request_list:
            result = self.build_allreq_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def searchRequest(self, args):
        reqid_filter = args.get("reqid")
        rid_filter = args.get("rid")
        uid_filter = args.get("uid")
        rname_filter = args.get ("rname")
        reqtype_filter = args.get ("reqtype")
        reqdate_filter = args.get ("reqdate")
        expdeliverydate_filter = args.get("expdeliverydate")
        carrier_filter = args.get ("carrier")
        reqstatus_filter = args.get ("reqstatus")
        #rqty_filter = args.get ("rqty")
        if (len(args) == 1) and reqid_filter:
            return (RequestHandler().getRequestById(reqid_filter))
        elif (len(args) == 1) and rid_filter:
            return (RequestHandler ().getRequestByResourcesId (rid_filter))
        elif (len(args) == 1) and uid_filter:
            return (RequestHandler ().getRequestByUser (uid_filter))
        elif (len(args) == 1) and rname_filter:
            return (RequestHandler ().getRequestSortingByName (rname_filter))
        elif (len (args) == 1) and reqtype_filter:
            return (RequestHandler ().getRequestByType (reqtype_filter))
        #elif (len(args) == 1) and reqdate_filter:
        #    return (RequestHandler ().getRequestByReqDate (reqdate_filter))
        #elif (len(args) == 1) and expdeliverydate_filter:
        #    return (RequestHandler ().getRequestByExpDevDate (expdeliverydate_filter))
        elif (len(args) == 1) and carrier_filter:
            return (RequestHandler ().getRequestByCarrier (carrier_filter))
        elif (len(args) == 1) and reqstatus_filter:
            return (RequestHandler ().getRequestByStatus (reqstatus_filter))
        #elif (len(args) == 1) and rqty_filter :
        #    return (RequestHandler ().getRequestByQty (rqty_filter))
        else:
            return jsonify(Error = "Malformed query string"), 400

    def insertRequest(self, form):
        dao = RequestDAO ()
        if len (form) != 8:
            return jsonify (Error="Malformed post request"), 400
        else:
            rid = form['rid']
            uid = form['uid']
            rqty = form['rqty']
            reqtype = form['reqtype']
            reqdate = form['reqdate']
            expdeliverydate = form['expdeliverydate']
            carrier = form['carrier']
            reqstatus = form['reqstatus']

            if rid and uid and rqty and reqtype and reqdate and expdeliverydate and carrier and reqstatus:
                reqid = dao.insert (rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus)
                result = self.build_req_dict2 (reqid,rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus)
                return jsonify (Request=result), 201
            else:
                return jsonify (Error="Unexpected attributes in post request"), 400

    def updateRequest(self, reqid,form):
        dao = RequestDAO ()
        if not dao.getRequestById(reqid):
            return jsonify (Error="Request not found."), 404
        if len (form) != 9:
            return jsonify (Error="Malformed post request"), 400
        else:
            reqid = form['reqid']
            rid = form['rid']
            uid = form['uid']
            rqty = form['rqty']
            reqtype = form['reqtype']
            reqdate = form['reqdate']
            expdeliverydate = form['expdeliverydate']
            carrier = form['carrier']
            reqstatus = form['reqstatus']

            if reqid and rid and uid and rqty and reqtype and reqdate and expdeliverydate and carrier and reqstatus:
                dao.update (reqid,rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus)
                result = self.build_req_dict2 (reqid,rid, uid, rqty, reqtype, reqdate, expdeliverydate, carrier, reqstatus)
                return jsonify (Request=result), 201
            else:
                return jsonify (Error="Unexpected attributes in put request"), 400

    def deleteRequest(self, reqid):
        dao = RequestDAO ()
        if not dao.getRequestById (reqid):
            return jsonify (Error="Cannot delete, purchase info not found."), 404
        else:
            dao.delete (reqid)
            return jsonify (DeleteStatus="OK"), 200












