# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'}, inplace = True)
data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data

['Total_Winter'],'Summer','Winter')
data['Better_Event']=np.where(data['Total_Summer']==data['Total_Winter'],'Both',data

['Better_Event'])
print(data['Better_Event'])
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries= data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
# print(len(top_countries))
top_countries.drop(index= len(top_countries)-1, axis=0, inplace=True)
# print(len(top_countries))
def top_ten(top_countries,Col):
    country_list=[]
    top=top_countries.nlargest(10,Col)
    # print(top)
    country_list=list(top['Country_Name'])
    return country_list
top_10_summer=list(top_ten(top_countries,'Total_Summer'))
print(top_10_summer)
top_10_winter=list(top_ten(top_countries,'Total_Winter'))
print(top_10_winter)
top_10= list(top_ten(top_countries,'Total_Medals'))
print(top_10)
common=[x for x in top_10_summer if x in top_10_winter and x in top_10]
print(common)


# --------------
#Code starts here
summer_df=data[data['Country_Name'].isin(top_10_summer)]
# print(summer_df)
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.title('Top 10 Summer')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
plt.show()
winter_df = data[data['Country_Name'].isin(top_10_winter)]
print(winter_df)
plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.title('Top 10 Winter')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
plt.show()
top_df= data[data['Country_Name'].isin(top_10)]
# print(top_10)
plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
plt.title('Top 10')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
# summer_max_ratio=summer_df['Golden_Ratio'].idxmax()
summer_max_ratio=max(summer_df['Golden_Ratio'])
print(summer_max_ratio)
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax

(),'Country_Name']
print(summer_country_gold)
winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
print(winter_max_ratio)
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)
top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
print(top_max_ratio)
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)


# --------------
#Code starts here
data_1=data[:-1]
print(len(data_1))
# Total_Points={'Gold'}
data_1['Total_Points']=data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(best_country)


# --------------
#Code starts here
best = data[data['Country_Name']== best_country]
# print(best)
best= best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medal Tally')
plt.xticks(rotation=45)
plt.show()


