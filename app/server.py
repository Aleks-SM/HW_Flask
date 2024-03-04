import flask
from flask import views, jsonify, request
from models import Session, Adverts, Users
from sqlalchemy.exc import IntegrityError
from errors import HttpError
from schema import CreateAdv, UpdateAdv
from tools import validate


app = flask.Flask('app')


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response: flask.Response):
    request.session.close()
    return response


@app.errorhandler(HttpError)
def error_handler(error):
    response = jsonify({"error": error.description})
    response.status_code = error.status_code
    return response


def get_adv_by_id(adv_id: int):
    adv = request.session.get(Adverts, adv_id)
    if adv is None:
        raise HttpError(404, 'advertisement not found')
    return adv


def add_adv(adv: Adverts):
    try:
        request.session.add(adv)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "adv already exists")


class AdvView(views.MethodView):

    @property
    def session(self) -> Session:
        return request.session

    def get(self, adv_id: int):
        adv = get_adv_by_id(adv_id)
        return jsonify(adv.dict)

    def post(self):
        adv_data = validate(CreateAdv, request.json)
        adv = Adverts(**adv_data)
        add_adv(adv)
        return jsonify({"id": adv.id})

    def patch(self, adv_id: int):
        adv = get_adv_by_id(adv_id)
        adv_data = validate(UpdateAdv, request.json)
        for key, value in adv_data.items():
            setattr(adv, key, value)
            add_adv(adv)
        return jsonify({"id": adv.id})

    def delete(self, adv_id):
        adv = get_adv_by_id(adv_id)
        self.session.delete(adv)
        self.session.commit()
        return jsonify({'status': 'OK'})


adv_view = AdvView.as_view("adv_view")


app.add_url_rule("/adverts/<int:adv_id>", view_func=adv_view, methods=["GET", "PATCH", "DELETE"])
app.add_url_rule("/adverts", view_func=adv_view, methods=["POST"])


if __name__ == "__main__":
    app.run()
