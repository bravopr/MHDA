from flask import jsonify
from dao.ResourcesDAO import ResourcesDAO
from dao.UserDAO import UserDAO

class ResourcesHandler:

    def build_allresourcesinfo_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['uid'] = row[1]
        result['rname'] = row[2]
        result['rprice'] = row[3]
        result['descpercent'] = row[4]
        result['rcategory'] = row[5]
        result['rqty'] = row[6]
        result['rregion'] = row[7]
        return result

    def build_SupplierByResourcesId_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['uid'] = row[1]
        result['uname'] = row[2]
        result['ulast'] = row[3]
        result['uaddress'] = row[4]
        result['ucity'] = row[5]
        result['uregion'] = row[6]
        result['uzip'] = row[7]
        result['ustate'] = row[8]
        result['loclat'] = row[9]
        result['loclon'] = row[10]
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getResourceById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result = self.build_allresourcesinfo_dict(row)
        return jsonify(result)

    def getResourceByCategory(self, rcategory):
        dao = ResourcesDAO()
        resources_list = dao.getResourceByCategory(rcategory)
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getResourceByQty(self, rqty):
        dao = ResourcesDAO()
        resources_list = dao.getResourceByQty(rqty)
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getResourceByRegion(self, rregion):
        dao = ResourcesDAO()
        resources_list = dao.getResourceByRegion(rregion)
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict(row)
            result_list.append(result)
        return jsonify(result_list)

    def getResourceByName(self, rname):
        dao = ResourcesDAO()
        row = dao.getResourceByName(rname)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result = self.build_allresourcesinfo_dict(row)
        return jsonify(result)

    def getResourceByDesc(self, descpercent_filter):
        dao = ResourcesDAO ()
        resources_list = dao.getResourceByDesc (descpercent_filter)
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getResourceByPrice(self, rprice_filter):
        dao = ResourcesDAO ()
        resources_list = dao.getResourceByPrice (rprice_filter)
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getSupplierByResourcesId(self, rid):
        dao = ResourcesDAO ()
        if not dao.getSupplierByResourcesId (rid):
            return jsonify (Error="Supplier Not Found"), 404
        resources_list = dao.getSupplierByResourcesId (rid)
        result_list = []
        for row in resources_list:
            result = self.build_SupplierByResourcesId_dict (row)
            result_list.append (result)
        return jsonify (SupplierByResources=result_list)

    def getResourceByCategoryAndRegion (self, rcategory, rregion):
        dao = ResourcesDAO ()
        resources_list = dao.getResourceByCategoryAndRegion (rcategory, rregion)
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def getAllResourcesAvailable(self):
        dao = ResourcesDAO ()
        resources_list = dao.getAllResourcesAvailable ()
        result_list = []
        for row in resources_list:
            result = self.build_allresourcesinfo_dict (row)
            result_list.append (result)
        return jsonify (result_list)

    def searchResources(self, args):
        rid_filter = args.get("rid")
        uid_filter = args.get("uid")
        rname_filter = args.get("rname")
        rprice_filter = args.get ("rprice")
        descpercent_filter = args.get ("descpercent")
        rcategory_filter = args.get("rcategory")
        rqty_filter = args.get ("rqty")
        rregion_filter = args.get ("rregion")
        if (len(args) == 1) and rid_filter:
            return (ResourcesHandler().getResourceById(rid_filter))
        elif (len(args) == 1) and uid_filter:
            return (ResourcesHandler ().getSupplierByResourcesId (uid_filter))
        elif (len(args) == 1) and rname_filter:
            return (ResourcesHandler ().getResourceByName (rname_filter))
        elif (len (args) == 1) and rprice_filter:
            return (ResourcesHandler ().getResourceByPrice (rprice_filter))
        elif (len(args) == 1) and descpercent_filter:
            return (ResourcesHandler ().getResourceByDesc (descpercent_filter))
        elif (len(args) == 1) and rcategory_filter:
            return (ResourcesHandler ().getResourceByCategory (rcategory_filter))
        elif (len(args) == 1) and rregion_filter:
            return (ResourcesHandler ().getResourceByRegion (rregion_filter))
        elif (len(args) == 1) and rqty_filter:
            return (ResourcesHandler ().getResourceByQty (rqty_filter))
        elif (len(args) == 2) and rcategory_filter and rregion_filter:
            return (ResourcesHandler ().getResourceByCategoryAndRegion (rcategory_filter,rregion_filter))
        else:
            return jsonify(Error = "Malformed query string"), 400


    def insertResource(self, form):
        pass





