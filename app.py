from flask import Flask, jsonify, request
from handler.UserHandler import UserHandler
from handler.ResourcesHandler import ResourcesHandler
from handler.RequestHandler import RequestHandler
from handler.PurchaseHandler import PurchaseHandler
from handler.PaymentInfoHandler import PaymentInfoHandler

app = Flask (__name__)
#app.run(debug=True)
@app.route ('/')
def greeting():
    with open ("welcome.txt", "r") as f:
        content = f.read ()
    return content

@app.route ('/MHDA/')
def greeting2():
    with open ("welcome.txt", "r") as f:
        content = f.read ()
    return content

#All Users
@app.route ('/MHDA/users/', methods=['GET', 'POST','PUT','DELETE'])
def getUsers():
    if request.method == 'POST':
        userDic = {}
        userDic['uname'] = request.args.get ('uname')
        userDic['ulast'] = request.args.get ('ulast')
        userDic['utype'] = request.args.get ('utype')
        userAddressDic = {}
        userAddressDic['uaddress'] = request.args.get ('uaddress')
        userAddressDic['ucity'] = request.args.get ('ucity')
        userAddressDic['uregion'] = request.args.get ('uregion')
        userAddressDic['uzip'] = request.args.get ('uzip')
        userAddressDic['ustate'] = request.args.get ('ustate')
        userAddressDic['loclat'] = request.args.get ('loclat')
        userAddressDic['loclon'] = request.args.get ('loclon')
        return UserHandler().insertUser(userDic,userAddressDic)

    elif request.method == 'PUT':
        userDic = {}
        userDic['uid'] = request.args.get ('uid')
        userDic['uname'] = request.args.get ('uname')
        userDic['ulast'] = request.args.get ('ulast')
        userDic['utype'] = request.args.get ('utype')
        userAddressDic = {}
        userAddressDic['uaddress'] = request.args.get ('uaddress')
        userAddressDic['ucity'] = request.args.get ('ucity')
        userAddressDic['uregion'] = request.args.get ('uregion')
        userAddressDic['uzip'] = request.args.get ('uzip')
        userAddressDic['ustate'] = request.args.get ('ustate')
        userAddressDic['loclat'] = request.args.get ('loclat')
        userAddressDic['loclon'] = request.args.get ('loclon')
        return UserHandler().updateUser(userDic,userAddressDic)

    elif request.method == 'DELETE':
        uid = request.args.get ('uid')
        return UserHandler ().deleteUser (uid)

    else:
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUsers(request.args)

@app.route ('/MHDA/users/<int:uid>')
def getUserById(uid):
    return UserHandler ().getUserById (uid)

################Customers
@app.route ('/MHDA/customers/')
def getAllCustomers():
    return UserHandler ().getAllCustomers ()

@app.route ('/MHDA/customers/<int:uid>')
def getCustomerById(uid):
    return UserHandler ().getCustomerById (uid)

################

################Suppliers
@app.route ('/MHDA/suppliers/')
def getAllSuppliers():
    return UserHandler ().getAllSuppliers ()


@app.route ('/MHDA/suppliers/<int:uid>')
def getSupplierById(uid):
    return UserHandler ().getSupplierById (uid)


################

################ Resources

@app.route('/MHDA/resources/', methods=['GET', 'POST','PUT','DELETE'])
def getResources():
    if request.method == 'POST':
        result = {}
        result['uid'] = request.args.get('uid')
        result['rname'] = request.args.get ('rname')
        result['rprice'] = request.args.get ('rprice')
        result['descpercent'] = request.args.get ('descpercent')
        result['rcategory'] = request.args.get ('rcategory')
        result['rqty'] = request.args.get ('rqty')
        result['rregion'] = request.args.get ('rregion')
        return ResourcesHandler().insertResource(result)

    elif request.method == 'PUT':
        result = {}
        rid = request.args.get ('rid')
        result['rid'] = rid
        result['uid'] = request.args.get ('uid')
        result['rname'] = request.args.get ('rname')
        result['rprice'] = request.args.get ('rprice')
        result['descpercent'] = request.args.get ('descpercent')
        result['rcategory'] = request.args.get ('rcategory')
        result['rqty'] = request.args.get ('rqty')
        result['rregion'] = request.args.get ('rregion')
        return ResourcesHandler ().updateResource (rid, result)

    elif request.method == 'DELETE':
        rid = request.args.get ('rid')
        return ResourcesHandler ().deleteResource (rid)
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)

@app.route ('/MHDA/resources/available/')
def getAllResources():
        return ResourcesHandler ().getAllResourcesAvailable ()

'''
@app.route ('/MHDA/resources/maxid')
def getMaxID():
    return ResourcesHandler ().getMaxID()
'''

