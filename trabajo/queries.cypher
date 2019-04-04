//Query 1: Obtener el id de las diez primeras personas que más confían en otras personas
match (n:Person)-[r:Trusts]->(s) with n,count(r) as ntrusts return n.id, ntrusts order by ntrusts desc limit 10;

//Query 2: Obtener el id de las diez primeras personas en las que más confían
match (n:Person)<-[r:Trusts]-(s) with n,count(r) as ntrusts return n.id, ntrusts order by ntrusts desc limit 10;

//Query 3: Obtener el id de las personas que no confían en nadie
match (p:Person) where not (p)-[:Trusts]->() return p;
