from flask import Flask, jsonify, request
#from handler.parts import PartHandler
from handler.supplier import SupplierHandler
from handler.ProductHandler import ProductHandler
from handler.CustomerHandler import CustomerHandler
from handler.RequestHandler import RequestHandler
from handler.PurchaseHandler import PurchaseHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the Maria Hurricane Disaster App (MHDA)!'

################Suppliers
@app.route('/MHDA/suppliers/')
def getAllSuppliers():
        return SupplierHandler ().getDummyData ()

@app.route('/MHDA/suppliers/<int:sid>')
def getSupplierById(sid):
    #return SupplierHandler().getSupplierById(sid)
    return SupplierHandler ().getDummyData2 (sid)

@app.route('/MHDA/suppliers/<int:sid>/products/')
def getPartsBySuplierId(sid):
    #return SupplierHandler().getPartsBySupplierId(sid)
    return SupplierHandler ().getDummyData2 (sid)
################

################Products
@app.route('/MHDA/products/')
def getAllProducts():
        return ProductHandler ().getDummyData ()

@app.route('/MHDA/products/<int:pid>')
def getProductsById(pid):
    #return PartHandler().getPartById(pid)
    return ProductHandler ().getDummyData2 (pid)

@app.route('/MHDA/products/<int:pid>/suppliers/')
def getProductsByPartId(pid):
    #return PartHandler().getSuppliersByPartId(pid)
    return ProductHandler ().getDummyData2 (pid)

@app.route('/MHDA/products/<int:pid>/category')
def getProductByPartIdCategory(pid):
    #return PartHandler().getSuppliersByPartId(pid)
    return ProductHandler ().getDummyData2 (pid)
################

################Customers
@app.route('/MHDA/customer/')
def getAllCustomer():
    #return PartHandler().getSuppliersByPartId(pid)
    return CustomerHandler ().getDummyData ()

@app.route('/MHDA/customer/<int:cid>/')
def getCustomerByPartId(cid):
    #return PartHandler().getSuppliersByPartId(pid)
    return CustomerHandler ().getDummyData2 (cid)

@app.route('/MHDA/customer/<int:pid>/request')
def getcustomerByPartIdAndRequest(pid):
    #return PartHandler().getSuppliersByPartId(pid)
    return CustomerHandler ().getDummyData2 (pid)

@app.route('/MHDA/customer/<int:pid>/purchase')
def getcustomerByPartIdAndPurchase(pid):
    #return PartHandler().getSuppliersByPartId(pid)
    return CustomerHandler ().getDummyData2 (pid)
##################

###############Purchase
@app.route('/MHDA/purchase/')
def getPurchaseByPartId():
    #return PartHandler().getSuppliersByPartId(pid)
    return PurchaseHandler ().getDummyData ()

@app.route('/MHDA/purchase/<int:puid>')
def getPurchaseById(puid):
    #return PartHandler().getSuppliersByPartId(pid)
    return PurchaseHandler ().getDummyData2 (puid)

@app.route('/MHDA/purchase/<int:pid>/customer/<int:cid>')
def getPurchaseByProductIdAndCustomerID(pid,cid):
    pid=cid
    return PurchaseHandler ().getDummyData2 (pid)
################

############ Request

@app.route('/MHDA/request/')
def getAllRequest():
    #return PartHandler().getSuppliersByPartId(pid)
    return RequestHandler().getDummyData()

@app.route('/MHDA/request/<int:rid>/')
def getRequestByrId(rid):
    return RequestHandler().getDummyData2(rid)

if __name__ == '__main__':
    app.run()