import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
#from sqlalchemy import create_engine
#import matplotlib.pyplot as plt
#import vaex

st.set_page_config(page_title='Air Quality Dashboard', page_icon=':alien:', layout='wide')


#header
with st.container():
    #st.subheader('This is my dashboard for displaying interactive plots.')
    st.title('United States Air Quality :us:')
    st.write('To check out all the project code and collection methods please see my [Github](https://github.com/swedes5) page.')
    st.write('Here is a small peek at the full amount of data collected from the EPA. A small disclaimer is that some states and many counties in each state'
            + ' did not have data from the past five years for these pollutants or in some cases I could not obtain the data. ')

#required installs are: streamlit==1.11.0, plotly, pandas, Pillow, pandas,
#load the data
@st.cache
def load_benzene_data(nrows):
    benzene_data = pd.read_csv('benzene copy.csv', nrows=nrows)
    benzene_data['date_local'] = pd.to_datetime(benzene_data['date_local'], infer_datetime_format=True)
    benzene_data['sample_measurement'] = benzene_data['sample_measurement'].astype(float)
    return benzene_data

@st.cache
def load_co_data(nrows):
    co_data = pd.read_csv('carbon_monoxide copy.csv', nrows=nrows)
    co_data['date_local'] = pd.to_datetime(co_data['date_local'], infer_datetime_format=True)
    co_data['sample_measurement'] = co_data['sample_measurement'].astype(float)
    return co_data

@st.cache
def load_no2_data(nrows):
    no2_data = pd.read_csv('nitrogen_dioxide copy.csv', nrows=nrows)
    no2_data['date_local'] = pd.to_datetime(no2_data['date_local'], infer_datetime_format=True)
    no2_data['sample_measurement'] = no2_data['sample_measurement'].astype(float)
    return no2_data

@st.cache
def load_so2_data(nrows):
    so2_data = pd.read_csv('sulfer_dioxide copy.csv', nrows=nrows)
    so2_data['date_local'] = pd.to_datetime(so2_data['date_local'], infer_datetime_format=True)
    so2_data['sample_measurement'] = so2_data['sample_measurement'].astype(float)
    return so2_data

#checking if worked
#data_load_state = st.text('loading data...')

benzene_data = load_benzene_data(670611) #loading all the rows
co_data = load_co_data(9588069)
no2_data = load_no2_data(10708423)
so2_data = load_so2_data(4180127)

#data_load_state.text('loading data is done')

st.subheader('Raw data')
st.write(benzene_data.head())

col1, col2 = st.columns((1,1))

#plotting bar charts and descriptions for benzene
with col1:
    st.subheader('Amount of Benzene per state:')
    benzene_avgs = benzene_data.groupby(['state']).mean().sort_values(by=['sample_measurement'], ascending=False)
    benzene_fig = px.bar(benzene_avgs, labels={'state':'State','value':'Benzene per Billion'} ,title='State Average Benzene Air Quality')
    st.plotly_chart(benzene_fig)

with col2:
    st.write('Benzene is an air pollutant that typically is found indoors where objects like glue, paint, wood-working wax, and detergents exist.'
            + ' Some considerations to take note of regarding Benzene are that high levels of the pollutant can cause symptoms like:')
    st.write('- Headaches')
    st.write('- Dizziness')
    st.write('- Eye, Skin, Respiratory Irritation')
    st.write('- Unconsciousness')
    st.write('Safe levels of Benzene are at or below 1 part per million or 1000 parts per billion.  While this is a common air pollutant, it seems that dangerous levels'
            + ' probably only occur at specific job sites or inside near cleaning or finishing products.')

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

#plotting bar charts and descriptions for carbon monoxide
with col1:
    st.subheader('Amount of Carbon Monoxide per state:')
    co_avgs = co_data.groupby(['state']).mean().sort_values(by=['sample_measurement'], ascending=False)
    co_fig = px.bar(co_avgs, labels={'state':'State','value':'Carbon Monoxide per Million'} ,title='State Average Carbon Monoxide Air Quality')
    st.plotly_chart(co_fig)

