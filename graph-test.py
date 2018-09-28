from neo4j.v1 import GraphDatabase
from PyHugeGraph import PyHugeGraphClient

if __name__ == '__main__':
    hg = PyHugeGraphClient.HugeGraphClient("http://loaclhost:8090", "hugegraph")
    print hg.graph
    print hg.get_all_graphs().response
    print hg.get_vertex_by_id("123").response
    print hg.get_all_vertelabels().response

    # print hg.GetAllGraphs().response
    # print hg.GetVersion().response
    # print hg.GetGraphInfo().response
    # print hg.CreatePropertyKey('testname', 'TEXT', 'SINGLE').response
    print hg.get_graph_allpropertykeys().response
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
    # print hg.GetAllVerteLabels().response
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
    # print hg.GetVertexByCondition("character").response
    # print hg.GetVertexById("1:hydra").response
    # print hg.GetVertexByCondition("").response
    # print hg.GetVertexByPage(4, "AAuGMTpoeWRyYWcBEQAAAAA=").response

    # print hg.GetEdgeByCondition().response
    # print hg.GetEdgeByPage(3).response
    # print hg.GetEdgeByID("S1:pluto>4>>S2:tartarus").response
    # print hg.TraverserShortestPath("1:hercules", "1:pluto", "OUT", 2).response
    # print hg.TraverserKout("1:hercules", "OUT", 1).response
    # print hg.TraverserKneighbor("1:hercules", "OUT", 2).response
    # ids = ["1:jupiter", "1:cerberus", "2:tartarus", "1:alcmene", "1:hydra", "2:sky", "1:saturn", "1:pluto",
    #        "1:hercules", "1:neptune", "1:nemean"]
    # print hg.TraverserVertices(ids).response

    # print hg.CreateVariables("title","test").response
    # print hg.UpdateVariables("title","testnew").response
    # print hg.GetAllVariables().response
    # print hg.GetVariablesByKey("title").response
    # print hg.DeleteVariables("title").response
    # print hg.GetAllVariables().response
