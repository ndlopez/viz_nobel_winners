# Nobel winners data with Seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import seaborn as sb

plt.rcParams['figure.figsize']=8,4
df = pd.read_json(open('github_repo/nobel_winners_cleaned.json'))
df.date_of_birth = pd.to_datetime(df.date_of_birth)
df.date_of_death = pd.to_datetime(df.date_of_death)
#df.info()
'''
by_gender = df.groupby('gender')
by_gender.size().plot(kind='bar')
plt.show()
by_cat_gen = df.groupby(['category','gender'])
print(by_cat_gen.get_group(('Physics','female'))[['name','year']])

by_cat_gen.size().unstack().plot(kind='barh')
plot.show() -> by_cat_gender.png
cat_gen_sz = by_cat_gen.size().unstack()
cat_gen_sz['total']=cat_gen_sz.sum(axis=1)
cat_gen_sz=cat_gen_sz.sort_values(by='female',ascending=True)
cat_gen_sz[['female','total','male']].plot(kind='barh')
plt.show()
df[(df.category=='Literature') & (df.gender =='female')][['name','country','year']]
#[out]Gabriela Mistral           Chile  1945
#Chemistry  24  Irène Joliot-Curie          France  1935
#Peace 622       Malala Yousafzai         Pakistan  2014
#691          Mother Teresa            India  1979
#698       Rigoberta Menchú        Guatemala  1992

#Winners by gender
new_idx=pd.Index(np.arange(1901,2015),name='year')#fill with Nan the empty gap
by_year_gen=df.groupby(['year','gender'])
year_gen_sz=by_year_gen.size().unstack().reindex(new_idx)
fig,axes=plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True)
ax_f=axes[0]
ax_m=axes[1]
fig.suptitle('Nobel prize winners by gender',fontsize=16)
#Text(0.5, 0.98, 'Nobel prize winners by gender')
ax_f.bar(year_gen_sz.index,year_gen_sz.female)
#<BarContainer object of 114 artists>
ax_f.set_ylabel('Female winners')
#Text(0, 0.5, 'Female winners')
ax_m.bar(year_gen_sz.index,year_gen_sz.male)
#<BarContainer object of 114 artists>
ax_m.set_ylabel('Male winners')
#Text(0, 0.5, 'Male winners')
ax_m.set_xlabel('Year')
#Text(0.5, 0, 'Year')
ax_f.grid(True)
ax_m.grid(True)
plt.show() -> winners_by_gender.png
'''
#winners by country
#df.groupby('country').size().plot(kind='bar',figsize=(10,5))

nat_cat_sz = df.groupby(['country','category']).size().unstack()
#print(nat_cat_sz)
COLS=2
ROWS=3
fig,axes=plt.subplots(ROWS,COLS,figsize=(8,8))
for i, (label,col) in enumerate(nat_cat_sz.iteritems()):
    print(int(i/COLS),i%COLS)
    ax = axes[int(i/COLS),i%COLS]
    col = col.sort_values(ascending=False)[:10]
    col.plot(kind='barh',ax=ax)
    ax.set_title(label)

plt.tight_layout()
plt.show()  -> prize_by_country.png
'''
bins = np.arange(df.year.min(),df.year.max(),10) #decadal bin
by_year_nat_bin = df.groupby([pd.cut(df.year,bins,precision=0),
                              'country']).size().unstack().fillna(0)
plt.figure(figsize=(8,8))
sb.heatmap(by_year_nat_bin[by_year_nat_bin.sum(axis=1) > 2])#more than 2nobels
#must revert the color bar
plt.show()
df['award_age'].hist(bins=20)
sb.histplot(df['award_age'])
#how to plot KDE (kernel density estimation)
plt.show()

* df['age_of_death'] = (df.date_of_death - df.date_of_birth).dt.days/365
** age_at_death = df[df.age_of_death.notnull()].age_of_death
sb.histplot(age_at_death,bins=40) #works! <- age_at_death.png
df2 = df[df.age_of_death.notnull()]
sb.kdeplot(df2[df2.gender == 'male'].age_of_death,shade=True,label='Male')
sb.kdeplot(df2[df2.gender == 'female'].age_of_death,shade=True,label='Female')
plt.legend()
plt.show()  -> life_expect_by_gender.png
add *,**
df_tmp = df[df.age_of_death.notnull()]
dat = pd.DataFrame({'age at death':df_tmp.age_of_death,
                    'date of birth':df_tmp.date_of_birth.dt.year})
sb.lmplot('date of birth','age at death',dat,height=6,aspect=1.5)
plt.show()

df.info()
by_bornin_nat = df[df.born_in.notnull()].groupby( #no born_in object :(
    ['born_in','country']).size().unstack()
by_bornin_nat.index.name = 'Born in'
by_bornin_nat.columns.name = 'Moved to'
plt.figure(figsize=(8,8))
ax = sb.heatmap(by_bornin_nat,vmin=0,vmax=8)
ax.set_title('The nobel diaspora')
plt.show()
'''
