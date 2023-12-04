import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Arizona Housing Price Analysis",
    page_icon=":house_buildings:",
    layout="wide",
)

st.title("Arizona Housing Price Analysis")
data_path = 'streamlit_tutorial/housing_data_with_lat_long.parquet'

@st.cache_data(persist=True)
def load_data():
    data = pd.read_parquet(data_path,columns= ['zip','period_begin','period_end','county','median_sale_price', 'homes_sold', 'inventory','irs_estimated_population','longitude','latitude'])
    data = data.dropna()
    data['period_begin'] = pd.to_datetime(data['period_begin'])
    data['period_end'] = pd.to_datetime(data['period_end'])
    int_columns = ['median_sale_price', 'homes_sold', 'inventory', 'irs_estimated_population']
    data[int_columns] = data[int_columns].astype(float)
    return data

df = load_data()

st.sidebar.subheader("")



# Sidebar for user input
st.sidebar.header("Filters")
select_by = st.sidebar.selectbox("Select Location filter:",['County','Zip'])

if select_by == 'County':
    selected_counties = st.sidebar.multiselect("Select Counties:", df['county'].unique(),default=['Pima County'])
    filtered_data = df[df['county'].isin(selected_counties)]
elif select_by =='Zip':
    selected_zip = st.sidebar.multiselect("Select Zip Code:", df['zip'].unique(),default=[85719])
    filtered_data = df[df['zip'].isin(selected_zip)]
from datetime import datetime
# Filter data based on user input
unique_periods = sorted(filtered_data['period_begin'].dt.strftime('%Y-%m-%d').unique(),reverse=True)
period_start = datetime.strptime(st.sidebar.selectbox("Select end year:", unique_periods[1:]),'%Y-%m-%d')
period_end = datetime.strptime(st.sidebar.selectbox("Select start year :", unique_periods),'%Y-%m-%d')
filtered_data = filtered_data.loc[(filtered_data['period_begin'] >= period_start)  & (filtered_data['period_begin'] <= period_end) ]

kpi1, kpi2, kpi3 = st.columns(3)

avg_price  = np.mean(filtered_data['median_sale_price'])
avg_home_sold  = np.sum(filtered_data['homes_sold'])
avg_inventory_size  = np.sum(filtered_data['inventory'])
kpi1.metric(
    label="Average Median Sale Price ＄",
    value=round(avg_price),
)

kpi2.metric(
    label="Total Homes Sold ",
    value=round(avg_home_sold),
)

kpi3.metric(label= "Average Inventory Size",     value=round(avg_inventory_size))


fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.markdown("### First Chart")
    fig = px.density_heatmap(
        data_frame=filtered_data, y="inventory", x="median_sale_price"
    )
    st.write(fig)
   
with fig_col2:
    st.markdown("### Second Chart")
    fig2 = px.histogram(data_frame=filtered_data, x="median_sale_price")
    st.write(fig2)


st.subheader('Map')
st.map(filtered_data[['latitude', 'longitude']])

# Display filtered data
st.subheader('Filtered Data')
st.write(filtered_data)

