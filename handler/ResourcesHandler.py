from flask import jsonify
from dao.ResourcesDAO import ResourcesDAO


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