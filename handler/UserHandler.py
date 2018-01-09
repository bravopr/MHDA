from flask import jsonify
from dao.UserDAO import UserDAO

class UserHandler:

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['ulast'] = row[2]
        result['utype'] = row[3]
        return result

    def build_alluserinfo_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['uname'] = row[1]
        result['ulast'] = row[2]
        result['utype'] = row[3]
        result['uaddress'] = row[4]
        result['ucity'] = row[5]
        result['uregion'] = row[6]
        result['uzip'] = row[7]
        result['ustate'] = row[8]
        result['loclat'] = row[9]
        result['loclon'] = row[10]
        return result


    def build_part_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pmaterial'] = row[2]
        result['pcolor'] = row[3]
        result['pprice'] = row[4]
        result['quantity'] = row[5]
        return result

    def getResourceBySupllierIDdic(self,row):
        result={}
        result['uid'] = row[0]
        result['rid'] = row[1]
        result['rname'] = row[2]
        result['rprice'] = row[3]
        result['descpercent'] = row[4]
        result['rcategory'] = row[5]
        result['rqty'] = row[6]
        result['rregion'] = row[7]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_alluserinfo_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getAllSuppliers(self):
        dao = UserDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_alluserinfo_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getAllCustomers(self):
        dao = UserDAO()
        customers_list = dao.getAllCustomers()
        result_list = []
        for row in customers_list:
            result = self.build_alluserinfo_dict(row)
            result_list.append(result)
        return jsonify(Customers=result_list)

    def getUserById(self, uid):
        dao = UserDAO()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            result = self.build_alluserinfo_dict(row)
        return jsonify(result)

    def getSupplierById(self, uid):
        dao = UserDAO()
        row = dao.getSupplierById(uid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result = self.build_alluserinfo_dict(row)
        return jsonify(result)

    def getCustomerById(self, uid):
        dao = UserDAO()
        row = dao.getCustomerById(uid)
        if not row:
            return jsonify(Error="Customers Not Found"), 404
        else:
            result = self.build_alluserinfo_dict(row)
        return jsonify(result)


    def getResourcesBySupplierId(self, uid):
        dao = UserDAO()
        if not dao.getResourcesBySupplierId(uid):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(uid)
        result_list = []
        for row in resources_list:
            result = self.getResourceBySupllierIDdic(row)
            result_list.append(result)
        return jsonify(ResourcesSupply=result_list)
    '''
    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            city = args.get("city")
            if city:
                dao = UserDAO()
                supplier_list = dao.getSuppliersByCity(city)
                result_list = []
                for row in supplier_list:
                    result = self.build_user_dict(row)
                    result_list.append(row)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

'''

