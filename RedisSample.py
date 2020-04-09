import redis
import json

db = redis.Redis(host='localhost', port=6379, db=0)

data = {"name":"chandra", "id":1, "branch":"CSE"}
         
jdata = json.dumps(data)

print(type(str(jdata)))

id = data["id"]

db.set(id, jdata)

jdata1 = json.loads(db.get(id))
print(type(jdata1))

#print(dict1["name"])
