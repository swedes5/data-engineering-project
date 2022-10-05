# Data Engineering Project
The goal of this project was to use methods to gather and store large data in an efficient manner.  I was able to gather large data from the Environmental Protection Agency (EPA) weather data API and store it in a SQLite database effectively.[[A quick side note that I reset my API key so the one in this code will not work. To get your own go to: https://aqs.epa.gov/aqsweb/documents/data_api.html#signup]]  Then, using Streamlit (an app for deploying web pages),  I was able to create an interactive dashboard for users to be able to view some simple plots regarding my data.

The requirements.txt and app.py files are for the streamlit app I created.  The link for that is here: https://swedes5-data-engineering-project-app-nu3qn8.streamlitapp.com/

The two screenshots are there in case the instructor wants to verify I was using sufficient data in the pipeline portion of this project.  In the pipeline, I recieved 25m+ rows from the EPA API and 29 columns of which I kept 6 for my specific needs. 

The data gathering file is there to show how I used the API to form the data frames and CSVs I needed to add the data to my SQLite database.
