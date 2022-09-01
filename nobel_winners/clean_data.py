#Cleaning the nobel_winners json object
import numpy as np
import pandas as pd
from pymongo import MongoClient

client = MongoClient()
DB_NOBEL_PRIZE='nobel_prize'
COLL_WINNERS='winners'
db= client[DB_NOBEL_PRIZE]
coll = db[COLL_WINNERS]

def get_mongo_database(db_name,host='localhost',port=27017,username=None,
                       password=None):
    #get named database from MongoDB w/o auth
    if username and password:
        mongo_uri = 'mongodb://%s@%s/%s'%(username,password,host,db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host,port)
    return conn[db_name]


cursor = db.winners.find()
df = pd.DataFrame(list(cursor))


df = pd.read_json(open('data/nobel_winners_full.json'))


def mongo_to_dataframe(db_name,collection,query={}, host='localhost',
                       port=27017, username=None, password=None,no_id=True):
    #create a dataframe from mongodb collection
    db = get_mongo_database(db_name,host,port,username,password)
    cursor = db[collection].find(query)
    df = pd.DataFrame(list(cursor))

    if no_id:
        del df['_id']
    return df

def dataframe_to_mongo(df,db_name,collection,host='localhost',port=27017,
                       username=None,password=None):
    #save a dataframe to mongodb collection
    db = get_mongo_database(db_name,host,port,username,password)

    records = df.to_dict('records')
    db[collection].insert_many(records)

def clean_data(df):
    df = df.replace('',np.nan)
    df_born_in = df[df.born_in.notnull()]
    df = df[df.born_in.isnull()]
    df = df.drop('born_in',axis=1)
    df.drop(df[df.year==1809].index,inplace=True)
    df = df[~(df.name == 'Marie Curie')]
    df.loc[(df.name == 'Marie Sk\u0142odowska-Curie') &(df.year == 1911),
           'country']= 'France'
    df = df[~((df.name == 'Sidney Altman') & (df.year == 1990))]
    df = df.reindex(np.random.permutation(df.index))
    df = df.drop_duplicates(['name','year'])
    df = df.sort_index()
    df.loc[df.name == 'Alexis Carrel', 'category']='Physiology or Medicine'
    df.loc[df.name == 'Ragnar Granit', 'gender']= 'male'
    df = df[df.gender.notnull()]
    df.loc[df.name == 'Hiroshi Amano', 'date_of_birth']='11 September 1960'
    df.date_of_birth = pd.to_datetime(df.date_of_birth)
    df.date_of_death = pd.to_datetime(df.date_of_death,errors='coerce')
    df['award_age']=df.year - pd.DatetimeIndex(df.date_of_birth).year
    return df, df_born_in

df_clean, df_born_in = clean_data(df)
dataframe_to_mongo(df_clean,'nobel_prize','winners')
dataframe_to_mongo(df_born_in,'nobel_prize','winners_born_in')

#df = mongo_to_dataframe('nobel_prize','winners')

#import sqlalchemy
#engine =sqlalchemy.create_engine('sqlite:///data/nobel_prize.db')
#df_clean.to_sql('winners',engine)