with col2:
    st.write('Carbon Monixide is a colorless, odorless gas that is a common air pollutant. It is product of smoke and exhaust fumes that contain the gas.'
            + ' Some considerations to take note of regarding Carbon Monoxide are that high levels of the gas can cause symptoms like:')
    st.write('- Headaches')
    st.write('- Dizziness')
    st.write('- Nausea')
    st.write('- Death')
    st.write('Safe levels of Carbon Monixide are at or below exposure to 50 parts per million every eight hours.  While this is a common air pollutant, it seems that dangerous levels'
            + ' probably only occur at specific job sites with many vehicles or other concentration points.')
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

#plotting bar charts and descriptions for nitrogen_dioxide
with col1:
    st.subheader('Amount of Nitrogen Dioxide per state:')
    no2_avgs = no2_data.groupby(['state']).mean().sort_values(by=['sample_measurement'], ascending=False)
    no2_fig = px.bar(no2_avgs, labels={'state':'State','value':'Nitrogen Dioxide per Billion'} ,title='State Average Nitrogen Dioxide Air Quality')
    st.plotly_chart(no2_fig)

with col2:
    st.write('Nitrogen Dioxide is a reddish-brown gaseous air pollutant. It forms when fossil fuels like coal, oil, gasoline or diesel are burned at high temperatures.'
            + 'Some considerations to take note of regarding Nitrogen Dioxide are that high levels of the gas can cause enviornmental problems such as:')
    st.write('- Damaging trees/foliage')
    st.write('- Decreasing crop yields')
    st.write('- One pound of Nitrogen Dioxide affects global warming at 300x effectiveness compared to one pound of Carbon Dioxide ')
    st.write('Safe levels of Nitrogen Dioxide are at or below exposure to 1 part per million at any time and 3 parts per million over the course of eight hours.'
            + ' High levels of this pollutant can be found near busy roads/highways, power plants, and other industrial plants.')
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

#plotting bar charts and descriptions for sulfur dioxide
with col1:
    st.subheader('Amount of Sulfur Dioxide per state:')
    so2_avgs = so2_data.groupby(['state']).mean().sort_values(by=['sample_measurement'], ascending=False)
    so2_fig = px.bar(so2_avgs, labels={'state':'State','value':'Sulfur Dioxide per Billion'} ,title='State Average Sulfur Dioxide Air Quality')
    st.plotly_chart(so2_fig)

with col2:
    st.write('Sulfur Dioxide is a colorless, strong odored, reactive, gaseous air pollutant. Its sources are mainly fossil fuel combustion and natural volcanic activity.'
            + 'Some considerations to take note of regarding Sulfur Dioxide are that high levels of the gas can cause enviornmental and health problems such as:')
    st.write('- Eye/Nose/Throat/Lung Irritation')
    st.write('- A main component of Sulferic Acid, which is itself a main component of acid rain')
    st.write('- Acid rain can cause deforestation, harm aquatic life, and corrode buildings and structures')
    st.write('Safe levels of Sulfur Dioxide are at or below exposure to 1 part per million.'
            + ' High levels of this pollutant can be found near active volcanoes, which may explain the large levels in Alaska [which has over 130 active volcanoes](https://www.usgs.gov/faqs/where-can-i-find-information-about-volcanoes-alaska) compared to other states.')


#australian epa link for info: https://www.qld.gov.au/environment/management/monitoring/air/air-pollution/pollutants
#usa epa link for info: https://www.epa.gov/environmental-topics/air-topics
with st.container():
    st.subheader('Data Credit:')
    st.write("I gathered the data used in this dashboard from the US's [EPA API](https://aqs.epa.gov/aqsweb/documents/data_api.html) and used information"
                + " found in the [Australian government's enviornmental agency's page](https://www.qld.gov.au/environment/management/monitoring/air/air-pollution/pollutants)"
                +' as well as information from the US EPA to learn more about each of these major air pollutants.')
