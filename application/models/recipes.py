import requests
from application import app
from flask import request, jsonify


def get_recipes(filters):
    library_url = "https://studio.api.f45training.com/v1/strapi/recipe"
    result = requests.get(library_url, params=filters)
    return result.json()


def get_recipe_by_id(recipe_id):
    recipe_url = "https://strapi.f45training.com/recipes/{}".format(recipe_id)
    result = requests.get(recipe_url)
    return result.json()


def get_challenge_recipes(challenge_id=3):
    url = "https://strapi.f45training.com/meal-plannings?challenge.id={}".format(challenge_id)
    result = requests.get(url)
    return result.json()


@app.route('/api/challenge-recipes', methods=['GET'])
def fetch_challenge_meals():
    challenge_id = request.args.get('id') or 3
    return jsonify(get_challenge_recipes(challenge_id))
