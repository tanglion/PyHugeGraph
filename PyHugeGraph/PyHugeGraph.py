# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     HugeGraph.py
   Description :
   Author :       tangjiawei
   date:          2018/08/23
-------------------------------------------------
   Change Activity:
                   2018/08/23: v1
-------------------------------------------------
"""
from Response import Response
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class HugeGraph():
    """
    HugeGraph restful API
    """

    def __init__(self, host,graph_name):
        self.host = ""
        if host.startswith("http://"):
            self.host = host
        else:
            self.host = "http://" + host
        self.graph = graph_name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Content-Type': 'application/json'
        }
        self.token = "162f7848-0b6d-4faf-b557-3a0797869c55"
        self.conform_message = "I%27m+sure+to+delete+all+data"

    def GetAllGraphs(self):
        """
        列出数据库中全部的图（传统数据库中的数据库database）
        :return:
        """
        url = self.host + "/graphs"
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetVersion(self):
        """
        查看HugeGraph的版本信息
        :return:
        """
        url = self.host + "/versions"
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetGraphInfo(self):
        """
        查看某个图的信息
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def ClearGraphAllData(self):
        """
        清空某个图的全部数据，包括schema、vertex、edge和索引等，该操作需要管理员权限
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "clear?token=" + self.token + "&confirm_message=" + self.conform_message
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetGraphConfig(self):
        """
        查看某个图的配置，该操作需要管理员权限
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "conf?token=" + self.token
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreatePropertyKey(self, propertykey_name, dataType, cardinality):
        """
        创建一个propertykey
        :param property_name:
        :param dataType: INT TEXT
        :param cardinality:  SINGLE
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys"
        propertykeys = {
            "name": propertykey_name,
            "data_type": dataType,
            "cardinality": cardinality

        }
        response = requests.post(url, data=json.dumps(propertykeys), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def AddPropertykeyUserdata(self, property_name, user_data):
        """
        为已存在的 PropertyKey 添加userdata
        :param property_name:
        :param user_data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" + "/" + property_name + "?action=append"
        data = {
            "name": property_name,
            "user_data": user_data
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeletePropertykeyUserdata(self, property_name, user_data):
        """
        为已存在的 PropertyKey 移除 userdata
        :param property_name:
        :param user_data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" + "/" + property_name + "?action=eliminate"
        data = {
            "name": property_name,
            "user_data": user_data
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetGraphAllPropertykeys(self):
        """
        获取所有的 PropertyKey
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys"
        response = requests.get(url)
        res = Response(response.status_code, response.content)
        return res

    def GetGraphPropertykeyByName(self, property_name):
        """
        根据name获取PropertyKey
        :param property_name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" + "/" + property_name
        response = requests.get(url)
        res = Response(response.status_code, response.content)
        return res

    def DeleteGraphPropertykeyByName(self, property_name):
        """
        根据name删除PropertyKey
        :param property_name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" + "/" + property_name
        response = requests.delete(url)
        res = Response(response.status_code, response.content)
        return res

    def CreateVertexLabel(self, data):
        """
        创建一个VertexLabel
        :param data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def AddVertexLabelProperties(self, name, properties, nullable=[]):
        """
        为一个VertexLabel添加properties属性
        :param name:
        :param properties:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name + "?action=append"
        data = {
            "name": name,
            "properties": properties,
            "nullable_keys": nullable
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    # def DeleteVertexLabelProperties(self,name, properties):
    #     """
    #     ***(此功能暂不支持)***
    #     为一个VertexLabel移除properties属性
    #     :param name:
    #     :param properties:
    #     :return:
    #     """
    #     url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name + "?action=eliminate"
    #     data = {
    #         "name": name,
    #         "properties": properties
    #     }
    #     response = requests.put(url,data = json.dumps(data), headers = self.headers)
    #     res = Response(response.status_code, response.content)
    #     return res

    def AddVertexLabelUserdata(self, name, userdata):
        """
        为一个VertexLabel添加userdata属性
        :param name:
        :param userdata:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name + "?action=append"
        data = {
            "name": name,
            "user_data": userdata
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteVertexLabelUserdata(self, name, userdata):
        """
        为一个VertexLabel删除userdata属性
        :param name:
        :param userdata:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name + "?action=eliminate"
        data = {
            "name": name,
            "user_data": userdata
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetAllVerteLabels(self):
        """
        获取所有的VertexLabel
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels"
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetVerteLabelByName(self, name):
        """
        根据name获取VertexLabel
        :param name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteVerteLabelByName(self, name):
        """
        根据name删除VertexLabel
        :param name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateEdgeLabel(self, data):
        """
        创建一个EdgeLabel
        :param data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def AddEdgeLabelProperties(self, name, properties, nullable=[]):
        """
        为一个EdgeLabel添加properties
        :param name:
        :param properties:
        :param nullable:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name + "?action=append"
        data = {
            "name": name,
            "properties": properties,
            "nullable_keys": nullable
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def AddEdgeLabelUserdata(self, name, userdata):
        """
        为一个EdgeLabel添加userdata
        :param name:
        :param userdata:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name + "?action=append"
        data = {
            "name": name,
            "user_data": userdata
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteEdgeLabelUserdata(self, name, userdata):
        """
        为一个EdgeLabel删除userdata
        :param name:
        :param userdata:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name + "?action=eliminate"
        data = {
            "name": name,
            "user_data": userdata
        }
        response = requests.put(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetAllEdgeLabels(self):
        """
        获取所有的EdgeLabels
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels"
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetEdgeLabelByName(self, name):
        """
        根据name获取EdgeLabel
        :param name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteEdgeLabelByName(self, name):
        """
        根据name删除EdgeLabel
        :param name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateIndexLabel(self, data):
        """
        创建一个IndexLabel
        :param data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetAllIndexLabels(self):
        """
        获取所有的indexlabel
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels"
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetIndexLabelByName(self, name):
        """
        根据name获取indexlabel
        :param name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels" + "/" + name
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteIndexLabelByName(self, name):
        """
        根据name删除indexlabel
        :param name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels" + "/" + name
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateVertex(self, label, properties):
        """
        创建一个顶点
        :param label:
        :param properties:
        :return:
        """
        data = {
            "label": label,
            "properties": properties
        }
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateMultiVertex(self, data):
        """
        创建多个顶点
        :param data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/batch"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def UpdateVertexProperties(self, vertex_id, label, properties):
        """
        更新顶点属性
        :param vertex_id:
        :param label:
        :param properties:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/" + vertex_id + "?action=append"
        data = {
            "label": label,
            "properties": properties
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteVertexProperties(self, vertex_id, label, properties):
        """
        删除顶点属性
        :param vertex_id:
        :param label:
        :param properties:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/" + vertex_id + "?action=eliminate"
        data = {
            "label": label,
            "properties": properties
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetVertexByCondition(self, label="", properties={}, limit=0):
        """
        获取符合条件的顶点
        :param label:
        :param properties:
        :param limit:
        :param page:
        :return:
        """
        # 以上参数都是可选的，如果提供page参数，必须提供limit参数，不允许带其他参数。"/graphs" + "/" + self.graph + "/graph/vertices?"
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices?"
        para = ""
        if label != "":
            para = para + "&label=" + label
        if properties != {}:
            para = para + "&properties=" + properties
        if limit > 0:
            para = para + "&limit=" + limit
        url = url + para[1:]
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetVertexByPage(self, limit, page=""):
        """
        获取符合条件的顶点 ，如果提供page参数，必须提供limit参数，不允许带其他参数
        :param page:
        :param limit:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices?"
        if page == "":
            if limit <= 0:
                res = Response(400, "parameter：limit can not be empty ")
            else:
                url = url + "page&limit=" + str(limit)
        else:
            url = url + "page=" + str(page) + "&limit=" + str(limit)
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetVertexById(self, vertex_id):
        """
        根据ID 获取顶点
        :param vertex_id:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/\"" + vertex_id + "\""
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteVertexById(self, vertex_id):
        """
        根据ID 删除顶点
        :param vertex_id:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/\"" + vertex_id + "\""
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateEdge(self, edge_label, outv, inv, outv_label, inv_label, properties):
        """
        创建一条边
        :param edge_label:
        :param outv:
        :param inv:
        :param outv_label:
        :param inv_label:
        :param properties:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges"
        data = {
            "label": edge_label,
            "outV": outv,
            "inV": inv,
            "outVLabel": outv_label,
            "inVLabel": inv_label,
            "properties": properties
        }
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateMultiEdge(self, data):
        """
        创建多条边
        :param data:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/batch"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def UpdateEdgeProperties(self, edge_id, properties):
        """
        更新边的属性
        :param properties:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/" + edge_id + "?action=append"
        data = {
            "properties": properties
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteEdgeProperties(self, edge_id, properties):
        """
        删除边的属性
        :param properties:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/" + edge_id + "?action=eliminate"
        data = {
            "properties": properties
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetEdgeByCondition(self, vertex_id="", direction="", label="", properties={}, limit=0):
        """
        根据条件查询获取边
        :param vertex_id: vertex_id为可选参数，如果提供参数vertex_id则必须同时提供参数direction。
        :param direction: (IN | OUT | BOTH)
        :param label:
        :param properties:
        :param limit:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges?"
        para = ""
        if vertex_id != "":
            if direction != "":
                para = para + "&vertex_id=" + vertex_id + "&direction=" + direction
            else:
                return Response(400, "direction can not be empty")
        if label != "":
            para = para + "&label=" + label
        if properties != {}:
            para = para + "&properties=" + properties
        if limit > 0:
            para = para + "&limit=" + limit
        url = url + para[1:]
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetEdgeByPage(self, limit, page=""):
        """
        获取符合条件的边 ，如果提供page参数，必须提供limit参数，不允许带其他参数
        :param limit:
        :param page:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges?"
        if page == "":
            if limit <= 0:
                res = Response(400, "parameter：limit can not be empty ")
            else:
                url = url + "page&limit=" + str(limit)
        else:
            url = url + "page=" + str(page) + "&limit=" + str(limit)
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetEdgeByID(self, edge_id):
        """
        根据Id 获取边
        :param edge_id:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/" + edge_id
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteEdgeByID(self, edge_id):
        """
        根据Id 删除边
        :param edge_id:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/" + edge_id
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def TraverserShortestPath(self, source, target, direction, max_depth, label=""):
        """
        根据起始顶点、目的顶点、方向、边的类型（可选）和最大深度，查找一条最短路径
        :param source:
        :param target:
        :param direction: (IN | OUT | BOTH)
        :param max_depth:
        :param label:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/shortestpath?"
        para = ""
        if source == "":
            return Response(400, "source can not be empty")
        else:
            para = para + "&source=\"" + source + "\""
        if target == "":
            return Response(400, "target can not be empty")
        else:
            para = para + "&target=\"" + target + "\""
        if direction == "":
            return Response(400, "direction can not be empty")
        else:
            para = para + "&direction=" + direction
        if max_depth == "":
            return Response(400, "max_depth can not be empty")
        else:
            para = para + "&max_depth=" + str(max_depth)
        if label != "":
            para = para + "&label=" + label

        url = url + para[1:]
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def TraverserKout(self, source, direction, depth, label="", nearest="true"):
        """
        根据起始顶点、方向、边的类型（可选）和深度depth，查找从起始顶点出发恰好depth步可达的顶点
        :param source: 起始顶点id
        :param direction: 起始顶点向外发散的方向（OUT,IN,BOTH）
        :param depth: 步数
        :param label: 边的类型
        :param nearest: 默认为true，代表起始顶点到达结果顶点的最短路径长度为depth，不存在更短的路径；nearest为false时，代表起始顶点到结果顶点有一条长度为depth的路径（未必最短且可以有环)
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kout?"
        para = ""
        if source == "":
            return Response(400, "source can not be empty")
        else:
            para = para + "&source=\"" + source + "\""
        if direction == "":
            return Response(400, "direction can not be empty")
        else:
            para = para + "&direction=" + direction
        if depth == "":
            return Response(400, "depth can not be empty")
        else:
            para = para + "&depth=" + str(depth)
        if label != "":
            para = para + "&label=" + label
        if nearest != "":
            para = para + "&nearest=" + label

        url = url + para[1:]
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def TraverserKneighbor(self, source, direction, depth, label=""):
        """
        根据起始顶点、方向、边的类型（可选）和深度depth，查找包括起始顶点在内、depth步之内可达的所有顶点
        :param source: 起始顶点id
        :param direction: 起始顶点向外发散的方向（OUT,IN,BOTH）
        :param depth: 步数
        :param label: 边的类型
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kneighbor?"
        para = ""
        if source == "":
            return Response(400, "source can not be empty")
        else:
            para = para + "&source=\"" + source + "\""
        if direction == "":
            return Response(400, "direction can not be empty")
        else:
            para = para + "&direction=" + direction
        if depth == "":
            return Response(400, "depth can not be empty")
        else:
            para = para + "&depth=" + str(depth)
        if label != "":
            para = para + "&label=" + label

        url = url + para[1:]
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def TraverserVertices(self, vertex_ids):
        """
        根据顶点的id列表，批量查询顶点
        :param vertex_ids: 要查询的顶点id列表
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/vertices?"
        para = ""
        for id in vertex_ids:
            para = para + "&ids=\"" + id + "\""
        url = url + para[1:]
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def CreateVariables(self, key, value):
        """
        创建某个键值对
        :param key:
        :param value:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        data = {
            "data": value
        }
        response = requests.put(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def UpdateVariables(self, key, value):
        """
        更新某个键值对
        :param key:
        :param value:
        :return:
        """
        return self.CreateVariables(key, value)

    def GetAllVariables(self):
        """
        列出全部键值对
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/"
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetVariablesByKey(self, key):
        """
        列出某个键值对
        :param key:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteVariables(self, key):
        """
        删除某个键值对
        :param key:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetGraphAllTasks(self, status="success", limit=""):
        """
        列出某个图中全部的异步任务
        :param status: 异步任务的状态(success,failed)
        :param limit: 返回异步任务数目上限
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks?status=" + status
        if limit != "":
            url = url + "&limit=" + limit
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def GetGraphTaskInfo(self, task_id):
        """
        查看某个任务的信息
        :param task_id:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def DeleteGraphTaskInfo(self, task_id):
        """
        删除某个异步任务信息，不删除异步任务本身
        :param task_id:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id
        response = requests.delete(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def RebuildIndexLabel(self, indexlabel_name):
        """
        重建IndexLabel
        :param indexlabel_name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/jobs/rebuild/indexlabels/" + indexlabel_name
        response = requests.put(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def RebuildVertexLabel(self, vertexlabel_name):
        """
        重建vertexlabel
        :param vertexlabel_name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/jobs/rebuild/vertexlabels/" + vertexlabel_name
        response = requests.put(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def RebuildEdgeLabel(self, edgelabel_name):
        """
        重建edgelabel
        :param edgelabel_name:
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/jobs/rebuild/edgelabels/" + edgelabel_name
        response = requests.put(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def ExecuteGermlinGet(self, gremlin, bindings={}, language="gremlin-groovy", aliases=""):
        """
        向HugeGraphServer发送gremlin语句（GET），同步执行
        :param gremlin: 要发送给HugeGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return:
        """
        url = self.host + "/gremlin?gremlin=" + gremlin
        if bindings != {}:
            url = url + "&bindings=" + bindings
        if language != "gremlin-groovy":
            url = url + "&language=" + language
        if aliases != "":
            url = url + "&aliases=" + aliases
        response = requests.get(url, headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def ExecuteGermlinPost(self, gremlin, bindings={}, language="gremlin-groovy", aliases=""):
        """
        向HugeGraphServer发送gremlin语句（post），同步执行
        :param gremlin: 要发送给HugeGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return:
        """
        url = self.host + "/gremlin"
        data = {
            "gremlin": gremlin,
            "bindings": bindings,
            "language": language,
            "aliases": aliases
        }
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

    def ExecuteGermlinPostJob(self, gremlin, bindings={}, language="gremlin-groovy"):
        """
        向HugeGraphServer发送gremlin语句（post），异步执行
        异步执行Gremlin语句暂不支持aliases，可以使用 graph 代表要操作的图，也可以直接使用图的名字， 例如 hugegraph; 另外g代表 traversal，等价于 graph.traversal() 或者 hugegraph.traversal()
        :param gremlin: 要发送给HugeGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return:
        """
        url = self.host + "/graphs" + "/" + self.graph + "/jobs/gremlin"
        data = {
            "gremlin": gremlin,
            "bindings": bindings,
            "language": language,
            "aliases": {}
        }
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        res = Response(response.status_code, response.content)
        return res

if __name__ == '__main__':
    hg = HugeGraph("10.14.139.15:8090","hugegraph")
    # print hg.GetAllGraphs().response
    # print hg.GetVersion().response
    # print hg.GetGraphInfo().response
    # print hg.CreatePropertyKey('testname', 'TEXT', 'SINGLE').response
    print hg.GetGraphAllPropertykeys().response
    # print hg.GetGraphPropertykeysByName("testname").response
    # print hg.DeleteGraphPropertykeysByName("curltest").status_code
    # user_data = {
    #     "min": 0,
    #     "max": 100
    # }
    # print hg.AddPropertykeyUserdata("age",user_data).response
    # print hg.DeletePropertykeyUserdata("age", {"min": 0}).response
    # ------------------------------------------
    # data = {
    #     "name": "person",
    #     "id_strategy": "DEFAULT",
    #     "properties": [
    #         "name",
    #         "age"
    #     ],
    #     "primary_keys": [
    #         "name"
    #     ],
    #     "nullable_keys": [],
    #     "enable_label_index": True
    # }
    # print hg.CreateVertexLabel(data).response
    # properties = ["reason",]
    # userdata = {
    #     "super": "animal"
    # }
    # print hg.AddVertexLabelProperties("person",properties).response
    # print hg.AddVertexLabelUserdata("person",userdata).response
    # print hg.DeleteVertexLabelUserdata("person",userdata).response
    # print hg.GetVerteLabelByName("person").response
    print hg.GetAllVerteLabels().response
    # ------------------------------------------
    # data = {
    #     "name": "created",
    #     "source_label": "person",
    #     "target_label": "person",
    #     "frequency": "SINGLE",
    #     "properties": [
    #         "time"
    #     ],
    #     "sort_keys": [],
    #     "nullable_keys": [],
    #     "enable_label_index": True
    # }
    # # print hg.CreateEdgeLabel(data).response
    # properties = [
    #     "type"
    # ]
    # nullable_keys = [
    #     "type"
    # ]
    # # print hg.AddEdgeLabelProperties("created", properties, nullable_keys).response
    # userdata = {
    #         "min": "1970-01-01"
    #     }
    # # print hg.AddEdgeLabelUserdata("created",userdata).response
    # # print hg.DeleteEdgeLabelUserdata("created",userdata).response
    # print hg.GetEdgeLabelByName("created").response
    # print hg.GetEdgeLabelByName("created").status_code
    # print hg.DeleteEdgeLabelByName("created").response
    # print hg.GetEdgeLabelByName("created").response
    # # print hg.GetAllEdgeLabels().response
    print hg.GetVertexByCondition("character").response
    # print hg.GetVertexById("1:hydra").response
    # print hg.GetVertexByCondition("").response
    # print hg.GetVertexByPage(4, "AAuGMTpoeWRyYWcBEQAAAAA=").response

    print hg.GetEdgeByCondition().response
    # print hg.GetEdgeByPage(3).response
    # print hg.GetEdgeByID("S1:pluto>4>>S2:tartarus").response
    print hg.TraverserShortestPath("1:hercules", "1:pluto", "OUT", 2).response
    print hg.TraverserKout("1:hercules", "OUT", 1).response
    print hg.TraverserKneighbor("1:hercules", "OUT", 2).response
    ids = ["1:jupiter", "1:cerberus", "2:tartarus", "1:alcmene", "1:hydra", "2:sky", "1:saturn", "1:pluto",
           "1:hercules", "1:neptune", "1:nemean"]
    print hg.TraverserVertices(ids).response

    # print hg.CreateVariables("title","test").response
    # print hg.UpdateVariables("title","testnew").response
    # print hg.GetAllVariables().response
    # print hg.GetVariablesByKey("title").response
    # print hg.DeleteVariables("title").response
    # print hg.GetAllVariables().response
