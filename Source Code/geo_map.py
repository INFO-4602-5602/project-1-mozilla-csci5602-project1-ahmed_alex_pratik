# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import pycountry as pc
import plotly.graph_objects as go

def privacy_answer(response):
    if 'privacy' in response.lower():
        return 1
    return 0

def get_country_code(country_name):
    return country_code_maps[country_name]

def change_name(country_name):
    try:
        if country_name == 'Macau':
            return 'Macao'
        elif country_name =='Swaziland':
            return 'Eswatini'
        elif 'Palestinian' in country_name:
            return 'Palestine'
        elif country_name in 'Cape Verde':
            return 'Verde'
        elif 'Europe' in country_name or 'Anonymous Proxy' in country_name or 'Asia' in country_name:
            return np.nan
        else:
            return country_name
    except: # if its nan, just ignore
        pass
    
    
def get_score(row):
    return row['Tech Score'] * row['Privacy Score']


def change_privacy_priority(value):
    if value > 0:
        return -(value-11)
    return 0


def get_text(row):
    return row['Country'] + '<br>' + 'Tech Knowledge Score: ' + str(round(row['Tech Score'], 2)) + '<br>' + 'Privacy Priority Score: ' + \
                    str(round(row['Privacy Score'], 2)) + '<br>' + 'Final Score: ' + str(round(row['Score'], 2))

df = pd.read_csv('20171013111831-SurveyExport.csv', encoding = 'ISO-8859-1', low_memory=False)

privacy_col_name = 'Privacy:YouÛªre planning on buying your next cool new tech toy. Maybe itÛªs a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.'

tech_savvy_columns = [
    'WiFi Router:Check all the internet connected devices you currently own:',
    'Laptop computer:Check all the internet connected devices you currently own:',
    'Smart phone:Check all the internet connected devices you currently own:',
    'Smart TV:Check all the internet connected devices you currently own:',
    'Activity Tracker (ex: Fitbit or Apple Watch):Check all the internet connected devices you currently own:',
    'Smarthome Hub (ex. Amazon Echo, Google Alexa):Check all the internet connected devices you currently own:',
    'Car that connects to the internet:Check all the internet connected devices you currently own:',
    'Smart Thermostat (ex: Nest):Check all the internet connected devices you currently own:',
    'Smart Appliance (ex. Coffeemaker, Refrigerator, Oven, Fridge):Check all the internet connected devices you currently own:',
    'Smart Door Locks (ex. Door locks for your home you can open via bluetooth):Check all the internet connected devices you currently own:',
    'Smart Lighting (ex. Connected lighting switches, dimmers, or bulbs):Check all the internet connected devices you currently own:',
    'IoT:Check all the terms below that you could explain to a friend:',
    'Connected Devices:Check all the terms below that you could explain to a friend:',
    'Botnet:Check all the terms below that you could explain to a friend:',
    'Blockchain:Check all the terms below that you could explain to a friend:',
    'RFID:Check all the terms below that you could explain to a friend:',
    'DDOS:Check all the terms below that you could explain to a friend:',
    'Zero Day:Check all the terms below that you could explain to a friend:',
    'VPN:Check all the terms below that you could explain to a friend:',
    'TOR:Check all the terms below that you could explain to a friend:',
    'What is your biggest fear as we move towards a more connected future?',
    privacy_col_name
]


subset = df[tech_savvy_columns].copy()
subset['What is your biggest fear as we move towards a more connected future?'].fillna('no answer', inplace=True)
subset['biggest_fear'] = subset['What is your biggest fear as we move towards a more connected future?'].apply(privacy_answer)
subset.drop('What is your biggest fear as we move towards a more connected future?', inplace=True, axis = 1)
subset.rename(columns={privacy_col_name: "privacy priority"}, inplace=True) 

columns_to_dummify = subset.columns.tolist()[:-2]

numerical_subset = pd.get_dummies(subset, columns=columns_to_dummify)

numerical_subset['Tech Score'] = numerical_subset.iloc[:, 2:].sum(axis=1)

numerical_subset['privacy priority'] = pd.to_numeric(numerical_subset['privacy priority'], errors='coerce')
numerical_subset['privacy priority'] = numerical_subset['privacy priority'].apply(change_privacy_priority)
numerical_subset['Privacy Score'] = numerical_subset.iloc[:, :2].sum(axis=1)

numerical_subset['Country'] = df['Country']
numerical_subset['Country'] = numerical_subset['Country'].apply(change_name)
numerical_subset['Country'].dropna(inplace=True)

country_code_maps = {}

country_names = numerical_subset['Country'].unique().tolist()

for country_name in country_names:
    code = pc.countries.search_fuzzy(country_name)[0].alpha_3
    country_code_maps[country_name] = code
    
average_score_df = numerical_subset.groupby(['Country'], as_index=False).mean()
average_score_df['Score'] = average_score_df.apply(get_score, axis=1)
final_df = average_score_df[['Privacy Score', 'Tech Score', 'Score', 'Country']]
final_df['country_code'] = final_df['Country'].apply(get_country_code)
final_df['text'] = final_df.apply(get_text, axis = 1)


fig = go.Figure(data=go.Choropleth(
    locations = final_df['country_code'],
    z = final_df['Score'],
    text = final_df['text'],
    colorscale = "magma",
    reversescale=True,
    marker_line_width=0.5,
    colorbar_tickprefix = '',
    colorbar_title = 'Score',
))

fig.update_layout(
    title_text = 'Privacy & Tech Awareness Score Across The Globe'
)

fig.write_html('geo_plot.html', auto_open=True)

fig.show()