@app.route ('/MHDA/resources/<int:rid>', methods=['GET'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourcesHandler ().getResourceById (rid)
    else:
        return jsonify (Error="Method not allowed."), 405

@app.route ('/MHDA/resources/supplier/<int:uid>')
def getResourcesBySupplierId(uid):
    return UserHandler ().getResourcesBySupplierId(uid)

@app.route ('/MHDA/resources/<int:rid>/supplier')
def getSupplierByResourcesId(rid):
    return ResourcesHandler ().getSupplierByResourcesId(rid)

################

###############Purchase
@app.route ('/MHDA/purchase/', methods=['GET', 'POST','PUT','DELETE'])
def getPurchase():
    if request.method == 'POST':
        result = {}
        result['rid'] = request.args.get('rid')
        result['reqid'] = request.args.get ('reqid')
        result['uid'] = request.args.get ('uid')
        result['purdate'] = request.args.get ('purdate')
        result['purprice'] = request.args.get ('purprice')
        result['purqty'] = request.args.get ('purqty')
        result['expdeliverydate'] = request.args.get ('expdeliverydate')
        result['carrier'] = request.args.get ('carrier')
        result['purstatus'] = request.args.get ('purstatus')
        return PurchaseHandler().insertPurchase(result)

    elif request.method == 'PUT':
        result = {}
        result['purid'] = request.args.get ('purid')
        result['rid'] = request.args.get ('rid')
        result['reqid'] = request.args.get ('reqid')
        result['uid'] = request.args.get ('uid')
        result['purdate'] = request.args.get ('purdate')
        result['purprice'] = request.args.get ('purprice')
        result['purqty'] = request.args.get ('purqty')
        result['expdeliverydate'] = request.args.get ('expdeliverydate')
        result['carrier'] = request.args.get ('carrier')
        result['purstatus'] = request.args.get ('purstatus')
        return PurchaseHandler ().updatePurchase (result['purid'], result)

    elif request.method == 'DELETE':
        purid = request.args.get ('purid')
        return PurchaseHandler ().deletePurchase (purid)

    else:
        if not request.args:
            return PurchaseHandler().getAllPurchase()
        else:
            return PurchaseHandler().searchPurchase(request.args)

'''
@app.route ('/MHDA/purchase/<int:puid>')
def getPurchaseById(puid):
    # return PartHandler().getSuppliersByPartId(pid)
    return PurchaseHandler ().getDummyData2 (puid)


@app.route ('/MHDA/purchase/<int:pid>/customer/<int:cid>')
def getPurchaseByProductIdAndCustomerID(pid, cid):
    pid = cid
    return PurchaseHandler ().getDummyData2 (pid)
'''

################

############ PaymentInfo

@app.route ('/MHDA/paymentinfo/', methods=['POST','PUT','DELETE','GET'])
def getPaymentInfo():
    if request.method == 'POST':
        result = {}
        result['uid'] = request.args.get ('uid')
        result['ccnumber'] = request.args.get ('ccnumber')
        result['ccv'] = request.args.get ('ccv')
        result['validdate'] = request.args.get ('validdate')
        result['expdate'] = request.args.get ('expdate')
        return PaymentInfoHandler().insertPayment(result)

    elif request.method == 'PUT':
        result = {}
        result['uid'] = request.args.get ('uid')
        result['ccnumber'] = request.args.get ('ccnumber')
        result['ccv'] = request.args.get ('ccv')
        result['validdate'] = request.args.get ('validdate')
        result['expdate'] = request.args.get ('expdate')
        return PaymentInfoHandler ().updatePaymentInfo (result['uid'], result)

    elif request.method == 'DELETE':
        uid = request.args.get ('uid')
        return PaymentInfoHandler ().deletePaymentInfo (uid)

    else:
        if not request.args:
            return PaymentInfoHandler().getAllPaymentInfo()
        else:
          #  return "here"
            return PaymentInfoHandler().searchPayment(request.args)

############ Request

@app.route ('/MHDA/request/', methods=['GET', 'POST','PUT','DELETE'])
def getRequest():
    if request.method == 'POST':
        result = {}
        #result['reqid'] = request.args.get ('reqid')
        result['rid'] = request.args.get ('rid')
        result['uid'] = request.args.get ('uid')
        result['rqty'] = request.args.get ('rqty')
        result['reqtype'] = request.args.get ('reqtype')
        result['reqdate'] = request.args.get ('reqdate')
        result['expdeliverydate'] = request.args.get ('expdeliverydate')
        result['carrier'] = request.args.get ('carrier')
        result['reqstatus'] = request.args.get ('reqstatus')
        return RequestHandler().insertRequest(result)
    elif request.method == 'PUT':
        result = {}
        result['reqid'] = request.args.get ('reqid')
        result['rid'] = request.args.get ('rid')
        result['uid'] = request.args.get ('uid')
        result['rqty'] = request.args.get ('rqty')
        result['reqtype'] = request.args.get ('reqtype')
        result['reqdate'] = request.args.get ('reqdate')
        result['expdeliverydate'] = request.args.get ('expdeliverydate')
        result['carrier'] = request.args.get ('carrier')
        result['reqstatus'] = request.args.get ('reqstatus')
        return RequestHandler ().updateRequest (result['reqid'],result)
    elif request.method == 'DELETE':
        reqid = request.args.get ('reqid')
        return RequestHandler ().deleteRequest (reqid)
    else:
        if not request.args:
            return RequestHandler().getAllRequestSortingByName()
        else:
            return RequestHandler().searchRequest(request.args)


@app.route ('/MHDA/request/<int:reqid>/')
def getRequestByrId(reqid):
    return RequestHandler ().getRequestById (reqid)


if __name__ == '__main__':
    app.run ()
