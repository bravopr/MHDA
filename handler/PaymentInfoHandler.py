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
        request_list = dao.getAllPaymentInfo ()
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPaymentInfoByUserId(self, uid):
        dao = PaymentInfoDAO ()
        request_list = dao.getPaymentInfoByUserId (uid)
        result_list = []
        for row in request_list:
            result = self.build_pur_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPaymentInfoByCCNumber(self, ccnumber):
        dao = PaymentInfoDAO ()
        row = dao.getPaymentInfoByCCNumber (ccnumber)
        if not row:
            return jsonify (Error="Request Not Found"), 404
        else:
            result = self.build_pur_dict (row)
        return jsonify (result)

    def searchPayment(self, args):
        uid_filter = args.get ("uid")
        ccnumber_filter = args.get ("ccnumber")
        #ccv_filter = args.get ("ccv")
        #validdate_filter = args.get ("validdate")
        #expdate_filter = args.get ("expdate")

        if (len (args) == 1) and uid_filter:
            return (PaymentInfoHandler ().getPaymentInfoByUserId (uid_filter))
        elif (len (args) == 1) and ccnumber_filter:
            return (PaymentInfoHandler ().getPaymentInfoByCCNumber (ccnumber_filter))
        #elif (len (args) == 1) and ccv_filter:
        #    return (PaymentInfoHandler ().getPaymentInfoByCCV (ccv_filter))
        #elif (len (args) == 1) and validdate_filter:
        #    return (PaymentInfoHandler ().getPaymentInfoByValidDate (validdate_filter))
        #elif (len (args) == 1) and expdate_filter:
        #   return (PaymentInfoHandler ().getPaymentInfoByExpDate (expdate_filter))
        else:
            return jsonify (Error="Malformed query string"), 400

    def insertPayment(self, form):
        pass


