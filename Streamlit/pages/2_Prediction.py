import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import joblib
from datetime import datetime
from sklearn.preprocessing import StandardScaler,LabelEncoder

st.set_page_config(
    page_title="Arizona Housing Price Prediction",
    page_icon=":house_buildings:",
    layout="wide",
)

st.title("Arizona Housing Price Prediction")
data_path = 'streamlit_tutorial/housing_data_with_lat_long.parquet'
st.session_state['button_clicked'] = False


@st.cache_data(persist=True)
def load_data():
    data = pd.read_parquet(data_path)
    drop_cols = ['region','state_x','latitude','longitude','parent_metro_region','state_y','price_drops','price_drops_yoy','pending_sales_yoy','off_market_in_two_weeks_yoy']
    data = data.drop(columns=drop_cols)
    data = data.dropna()
    data['period_begin'] = pd.to_datetime(data['period_begin'])
    data['period_end'] = pd.to_datetime(data['period_end'])
    int_columns = ['median_sale_price', 'homes_sold', 'inventory', 'irs_estimated_population']
    data[int_columns] = data[int_columns].astype(float)
    return data

df = load_data()

# @st.cache_data(persist=True)
def load_model():
    md = joblib.load('streamlit_tutorial/prediction_model_tuned.joblib')
    return md

prediction_model = load_model()
# prd=md.predict(X_test_scaled)
# mse = mean_squared_error(y_test, prd)
# print(f'Mean Squared Error: {mse}')

st.sidebar.subheader("")

def callback():
    st.session_state['button_clicked'] = False

# Sidebar for user input
st.sidebar.header("Filters")

select_by = st.sidebar.selectbox("Select Location filter:",['County','Zip','City'])
if select_by == 'County':
    selected_counties = st.sidebar.multiselect("Select Counties:", df['county'].unique(),default=['Pima County'],on_change= callback)
    filtered_data = df[df['county'].isin(selected_counties)]
elif select_by =='Zip':
    selected_zip = st.sidebar.multiselect("Select Zip Code:", df['zip'].unique(),default=[85719],on_change= callback)
    filtered_data = df[df['zip'].isin(selected_zip)]
elif select_by =='City':
    selected_cities = st.sidebar.multiselect("Select City:", df['primary_city'].unique(),default=['Tucson'],on_change= callback)
    filtered_data = df[df['primary_city'].isin(selected_cities)]

selected_property_types = st.multiselect('Choose Property Type',options= df['property_type'].unique(),default=['Single Family Residential'],on_change= callback)
filtered_data = filtered_data[filtered_data['property_type'].isin(selected_property_types)]

submit_button = st.button("Submit")
st.session_state['button_clicked'] = submit_button
if submit_button:
    today_date = datetime.now()
    today_year = today_date.year
    today_month = today_date.month
    filtered_data = filtered_data.sort_values(by='period_end', ascending=False)
    group_columns = ['zip', 'county', 'primary_city', 'property_type']
    latest_rows = filtered_data.groupby(group_columns).first().reset_index()
    latest_rows['period_year'] = today_year
    latest_rows['period_month'] = today_month

    # Assuming your dataframe is named 'df'

    # Select relevant features and target variable
    features = ['zip','county','primary_city','period_year','period_month','property_type', 'median_list_price', 'median_sale_price_yoy', 'median_list_price_yoy',
                'median_ppsf', 'median_ppsf_yoy', 'median_list_ppsf', 'median_list_ppsf_yoy',
                'homes_sold', 'homes_sold_yoy', 'pending_sales', 'new_listings', 'new_listings_yoy',
                'inventory', 'inventory_yoy', 'median_dom', 'median_dom_yoy', 'avg_sale_to_list',
                'avg_sale_to_list_yoy', 'sold_above_list', 'sold_above_list_yoy',
                'off_market_in_two_weeks', 'irs_estimated_population']

    numeric_features = ['median_list_price', 'median_sale_price_yoy', 'median_list_price_yoy',
                'median_ppsf', 'median_ppsf_yoy', 'median_list_ppsf', 'median_list_ppsf_yoy',
                'homes_sold', 'homes_sold_yoy', 'pending_sales', 'new_listings', 'new_listings_yoy',
                'inventory', 'inventory_yoy', 'median_dom', 'median_dom_yoy', 'avg_sale_to_list',
                'avg_sale_to_list_yoy', 'sold_above_list', 'sold_above_list_yoy',
                'off_market_in_two_weeks', 'irs_estimated_population']
    string_cols = ['zip','county','primary_city','property_type']
    latest_rows_pred = latest_rows[features].copy()
    label_encoder = LabelEncoder()
    for col in string_cols:
    # Apply LabelEncoder to the 'property_type' column
        latest_rows_pred[col] = label_encoder.fit_transform(latest_rows_pred[col])


    # Standardize numerical features
    scaler = StandardScaler()
    scaled_features  = latest_rows_pred.copy()
    scaled_features[numeric_features] = scaler.fit_transform(latest_rows_pred[numeric_features])
    predictions = prediction_model.predict(scaled_features)

    latest_rows['predicted_price'] = predictions
    latest_rows = latest_rows[['zip','county','primary_city','property_type','predicted_price']]
    st.subheader('predicted Data')
    st.write(latest_rows)


