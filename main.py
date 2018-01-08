from flask import Flask, jsonify, request
# from handler.parts import PartHandler
from handler.UserHandler import UserHandler
from handler.ResourcesHandler import ResourcesHandler
from handler.CustomerHandler import CustomerHandler
from handler.RequestHandler import RequestHandler
from handler.PurchaseHandler import PurchaseHandler

app = Flask (__name__)


@app.route ('/')
def greeting():
    return 'Hello, this is the Maria Hurricane Disaster App (MHDA)!'

#All Users
@app.route ('/MHDA/users/')
def getAllUsers():
    return UserHandler ().getAllUsers ()

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

'''
@app.route ('/MHDA/suppliers/<int:sid>/products/')
def getPartsBySuplierId(sid):
    # return SupplierHandler().getPartsBySupplierId(sid)
    return UserHandler ().getDummyData2 (sid)
'''

################

################ Resources
@app.route ('/MHDA/resources/')
def getAllResources():
    return ResourcesHandler ().getAllResources()


@app.route ('/MHDA/resources/<int:rid>')
def getResourceById(rid):
    return ResourcesHandler ().getResourceById(rid)

@app.route ('/MHDA/resources/supplier/<int:uid>')
def getResourcesBySupplierId(uid):
    return UserHandler ().getResourcesBySupplierId(uid)

'''
@app.route ('/MHDA/products/<int:pid>/suppliers/')
def getProductsByPartId(pid):
    # return PartHandler().getSuppliersByPartId(pid)
    return ProductHandler ().getDummyData2 (pid)


@app.route ('/MHDA/products/<int:pid>/category')
def getProductByPartIdCategory(pid):
    # return PartHandler().getSuppliersByPartId(pid)
    return ProductHandler ().getDummyData2 (pid)

'''
################

################Customers

@app.route ('/MHDA/customer/<int:pid>/request')
def getcustomerByPartIdAndRequest(pid):
    # return PartHandler().getSuppliersByPartId(pid)
    return CustomerHandler ().getDummyData2 (pid)


@app.route ('/MHDA/customer/<int:pid>/purchase')
def getcustomerByPartIdAndPurchase(pid):
    # return PartHandler().getSuppliersByPartId(pid)
    return CustomerHandler ().getDummyData2 (pid)


##################

###############Purchase
@app.route ('/MHDA/purchase/')
def getPurchaseByPartId():
    # return PartHandler().getSuppliersByPartId(pid)
    return PurchaseHandler ().getDummyData ()


@app.route ('/MHDA/purchase/<int:puid>')
def getPurchaseById(puid):
    # return PartHandler().getSuppliersByPartId(pid)
    return PurchaseHandler ().getDummyData2 (puid)


@app.route ('/MHDA/purchase/<int:pid>/customer/<int:cid>')
def getPurchaseByProductIdAndCustomerID(pid, cid):
    pid = cid
    return PurchaseHandler ().getDummyData2 (pid)


################

############ Request

@app.route ('/MHDA/request/')
def getAllRequest():
    return RequestHandler ().getAllRequest ()


@app.route ('/MHDA/request/<int:reqid>/')
def getRequestByrId(reqid):
    return RequestHandler ().getRequestById (reqid)


if __name__ == '__main__':
    app.run ()
