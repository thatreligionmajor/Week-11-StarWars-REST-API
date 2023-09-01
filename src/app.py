"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, people
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# people
#get all people
@app.route('/people', methods=['GET'])
def handle_get_all_people():
    json_text = jsonify(people)
    return json_text
#get one person
@app.route('/people'<int:people_id>, methods=['GET'])
def handle_get_one_person():
    json_text = jsonify(person)
    return json_text

# planets 
# get all planets
@app.route('/planets', methods=['GET'])
def handle_get_all_planets():
    response_body = {
        "msg": "Hello, this is your GET /planets response "
    }
    return jsonify(response_body), 200
#get one planet
@app.route('/people'<int:planet_id>, methods=['GET'])
def handle_get_one_planet():
    response_body = {
        "msg": "Hello, this is your GET /planet response "
    }
    return jsonify(response_body), 200

# users
# get all users
@app.route('/users', methods=['GET'])
def handle_get_all_users():
    response_body = {
        "msg": "Hello, this is your GET /users response "
    }
    return jsonify(response_body), 200
# favorites
# get all favorites from current user # delete planet, delete people
@app.route('/users/favorites', methods=['GET'])
def handle_get_all_user_favorites():
    response_body = {
        "msg": "Hello, this is your GET /users/favorites response "
    }
    return jsonify(response_body), 200

#post favorite planet
@app.route('/users/favorites/planet/'<int:planet_id>, methods=['POST'])
def handle_post_favorite_planet():
    response_body = {
        "msg": "Hello, this is your GET /users/favorite/planet response "
    }
    return jsonify(response_body), 200

#post favorite people
@app.route('/users/favorites/people/'<int:people_id>, methods=['POST'])
def handle_post_favorite_people():
    response_body = {
        "msg": "Hello, this is your GET /users/favorite/people response "
    }
    return jsonify(response_body), 200
#delete favorite planet
@app.route('/favorite/planet/uid', methods=['DELETE'])
def delete_favorite_planet(position):
    print("This is the position to delete planet: ", position)
    todos.pop((position-1))
    return jsonify(#unknown)
#delete favorite person
@app.route('/favorite/people/uid', methods=['DELETE'])
def delete_favorite_person(position):
    print("This is the position to delete person: ", position)
    todos.pop((position-1))
    return jsonify(#unknown)

        

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
