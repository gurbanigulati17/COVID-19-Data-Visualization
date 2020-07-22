#!/usr/bin/env python
# coding: utf-8

# In[190]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']=17,8
import plotly as p
import plotly.express as px
import plotly.graph_objects as go

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot
#plt.rcParams['figure.figsize']=25,12
import folium




# In[191]:


pyo.init_notebook_mode(connected=True)
cf.go_offline()






# In[ ]:


df=pd.read_excel(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\Covid cases in India.xlsx")


# In[86]:


df


# In[10]:


df.drop(['S. No.'],axis=1,inplace=True)  #Drop the column S.No.


# In[87]:


df                                      #Display Data frame


# In[95]:


df['Total Cases']=df['Total Confirmed cases (Indian National)']+df['Total Confirmed cases ( Foreign National )']



# In[96]:



df


# In[97]:


total_cases_overall=df['Total Cases'].sum()
print("The total number of cases till now in India is ",total_cases_overall)


# In[98]:


df['Active Cases']=df['Total Cases']-(df['Death']+df['Cured'])


# In[35]:


df


# In[149]:


df.style.background_gradient(cmap='Reds')


# In[100]:


Total_Active_Cases=df.groupby('Name of State / UT')['Active Cases'].sum().sort_values(ascending=False).to_frame()


# In[51]:


Total_Active_Cases


# In[102]:


Total_Active_Cases.style.background_gradient(cmap='Reds')


# In[ ]:


#Graphical Representation.......................................


# In[192]:


#pandas lib
df.plot(kind='bar',x='Name of State / UT',y='Total Cases')
plt.show()
df.iplot(kind='bar',x='Name of State / UT',y='Total Cases')




# In[193]:


#matplotlib vis

plt.bar(df['Name of State / UT'],df['Total Cases'])


# In[1]:


px.bar(df,x='Name of State / UT',y='Total Cases')


# In[2]:


df.plot(kind='scatter',x='Name of State / UT',y='Total Cases')


# In[196]:


plt.scatter(df['Name of State / UT'],df['Total Cases'])



# In[175]:


df.iplot(kind='scatter',x='Name of State / UT',y='Total Cases',mode='markers+lines',title='My Graph',xTitle='Name of State / UT',yTitle='Total Cases',colors='red',size=20)



# In[176]:


px.scatter(df,x='Name of State / UT',y='Total Cases')


# In[198]:


#Matplotlib 
fig=plt.figure(figsize=(20,10))
axes=fig.add_axes([0,0,1,1])
axes.bar(df['Name of State / UT'],df['Total Cases'])
axes.set_title('Total Cases in India')
axes.set_xlabel('Name of State / UT')
axes.set_ylabel('Total Cases')
plt.show()

#plotly
fig=go.Figure()
fig.add_trace(go.Bar(x=df['Name of State / UT'],y=df['Total Cases']))
fig.update_layout(title='Total Cases in India',xaxis=dict(title='Name of State / UT'),yaxis=dict(title='Total Cases'))


# In[207]:


Indian_Cord=pd.read_excel(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\Indian Coordinates.xlsx")


# In[208]:


Indian_Cord


# In[209]:


df_full=pd.merge(Indian_Cord,df,on='Name of State / UT')


# In[210]:


df_full


# In[217]:


map=folium.Map(location=[20,70],zoom_start=4,tiles='Stamenterrain')
for lat,long,value, name in zip(df_full['Latitude'],df_full['Longitude'],df_full['Total Cases'],df_full['Name of State / UT']):
    folium.CircleMarker([lat,long],radius=value*0.8,popup=('<strong>State</strong>: '+str(name).capitalize()+'<br>''<strong>Total Cases</strong>: '+str(value)+'<br>'),color='red',fill_color='red',fill_opacity=0.3).add_to(map)
                        


# In[218]:


map


# In[ ]:


#How Corona virus is rising globally


# In[232]:


dbd_India=pd.read_excel(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\per_day_cases.xlsx",parse_dates=True,sheet_name="India")
dbd_Italy=pd.read_excel(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\per_day_cases.xlsx",parse_dates=True,sheet_name="Italy")
dbd_Korea=pd.read_excel(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\per_day_cases.xlsx",parse_dates=True,sheet_name="Korea")
dbd_Wuhan=pd.read_excel(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\per_day_cases.xlsx",parse_dates=True,sheet_name="Wuhan")


# In[223]:


dbd_India


# In[229]:


#matlplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(dbd_India["Date"],dbd_India["Total Cases"],color='blue')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()


#plotly Express
fig=px.bar(dbd_India,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()


# In[233]:


#plotly Express
fig=px.bar(dbd_Italy,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Italy')
fig.show()

#plotly Express
fig=px.bar(dbd_Korea,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Korea')
fig.show()

#plotly Express
fig=px.bar(dbd_Wuhan,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Wuhan')
fig.show()


# In[ ]:


#Scatter Plotting............................


# In[241]:


#MatplotLib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(dbd_India["Date"],dbd_India["Total Cases"],color='brown',marker="*")
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()

fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(dbd_India["Date"],dbd_India["Total Cases"],color='blue',marker='*')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()

#plotly Express
fig=px.scatter(dbd_India,x="Date",y="Total Cases",color="Total Cases",title='Confirmed Cases in India')
fig.show()


# In[ ]:


#Plotly ..............................


# In[242]:


#Plotly

dbd_India.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers')


# In[243]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=dbd_India['Date'],y=dbd_India['Total Cases'],mode='lines+markers'))


# In[244]:


#MatplotLib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(dbd_Italy["Date"],dbd_Italy["Total Cases"],color='brown',marker="*")
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Italy")
plt.show()

fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(dbd_Italy["Date"],dbd_Italy["Total Cases"],color='blue',marker='*')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Italy")
plt.show()

#plotly Express
fig=px.scatter(dbd_Italy,x="Date",y="Total Cases",color="Total Cases",title='Confirmed Cases in Italy')
fig.show()


# In[245]:


#MatplotLib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(dbd_Korea["Date"],dbd_Korea["Total Cases"],color='brown',marker="*")
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Korea")
plt.show()

fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(dbd_Korea["Date"],dbd_Korea["Total Cases"],color='blue',marker='*')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Korea")
plt.show()

#plotly Express
fig=px.scatter(dbd_Korea,x="Date",y="Total Cases",color="Total Cases",title='Confirmed Cases in Korea')
fig.show()


# In[246]:


#MatplotLib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(dbd_Wuhan["Date"],dbd_Wuhan["Total Cases"],color='brown',marker="*")
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Wuhan")
plt.show()

fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(dbd_Wuhan["Date"],dbd_Wuhan["Total Cases"],color='blue',marker='*')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Wuhan")
plt.show()

#plotly Express
fig=px.scatter(dbd_Wuhan,x="Date",y="Total Cases",color="Total Cases",title='Confirmed Cases in Wuhan')
fig.show()


# In[249]:


#Subplots......................................
from plotly.subplots import make_subplots


# In[269]:


fig=make_subplots(
    rows=2,cols=2,specs=[[{"secondary_y":True},{"secondary_y":True}],[{"secondary_y":True},{"secondary_y":True}]],
    subplot_titles=("S.Korea","Italy","India","Wuhan"))
fig.add_trace(go.Bar(x=dbd_Korea['Date'],y=dbd_Korea['Total Cases'],marker=dict(color=dbd_Korea['Total Cases'],coloraxis="coloraxis")),1,1)
fig.add_trace(go.Bar(x=dbd_Italy['Date'],y=dbd_Korea['Total Cases'],marker=dict(color=dbd_Italy['Total Cases'],coloraxis="coloraxis")),1,2)
fig.add_trace(go.Bar(x=dbd_India['Date'],y=dbd_Korea['Total Cases'],marker=dict(color=dbd_India['Total Cases'],coloraxis="coloraxis")),2,1)
fig.add_trace(go.Bar(x=dbd_Wuhan['Date'],y=dbd_Wuhan['Total Cases'],marker=dict(color=dbd_Wuhan['Total Cases'],coloraxis="coloraxis")),2,2)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'),showlegend=False,title_text="Total Cases in 4 Countries")

fig.update_layout(plot_bgcolor='rgb(230,230,230)')


# In[270]:


fig=make_subplots(
    rows=2,cols=2,specs=[[{"secondary_y":True},{"secondary_y":True}],[{"secondary_y":True},{"secondary_y":True}]],
    subplot_titles=("S.Korea","Italy","India","Wuhan"))
fig.add_trace(go.Scatter(x=dbd_Korea['Date'],y=dbd_Korea['Total Cases'],marker=dict(color=dbd_Korea['Total Cases'],coloraxis="coloraxis")),1,1)
fig.add_trace(go.Scatter(x=dbd_Italy['Date'],y=dbd_Korea['Total Cases'],marker=dict(color=dbd_Italy['Total Cases'],coloraxis="coloraxis")),1,2)
fig.add_trace(go.Scatter(x=dbd_India['Date'],y=dbd_Korea['Total Cases'],marker=dict(color=dbd_India['Total Cases'],coloraxis="coloraxis")),2,1)
fig.add_trace(go.Scatter(x=dbd_Wuhan['Date'],y=dbd_Wuhan['Total Cases'],marker=dict(color=dbd_Wuhan['Total Cases'],coloraxis="coloraxis")),2,2)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'),showlegend=False,title_text="Total Cases in 4 Countries")

fig.update_layout(plot_bgcolor='rgb(230,230,230)')


# In[ ]:


#World Coronavirus............................


# In[354]:


df=pd.read_csv(r'C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\covid_19_data.csv',parse_dates=['Last Update'])


# In[355]:


df.rename(columns={'ObservationDate':'Date','Country/Region':'Country'},inplace=True)

df

        


# In[293]:


df.groupby('Date').sum()


# In[294]:


confirmed=df.groupby('Date').sum()['Confirmed']


# In[295]:


confirmed


# In[307]:


confirmed=df.groupby('Date').sum()['Confirmed'].reset_index()
death=df.groupby('Date').sum()['Deaths'].reset_index()
rec=df.groupby('Date').sum()['Recovered'].reset_index()


# In[308]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'],mode='lines+markers',name='Confirmed',line=dict(color='blue',width=2)))
fig.add_trace(go.Scatter(x=death['Date'],y=death['Deaths'],mode='lines+markers',name='Deaths',line=dict(color='red',width=2)))
fig.add_trace(go.Scatter(x=rec['Date'],y=rec['Recovered'],mode='lines+markers',name='Recovered',line=dict(color='green',width=2)))


# In[356]:


df


# In[358]:


df_confirmed=pd.read_csv(r"C:\Users\geetg\Downloads\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\COVID-19-Time-Series-Forecasting-with-Data-Analysis-master\time_series_covid_19_confirmed.csv")


# In[360]:


df_confirmed.rename(columns={'Country/Region':'Country'},inplace=True)
df_confirmed


# In[361]:


df


# In[362]:


df_latlong=pd.merge(df,df_confirmed,on=['Country','Province/State'])
df_latlong


# In[363]:


fig=px.density_mapbox(df_latlong,lat="Lat",lon="Long",hover_name="Province/State",hover_data=["Confirmed","Deaths","Recovered"],animation_frame="Date",color_continuous_scale="Portland",radius=7,zoom=0,height=700)
fig.update_layout(title="Worldwide Coroa  Virus Cases")
fig.update_layout(mapbox_style="open-street-map",mapbox_center_lon=0)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# In[ ]:




