
import pandas as pd
import random



df = df = pd.DataFrame( columns=['id','name','rating', 'content', 'org_id'])
number = 59
user = ['doyltcoven', 'wateryfisher','likablerookery','favorableprofit','assistgigantic','thereforeshowy',
        'southeasterlypolenta', 'originfortress', 'penitentsuper', 'stronglyabashed', 'pufferfishresemble',
        'lamentableservice', 'upstagefrowning', 'upstagefrowning', 'flinkreceptive', 'jelliedjackstaff',
        'dextrousevolution', 'clubambiguous', 'pouchsteadfast','denoccasionally','breakfastsun']
comment  = ['good','bad','decent',' could not even imagine this exists', 'like, wow', 'eh', 'eggcelent','wtf']
for i in range(0, number):

    ind = i+1
    name=user[random.randint(0,len(user)-1)]
    rate= random.randint(0,5)
    content = comment[random.randint(0,len(comment)-1)]
    org = random.randint(1,5)
    df.loc[len(df.index)]=[ind, name, rate,content, org]



df.set_index("id", inplace = True)
df.to_csv("Reviews.csv")
