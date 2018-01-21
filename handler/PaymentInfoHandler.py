from flask import jsonify
from dao.PaymentInfoDAO import PaymentInfoDAO

class PaymentInfoHandler:
    def build_paymentinfo_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ccnumber'] = row[1]
        result['ccv'] = row[2]
        result['validdate'] = row[3]
        result['expdate'] = row[4]
        return result

    def build_paymentinfo_dict2(self,uid,ccnumber,ccv,validate,expdate):
        result = {}
        result['uid'] = uid
        result['ccnumber'] = ccnumber
        result['ccv'] = ccv
        result['validdate'] = validate
        result['expdate'] = expdate
        return result

    def getAllPaymentInfo(self):
        dao = PaymentInfoDAO ()
        request_list = dao.getAllPaymentInfo ()
        result_list = []
        for row in request_list:
            result = self.build_paymentinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getPaymentInfoByUserId(self, uid):
        dao = PaymentInfoDAO ()
        row = dao.getPaymentInfoByUserID (uid)
        if not row:
            return jsonify (Error="Request Not Found userID"), 404
        else:
            result = self.build_paymentinfo_dict (row)
        return jsonify (result)

    def getPaymentInfoByCCNumber(self, ccnumber):
        dao = PaymentInfoDAO ()
        row = dao.getPaymentInfoByCCNumber (ccnumber)
        if not row:
            return jsonify (Error="Request Not Found CCNumber"), 404
        else:
            result = self.build_paymentinfo_dict (row)
        return jsonify (result)

    def searchPayment(self, args):
        uid_filter = args.get ("uid")
        ccnumber_filter = args.get ("ccnumber")
        ccv_filter = args.get ("ccv")
        validdate_filter = args.get ("validdate")
        expdate_filter = args.get ("expdate")

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
            return jsonify (Error="Malformed query string searchPayment"), 400

    def insertPayment(self, form):
        dao = PaymentInfoDAO ()
        if len (form) != 5:
            return jsonify (Error="Malformed insertPaymentInfo post request"), 400
        else:
            uid = form['uid']
            ccnumber = form['ccnumber']
            ccv = form['ccv']
            validdate = form['validdate']
            expdate = form['expdate']

            if uid and ccnumber and ccv and validdate and expdate:
                dao.insert (uid,ccnumber,ccv,validdate,expdate)
                result = self.build_paymentinfo_dict2 (uid,ccnumber,ccv,validdate,expdate)
                return jsonify (User=result), 201
            else:
                return jsonify (Error="Unexpected attributes in post request"), 400

    def updatePaymentInfo(self, uid1, form):
        dao = PaymentInfoDAO ()
        if not dao.getPaymentInfoByUserID (uid1):
            return jsonify (Error="Malformed update request"), 400
        else:
            uid = form['uid']
            ccnumber = form['ccnumber']
            ccv = form['ccv']
            validdate = form['validdate']
            expdate = form['expdate']

            if uid and ccnumber and ccv and validdate and expdate:
                dao.update (uid, ccnumber, ccv, validdate, expdate)
                result = self.build_paymentinfo_dict2 (uid, ccnumber, ccv, validdate, expdate)
                return jsonify (User=result), 201
            else:
                return jsonify (Error="Unexpected attributes in put request updatePaymentInfo"), 400

    def deletePaymentInfo(self, uid):
        dao = PaymentInfoDAO ()
        if not dao.getPaymentInfoByUserID (uid):
            return jsonify (Error="User PaymentInfo not found."), 404
        else:
            dao.delete (uid)
            return jsonify (DeleteStatus="OK"), 200


