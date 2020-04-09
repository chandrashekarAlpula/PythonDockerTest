from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json
import redis

app = Flask(__name__)
api = Api(app)

db = redis.Redis(host='redis', port=6379)

class RedisUpdate(Resource):
    def post(self):
        data = request.get_json()
        jdata = json.dumps(data)
        id = data["id"]
        db.set(id, jdata)

        return jsonify({"ResponseData": data})


class RedisGet(Resource):
    def get(self, _id):        
        #data = request.get_json()
        #id = data["id"]

        d1 = json.loads(db.get(_id))
        #return jsonify({"Response": data["name"]})
        return jsonify({"Response": d1})

api.add_resource(RedisGet, "/GetData/<_id>")
api.add_resource( RedisUpdate, "/SetData")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug= True)



