from flask import Flask, jsonify, request
from handler.UserHandler import UserHandler
from handler.ResourcesHandler import ResourcesHandler
from handler.RequestHandler import RequestHandler
from handler.PurchaseHandler import PurchaseHandler
from handler.PaymentInfoHandler import PaymentInfoHandler

app = Flask (__name__)

@app.route ('/')
def greeting():
    return 'Hello, this is the Maria Hurricane Disaster App (MHDA)!'

#All Users
@app.route ('/MHDA/users/')
def getUsers():
    if request.method == 'POST':
        return UserHandler().insertResource(request.form)
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

@app.route('/MHDA/resources/', methods=['GET', 'POST'])
def getResources():
    if request.method == 'POST':
        return ResourcesHandler().insertResource(request.form)
    else:
        if not request.args:
            return ResourcesHandler().getAllResources()
        else:
            return ResourcesHandler().searchResources(request.args)

@app.route ('/MHDA/resources/available/')
def getAllResources():
        return ResourcesHandler ().getAllResourcesAvailable ()

'''       
@app.route ('/MHDA/resources/')
def getAllResources():
    return ResourcesHandler ().getAllResources()
'''

@app.route ('/MHDA/resources/<int:rid>')
def getResourceById(rid):
    return ResourcesHandler ().getResourceById(rid)

@app.route ('/MHDA/resources/supplier/<int:uid>')
def getResourcesBySupplierId(uid):
    return UserHandler ().getResourcesBySupplierId(uid)

@app.route ('/MHDA/resources/<int:rid>/supplier')
def getSupplierByResourcesId(rid):
    return ResourcesHandler ().getSupplierByResourcesId(rid)

################

###############Purchase
@app.route ('/MHDA/purchase/')
def getPurchase():
    if request.method == 'POST':
        return PurchaseHandler().insertPurchase(request.form)
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

@app.route ('/MHDA/paymentinfo/')
def getPaymentInfo():
    if request.method == 'POST':
        return PaymentInfoHandler().insertPayment(request.form)
    else:
        if not request.args:
            return PaymentInfoHandler().getAllPaymentInfo()
        else:
            return PaymentInfoHandler().searchPayment(request.args)

############ Request

@app.route ('/MHDA/request/')
def getRequest():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.form)
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
