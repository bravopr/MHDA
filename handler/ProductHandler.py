from flask import jsonify
from dao.supplier import SupplierDAO


class ProductHandler:
    def getDummyData(self):

        data = {"sid": 1, "sname": "Osmi", "scity": "Guaynabo", "sphone": "7875555555"}
        return jsonify(data)

    def getDummyData2(self, rid):

        data = {"sid": 1, "sname": "Osmi", "scity": "Guaynabo", "sphone": "7875555555"}
        return jsonify(data)