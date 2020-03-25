import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from my_app.series.models import Series
from my_app import api, db

series = Blueprint('series', __name__)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('genre', type=str)
parser.add_argument('seasons', type=int)
parser.add_argument('score', type=float)
parser.add_argument('is_active', type=bool)


class SeriesAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            series_in = Series.query.paginate(page, 10).items
        else:
            series_in = [Series.query.get(id)]
        if not series_in:
            abort(404)  # HttpStatus

        res = {}
        for single_series in series_in:
            res[single_series.id] = {
                'title': single_series.title,
                'genre': single_series.genre,
                'seasons': single_series.seasons,
                'score': str(single_series.score),
                'is_active': single_series.is_active
            }

        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        title = args['title']
        genre = args['genre']
        seasons = args['seasons']
        score = args['score']
        is_active = args['is_active']

        single_series = Series(title, genre, seasons, score, is_active)
        db.session.add(single_series)
        db.session.commit()

        res = {single_series.id: {
            'title': single_series.title,
            'genre': single_series.genre,
            'seasons': single_series.seasons,
            'score': str(single_series.score),
            'is_active': single_series.is_active
        }}
        return json.dumps(res)


api.add_resource(
    SeriesAPI,
    '/api/series',
    '/api/series/<int:id>',
    '/api/series/<int:id>/<int:page>',
)
