#<server_nosql.py>
#RESTful api with Flask

from flask import Flask, request, abort
from pymongo import MongoClient
from bson.json_util import dumps, default
app = Flask(__name__)
db = MongoClient().nobel_prize

@app.route('/api/winners')

def get_country_data():
    query_dict = {}
    for key in ['country','category','year']:
        arg = request.args.get(key) #e.g.'?country=Australia&category=Chemistry'
        if arg:
            query_dict[key] = arg

    winners = db.winners_clean.find(query_dict)
    if winners:
        return dumps(winners)
    abort(404) #resource not found

if __name__ == '__main__':
    app.run(port=8000, debug=True)

## in Python shell
#import requests
#response = requests.get('http://localhost:8000/api/winners',
#                        params={'country':'Australia','category':'Physics'})

#response.json()
