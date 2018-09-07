from neo4j.v1 import GraphDatabase
from PyHugeGraph import PyHugeGraph

class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

if __name__ == '__main__':

    # t = HelloWorldExample("bolt://localhost:7687","neo4j","neo4jcdc")
    # t.print_greeting("123")
    hg = PyHugeGraph.HugeGraph("http://10.14.139.15:8090","hugegraph")
    print hg.graph
    print hg.GetAllGraphs().response
    print hg.GetVertexById("123").response
    print hg.GetAllVerteLabels().response