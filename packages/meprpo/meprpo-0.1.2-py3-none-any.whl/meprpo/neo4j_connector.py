from neo4j import GraphDatabase


class Neo4jConnector:
    def __init__(self, uri, username, password):
        self.uri = uri
        self.username = username
        self.password = password
        self.driver = None

    def connect(self):
        self.driver = GraphDatabase.driver(self.uri, auth=(self.username, self.password))

    def close(self):
        if self.driver is not None:
            self.driver.close()


def connect_to_neo4j(uri, username, password):
    connector = Neo4jConnector(uri, username, password)
    connector.connect()
    return connector
