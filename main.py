from flask import Flask, jsonify, request
from handler.parts import PartHandler
from handler.supplier import SupplierHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/PartApp/parts')
def getAllParts():
    if not request.args:
        #return PartHandler().getAllParts()
        return SupplierHandler ().getAllSuppliers ()
    else:
        #return PartHandler().searchParts(request.args)
        return SupplierHandler ().getAllSuppliers ()

@app.route('/PartApp/parts/<int:pid>')
def getPartById(pid):
    #return PartHandler().getPartById(pid)
    return SupplierHandler ().getAllSuppliers ()

@app.route('/PartApp/parts/<int:pid>/suppliers')
def getSuppliersByPartId(pid):
    #return PartHandler().getSuppliersByPartId(pid)
    return SupplierHandler ().getAllSuppliers ()

@app.route('/PartApp/suppliers')
def getAllSuppliers():
    if not request.args:
        #return SupplierHandler().getAllSuppliers()
        return SupplierHandler ().getAllSuppliers ()
    else:
        #return SupplierHandler().searchSuppliers(request.args)
        return SupplierHandler ().getAllSuppliers ()

@app.route('/PartApp/suppliers/<int:sid>')
def getSupplierById(sid):
    #return SupplierHandler().getSupplierById(sid)
    return SupplierHandler ().getAllSuppliers ()

@app.route('/PartApp/suppliers/<int:sid>/parts')
def getPartsBySuplierId(sid):
    #return SupplierHandler().getPartsBySupplierId(sid)
    return SupplierHandler ().getAllSuppliers ()

if __name__ == '__main__':
    app.run()