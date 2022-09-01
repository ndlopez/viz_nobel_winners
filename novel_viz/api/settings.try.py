#api/settings.py
#optional MONGO vars
#MONGO_HOST='localhost'
#MONGO_PORT=27017
#MONGO_USERNAME='user'
#MONGO_PASSWORD='user'

URL_PREFIX = 'api'
MONGO_DBNAME = 'nobel_prize'
DOMAIN = {'winners':{
    'schema':{
        'country':{'type':'string'},
        'category':{'type':'string'},
        'name':{'type':'string'},
        'year':{'type':'integer'},
        'gender':{'type':'string'}}
    }}
