import streamlit as st
import datetime as dt
import requests as re
'''
# TaxiFareModel front
'''
date = st.date_input('Enter a date: ', value = dt.datetime(2014,7,6,19,18,0))
time = st.time_input('Insert time: ', value = dt.datetime(2014,7,6,19,18,0))
pickup_longitude = st.number_input('Insert pickup longitude', value = -73.950655)
pickup_latitude = st.number_input('Insert pickup latitude', value = 40.783282)
dropoff_longitude = st.number_input('Insert dropoff longitude', value = -73.984365)
dropoff_latitude = st.number_input('Insert dropoff latitude', value = 40.769802)
passenger_count = st.number_input('Insert number of passengers', value = 2)

dictionary = {
        'pickup_datetime': f'{date} {time}',
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
        }



'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'
button = st.button('Predict price')

if button is True:
    api = re.get(url=url, params=dictionary).json()
    st.write(api['fare'])

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
