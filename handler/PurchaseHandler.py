from flask import jsonify
from dao.PurchaseDAO import PurchaseDAO


class PurchaseHandler:
    def build_pur_dict(self, row):
        result = {}
        result['purid'] = row[0]
        result['rid'] = row[1]
        result['reqid'] = row[2]
        result['uid'] = row[3]
        result['purdate'] = row[4]
        result['purprice'] = row[5]
        result['purqty'] = row[6]
        result['expdeliverydate'] = row[7]
        result['carrier'] = row[8]
        result['purstatus'] = row[9]
        return result

    def getAllPurchase(self):
        dao = PurchaseDAO ()
        request_list = dao.getAllPurchase ()
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPurchaseById(self, purid):
        dao = PurchaseDAO ()
        request_list = dao.getPurchaseById (purid)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPurchaseByResourcesId(self, rid):
        dao = PurchaseDAO ()
        request_list = dao.getPurchaseByResourcesId (rid)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPurchaseByReqID(self, reqid):
        dao = PurchaseDAO ()
        row = dao.getPurchaseByReqID (reqid)
        if not row:
            return jsonify (Error="Request Not Found"), 404
        else:
            result = self.build_pur_dict (row)
        return jsonify (result)

    def getPurchaseByUser(self, uid):
        dao = PurchaseDAO ()
        request_list = dao.getPurchaseByUser (uid)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPurchaseByPrice(self, purprice):
        dao = PurchaseDAO ()
        request_list = dao.getPurchaseByPrice (purprice)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPurchaseByCarrier(self, carrier):
        dao = PurchaseDAO ()
        request_list = dao.getPurchaseByCarrier (carrier)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPurchaseByStatus(self, purstatus):
        dao = PurchaseDAO ()
        request_list = dao.getPurchaseByStatus (purstatus)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def searchPurchase(self, args):
        purid_filter = args.get ("purid")
        rid_filter = args.get ("rid")
        reqid_filter = args.get ("reqid")
        uid_filter = args.get ("uid")
        #purdate_filter = args.get ("purdate")
        purprice_filter = args.get ("purprice")
        purqty_filter = args.get ("purqty")
        #expdeliverydate_filter = args.get ("expdeliverydate")
        carrier_filter = args.get ("carrier")
        purstatus_filter = args.get ("purstatus")
        if (len (args) == 1) and purid_filter:
            return (PurchaseHandler ().getPurchaseById (purid_filter))
        elif (len (args) == 1) and rid_filter:
            return (PurchaseHandler ().getPurchaseByResourcesId (rid_filter))
        elif (len (args) == 1) and reqid_filter:
            return (PurchaseHandler ().getPurchaseByReqID (reqid_filter))
        elif (len (args) == 1) and uid_filter:
            return (PurchaseHandler ().getPurchaseByUser (uid_filter))
        #elif (len (args) == 1) and purdate_filter:
        #    return (PurchaseHandler ().getPurchaseByPurDate (purdate_filter))
        elif (len (args) == 1) and purprice_filter:
            return (PurchaseHandler ().getPurchaseByPrice (purprice_filter))
        #elif (len (args) == 1) and purqty_filter:
        #    return (PurchaseHandler ().getPurchaseByQty (purqty_filter))
        #elif (len (args) == 1) and expdeliverydate_filter:
        #    return (PurchaseHandler ().getPurchaseByExpDevDate (expdeliverydate_filter))
        elif (len (args) == 1) and carrier_filter:
            return (PurchaseHandler ().getPurchaseByCarrier (carrier_filter))
        elif (len (args) == 1) and purstatus_filter:
            return (PurchaseHandler ().getPurchaseByStatus (purstatus_filter))
        else:
            return jsonify (Error="Malformed query string"), 400

    def insertPurchase(self, form):
        pass
















