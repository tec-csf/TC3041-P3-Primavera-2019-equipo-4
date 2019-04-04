#!/usr/bin/env python


import json

from bottle import get, run, request, response, static_file
from py2neo import Graph


#password = {Your neo4j password}
graph = Graph(password = "admin")


@get("/")
def get_index():

    result = graph.evaluate("MATCH(n) return (n)")

    return result
    #return static_file("index.html", root="static")


if __name__ == "__main__":
    run(port=8080)
