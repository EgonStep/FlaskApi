from flask import Blueprint, abort, jsonify
from flask_restful import Resource, reqparse
from my_app.console.models import Console
from my_app import api, db

console = Blueprint('console', __name__)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('year', type=int)
parser.add_argument('price', type=float)
parser.add_argument('total_games', type=int)
parser.add_argument('is_active', type=bool)


# Endpoint creation
@console.route("/")
@console.route("/home")
def home():
    return "Catalogo de Consoles"


class ConsoleAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            consoles = Console.query.paginate(page, 10).items
            res = []
            for con in consoles:
                res.append({
                    'id': con.id,
                    'name': con.name,
                    'year': con.year,
                    'price': con.price,
                    'total_games': con.total_games,
                    'is_active': con.is_active
                })
            return jsonify(res)
        else:
            consoles = [Console.query.get(id)]
            res = {}
            for con in consoles:
                res = {
                    'id': con.id,
                    'name': con.name,
                    'year': con.year,
                    'price': con.price,
                    'total_games': con.total_games,
                    'is_active': con.is_active
                }
            return jsonify(res)
        if not consoles:
            abort(404)  # HttpStatus

    def post(self):
        args = parser.parse_args()
        name = args['name']
        year = args['year']
        price = args['price']
        total_games = args['total_games']
        is_active = args['is_active']

        con = Console(name, year, price, total_games, is_active)
        db.session.add(con)
        db.session.commit()

        res = {
            'id': con.id,
            'name': con.name,
            'year': con.year,
            'price': con.price,
            'total_games': con.total_games,
            'is_active': con.is_active
        }
        return jsonify(res)

    def delete(self, id):
        con = Console.query.get(id)
        db.session.delete(con)
        db.session.commit()

        res = {'id': id}
        return jsonify(res)

    def put(self, id):
        con = Console.query.get(id)
        args = parser.parse_args()
        name = args['name']
        year = args['year']
        price = args['price']
        total_games = args['total_games']
        is_active = args['is_active']

        con.name = name
        con.year = year
        con.price = price
        con.total_games = total_games
        con.is_active = is_active
        db.session.commit()

        res = {
            'id': con.id,
            'name': con.name,
            'year': con.year,
            'price': con.price,
            'total_games': con.total_games,
            'is_active': con.is_active
        }
        return jsonify(res)


api.add_resource(
    ConsoleAPI,
    '/api/consoles',
    '/api/consoles/<int:id>',
    '/api/consoles/<int:id>/<int:page>',
)
