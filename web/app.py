from flask import Flask,jsonify,request
from flask_restful import Api,Resource

# adhoc change to git master

app = Flask(__name__)
api = Api(app)


def checkposteddata(posteddata,funcname):
    
    if funcname in ["add","subtract","multiply"]:
        if "x" not in posteddata or "y" not in posteddata:
            return 300
        else:
            return 200
    
    elif funcname == "divide":
        if posteddata["y"] == 0:
            return 301
        if "x" not in posteddata or "y" not in posteddata:
            return 300


class Add(Resource):
    def post(self):
        posteddata = request.get_json()
        ret_stat = checkposteddata(posteddata,"add")
        
        if ret_stat != 200:
            retjson = {

                "message" : "invalid data sent"
            }

        else:
            x = posteddata["x"]
            y = posteddata["y"]
            z = int(x) + int(y)
            
            retjson = {
            
            "result": z
        }

        return jsonify(retjson)
    
    


class Subtract(Resource):
    def post(self):
        posteddata = request.get_json()
        ret_stat = checkposteddata(posteddata,"add")
        
        if ret_stat != 200:
            retjson = {

                "message" : "invalid data sent"
            }

        else:
            x = posteddata["x"]
            y = posteddata["y"]
            z = int(x) - int(y)
            
            retjson = {
            
            "result": z
        }

        return jsonify(retjson)
    
    

class Multiply(Resource):
    def post(self):
        posteddata = request.get_json()
        ret_stat = checkposteddata(posteddata,"add")
        
        if ret_stat != 200:
            retjson = {

                "message" : "invalid data sent"
            }

        else:
            x = posteddata["x"]
            y = posteddata["y"]
            z = int(x) * int(y)
            
            retjson = {
            
            "result": z
        }

        return jsonify(retjson)
    

class Divider(Resource):
    def post(self):
        posteddata = request.get_json()
        ret_stat = checkposteddata(posteddata,"add")
        
        if ret_stat != 200:
            
            retjson = {

                "message" : "invalid data sent"
            }

        else:
            x = posteddata["x"]
            y = posteddata["y"]
            z = int(x) / int(y)
            
            retjson = {
            
            "result": z
        }

        return jsonify(retjson)


api.add_resource(Add,"/add")
api.add_resource(Subtract,"/sub")
api.add_resource(Multiply,"/multi")
api.add_resource(Divider,"/dvd")


@app.route('/')
def say_hello():
    return "Hello"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

