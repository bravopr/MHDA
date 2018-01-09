from flask import jsonify
from dao.PaymentInfoDAO import PaymentInfoDAO


class PaymentInfoHandler:
    def build_pur_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ccnumber'] = row[1]
        result['ccv'] = row[2]
        result['validdate'] = row[3]
        result['expdate'] = row[4]
        return result

    def getAllPaymentInfo(self):
        dao = PaymentInfoDAO ()
        request_list = dao.getAllPurchase ()
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPaymentInfoByUserId(self, uid):
        dao = PaymentInfoDAO ()
        request_list = dao.getPurchaseById (uid)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)