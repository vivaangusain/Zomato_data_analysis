import pandas as pd
import numpy as np
def handlerate(value) :
    if(value== 'NEW' or value=='-'):
        return np.nan
    else:
        value = str(value).split('/')
        value = value [0]
        return float(value)

df=pd.read_csv('zomato.csv')
df3=df.drop(columns=['url','phone','rest_type','dish_liked','reviews_list','menu_item','listed_in(city)'] , axis=1)
df4=df3.rename(columns={'approx_cost(for two people)':'two_people_cost','listed_in(type)':'type_of_restaurant'})
df5=df4.rename(columns={'rate':'rating'})
df5=df5.dropna(subset=['location'])
df5=df5.dropna(subset=['cuisines','two_people_cost'])
df5['two_people_cost']=df5['two_people_cost'].str.replace(',', '').astype(int)
df5['two_people_cost']=df5['two_people_cost']/2
df5=df5.rename(columns={'two_people_cost':'cost_per_person'})
df5['rating'] = df5['rating'].apply(handlerate)
df5['rating']=df5['rating'].fillna(df5['rating'].mean)
df5.to_csv("zomato_data_analysis.csv")