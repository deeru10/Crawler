from py2neo import Graph, Node, Relationship
import sys
from time import sleep
graph_database_location = "http://192.168.100.53:7474/db/data/"
graph = Graph(graph_database_location, user='neo4j', password='cns2202') # connect to the local graph database

tx=graph.begin()

statement = 'Match (a:Main_Tab)-[c:Crawling_Complete]->(b:Completed) WHERE ((a.Crawler="CRAWLER-1")) RETURN c'
count=[]
flag_detected = 0
if (sys.argv[1] == "CRAWLER-1"):
    flag_detected = 1
else:
    while True:
        print("Okay I am gonna sleep for 30 seconds and Check again")
        sleep(30)
        
        cursor=tx.run(statement).data()
        print(cursor)
        if(len(cursor) != 0):
            for each in cursor:
                x=list(each.values())
                count.append(x[0])
        if (len(count) != 0):
            flag_detected = 1
            break

if( flag_detected == 1):
    print("Detected Completion")
    
