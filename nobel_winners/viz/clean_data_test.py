#Run from the Python interpreter
df = pd.read_json(open('data/nobel_winners_dirty.json'))
#install pymongo before running...
df = mongo2dataframe('nobel_prize','winners')

print(df.info())
#data will be indexed by name
df = df.set_index('name') #,inplace=True)
df.reset_index(inplace=True)
bi_col= df.born_in
type(by_col)

df.iloc[0]
df.loc['Albert Einstein']

#description of data
df.born_in.describe()
set(df.born_in.apply(type))
import numpy as np
#replace empty string with Numpy's Nan
bi_col.replace('',np.nan,inplace=True)
bi_col.count()
#Replace all empty strings with Nan
df.replace('',np.nan,inplace=True)

df.reset_index(inplace=True)
#list names with an *
df[df.name.str.contains('\*')]['name']
#Replace * with empty space
df.name = df.name.str.replace('*','')
#strip white-space from the names
df.name = df.name.str.strip()
#Check if null data exist
df = df[df.born_in.isnull()]
df.count()
#born_in col is already cleaned, then
df = df.drop('born_in',axis=1)
#find duplicates
dupes_by_name = df[df.duplicated('name')]
dupes_by_name.count()
#list all duplicated
all_dupes = df[df.duplicated('name') | df.duplicated('name',keep='last')]
all_dupes.count()
#or similarly
all_dupes = df[df.name.isin(dupes_by_name.name)]
all_dupes.count()
#or using groupby function
for name,rows in df.groupby('name'):
    print('name: %s, number of rows: %d'%(name,len(rows)))

#List all dupls
pd.concat([g for _,g in df.groupby('name') if len(g) > 1])['name']

#all dupls listed
all_dupes.sort_values('name')[['name','country','year']]
'''
                 name         country  year
121        Aaron Klug    South Africa  1982
131        Aaron Klug  United Kingdom  1982
844   Albert Einstein         Germany  1921
615   Albert Einstein     Switzerland  1921
176     Arieh Warshel   United States  2013
..                ...             ...   ...
294     Tsung-Dao Lee   United States  1957
333  Wassily Leontief   United States  1973
684  Wassily Leontief          Russia  1973
773    Yoichiro Nambu           Japan  2008
489    Yoichiro Nambu   United States  2008
'''
#Replacing country for Marie Curie
df.loc[(df.name == 'Marie Sk\u0142odowska-Curie') & (df.year==1911),'country']='France'
#Removing cleaned row
df.drop(df[(df.name == 'Sidney Altman') & (df.year ==1990)].index,inplace=True)
#another way...
df =df[~((df.name == 'Sidney Altman') & (df.year == 1990))]
#Clean data...
def clean_data(df):
    df = df.replace('',np.nan)
    df = df[df.born_in.isnull()]
    df = df.drop('born_in',axis=1)
    df.drop(df[df.year ==1809].index,inplace=True)
    df = df[~(df.name == 'Marie Curie')]
    df.loc[(df.name == 'Marie Sk\u0142odowska-Curie') & (df.year == 1911),'country']='France'
    df = df.[~((df.name == 'Sidney Altman') & (df.year == 1990))]
    return df

df = df.reindex(np.random.permutation(df.index))
df = df.drop_duplicates(['name','year'])
df = df.sort_index()
df.count()
''' [out]
name              870
category          869
country           870
date_of_birth     862
date_of_death     571
gender            861
link              870
place_of_birth    836
place_of_death    529
text              870
year              870
dtype: int64
'''
df[df.duplicated('name') | df.duplicated('name',keep='last')].sort_values(by='name')[['name','country','year','category']]
'''
                       name         country  year                category
548        Frederick Sanger  United Kingdom  1958               Chemistry
580        Frederick Sanger  United Kingdom  1980               Chemistry
292            John Bardeen   United States  1956                 Physics
326            John Bardeen   United States  1972                 Physics
285        Linus C. Pauling   United States  1954               Chemistry
309        Linus C. Pauling   United States  1962                   Peace
910             Marie Curie          France  1903                 Physics
919             Marie Curie          France  1911               Chemistry
706  Marie Skłodowska-Curie          Poland  1903                 Physics
709  Marie Skłodowska-Curie          France  1911               Chemistry
650           Ragnar Granit          Sweden  1967  Physiology or Medicine
960           Ragnar Granit         Finland  1809  Physiology or Medicine
'''

