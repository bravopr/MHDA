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
            return jsonify(Error="ResourcesBySupplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(uid)
        result_list = []
        for row in resources_list:
            result = self.getResourceBySupllierIDdic(row)
            result_list.append(result)
        return jsonify(ResourcesBySupplier=result_list)

    def getUserByName(self, uname):
        dao = UserDAO()
        user_list = dao.getUserByName(uname)
        result_list = []
        if not user_list:
            return jsonify(Error="Customers Not Found"), 404
        else:
            result = self.build_alluserinfo_dict(user_list)
        return jsonify(result)

    def getUserByLastname(self, ulast):
        dao = UserDAO ()
        user_list = dao.getUserByLastname (ulast)
        result_list = []
        if not user_list:
            return jsonify (Error="Customers Not Found"), 404
        else:
            result = self.build_alluserinfo_dict (user_list)
        return jsonify (result)

    def getUserByType(self, utype):
        dao = UserDAO ()
        user_list = dao.getUserByType (utype)
        result_list = []
        for row in user_list:
            result = self.build_alluserinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getUserByCity(self, ucity):
        dao = UserDAO ()
        user_list = dao.getUserByCity (ucity)
        result_list = []
        for row in user_list:
            result = self.build_alluserinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getUserByRegion(self, uregion):
        dao = UserDAO ()
        user_list = dao.getUserByRegion (uregion)
        result_list = []
        for row in user_list:
            result = self.build_alluserinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getUserByZip(self, uzip):
        dao = UserDAO ()
        user_list = dao.getUserByZip (uzip)
        result_list = []
        for row in user_list:
            result = self.build_alluserinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getUserByState(self, ustate):
        dao = UserDAO ()
        user_list = dao.getUserByState (ustate)
        result_list = []
        for row in user_list:
            result = self.build_alluserinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def searchUsers(self, args):
        uid_filter = args.get ("uid")
        uname_filter = args.get ("uname")
        ulast_filter = args.get ("ulast")
        utype_filter = args.get ("utype")
        #uaddress_filter = args.get ("uaddress")
        ucity_filter = args.get ("ucity")
        uregion_filter = args.get ("uregion")
        uzip_filter = args.get ("uzip")
        ustate_filter = args.get ("ustate")
        loclat_filter = args.get ("loclat")
        loclon_filter = args.get ("loclon")
        if (len (args) == 1) and uid_filter:
            return (UserHandler ().getUserById (uid_filter))
        elif (len (args) == 1) and uname_filter:
            return (UserHandler ().getUserByName (uname_filter))
        elif (len (args) == 1) and ulast_filter:
            return (UserHandler ().getUserByLastname (ulast_filter))
        elif (len (args) == 1) and utype_filter:
            return (UserHandler ().getUserByType (utype_filter))
        #elif (len (args) == 1) and uaddress_filter:
        #    return (UserHandler ().getUserByAddress (uaddress_filter))
        elif (len (args) == 1) and ucity_filter:
            return (UserHandler ().getUserByCity (ucity_filter))
        elif (len (args) == 1) and uregion_filter:
            return (UserHandler ().getUserByRegion (uregion_filter))
        elif (len (args) == 1) and uzip_filter:
            return (UserHandler ().getUserByZip (uzip_filter))
        elif (len (args) == 1) and ustate_filter:
            return (UserHandler ().getUserByState (ustate_filter))
        #elif (len (args) == 1) and loclat_filter:
        #    return (UserHandler ().getUserByloclat (loclat_filter))
        #elif (len (args) == 1) and loclon_filter:
        #    return (UserHandler ().getUserByloclon (loclon_filter))
        else:
            return jsonify (Error="Malformed query string"), 400
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

    def insertResource(self, form):
        pass















