
# coding: utf-8

# In[4]:


import pandas as pd
airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")
routes = pd.read_csv("routes.csv")
print(airlines.iloc[0])
print(airports.iloc[0])
print(routes.iloc[0])


# A map projection transforms points on a sphere to a two-dimensional plane. When projecting down to the two-dimensional plane, some properties are distorted. Each map projection makes trade-offs in what properties to preserve and you can read about the different trade-offs here. We'll use the Mercator projection, because it is commonly used by popular mapping software.

# In[5]:


from mpl_toolkits.basemap import Basemap


# In[19]:


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
get_ipython().run_line_magic('matplotlib', 'inline')
m = Basemap(projection= "merc",llcrnrlat= -80,urcrnrlat = 80,llcrnrlon = -180,urcrnrlon = 180)


# created a Basemap instance here

# In[20]:



long_list = airports["longitude"].tolist()
lat_list = airports["latitude"].tolist()
x , y = m(long_list,lat_list)


# In[21]:


print(x[0:5])
print(y[0:5])


# In[22]:


m.scatter(x,y,s=1)
plt.show()


# In[23]:


fig , ax = plt.subplots(figsize = (20,15))
ax.set_title("Scaled Up Earth With Coastlines")                  
map_1 = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = map_1(longitudes, latitudes)
map_1.scatter(x, y, s=1)
map_1.drawcoastlines()
plt.show()


# used fig, ax cration by plt.subplots to mentione figsize and axes.set_title() to set map title

# In[24]:


geo_routes = pd.read_csv("geo_routes.csv")


# In[25]:


geo_routes.info()


# In[26]:


geo_routes.head()


# In[27]:


fig, ax = plt.subplots(figsize=(15,20))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
def create_great_circles(input_df):
    for index, row in input_df.iterrows():
        if (abs(row["end_lat"]-row["start_lat"]) < 180) and (abs(row["end_lon"]-row["start_lon"]) < 180) :
            m.drawgreatcircle(row["start_lon"],row["start_lat"],row["end_lon"],row["end_lat"])
dfw = geo_routes[geo_routes["source"] == "DFW"]        

create_great_circles(dfw)
plt.show()


# Shows routes from airport code = DFW using basemap.drawgreatcircles()
