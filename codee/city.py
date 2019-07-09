from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

cities = [
    {
        "name": "New Delhi",
        "offer-type": "Lifestyle"
    },
    {
        "name": "Gurgaon",
        "offer-type": "Shopping"
    },
    {
        "name": "Noida",
        "offer-type": "Healthcare"
    }
]

class City(Resource):
    def get(self, name):
        for city in cities:
            if(name == city["name"]):
                return city, 200
        return "City not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("offer-type")
        args = parser.parse_args()

        for city in cities:
            if(name == city["name"]):
                return "City with name {} already exists".format(name), 400

        city = {
            "name": name,
            "offer-type": args["offer-type"]
        }
        cities.append(city)
        return city, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("offer-type")
        args = parser.parse_args()

        for city in cities:
            if(name == city["name"]):
                city["offer-type"] = args["offer-type"]
                return city, 200
        
        city = {
            "name": name,
            "offer-type": args["offer-type"]
        }
        cities.append(city)
        return city, 201

    def delete(self, name):
        global cities
        cities = [city for city in cities if city["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(City, "/http://127.0.0.1:5000/Users/503070370")

app.run(debug=True)