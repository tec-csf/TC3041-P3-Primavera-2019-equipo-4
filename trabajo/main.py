from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

def menu():
    inp=0
    while inp!="4":
        print("\nQueries disponibles:\n"
              "1. Desplegar las 10 personas que más confian en otras\n"
              "2. Desplegar las 10 personas en las que más se confía\n"
              "3. Desplegar 10 personas que no confian en nadie\n"
              "4. Cerrar programa\n")

        inp = input("Selecciona la opción que desees ejecutar:\n")
        if inp == "1":
            with driver.session() as session:
                session.read_transaction(mas_confia_en)
        if inp == "2":
            with driver.session() as session:
                session.read_transaction(mas_confiado_por)
        if inp == "3":
            with driver.session() as session:
                session.read_transaction(no_confia)

def mas_confia_en(tx):
    result = tx.run("match (n:Person)-[r:Trusts]->(s) with n,count(r) as ntrusts return n.id, ntrusts order by ntrusts desc limit 10;")
    for record in result:
        trust = record["n.id"]
        ntrusts = record["ntrusts"]
        print("La persona %s confia en %s personas" % (trust, ntrusts))

def mas_confiado_por(tx):
    result = tx.run("match (n:Person)<-[r:Trusts]-(s) with n,count(r) as ntrusts return n.id, ntrusts order by ntrusts desc limit 10;")
    for record in result:
        trust = record["n.id"]
        ntrusts = record["ntrusts"]
        print("La persona %s es confiada por %s personas" % (trust, ntrusts))

def no_confia(tx):
    result = tx.run("match (p:Person) where not (p)-[:Trusts]->() return p.id limit 10;")
    for record in result:
        trust = record["p.id"]
        print("La persona %s no confia en nadie" % (trust))

menu()

