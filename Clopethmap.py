#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:29:12 2020

@author: hendrasetiawan
"""
import plotly.graph_objects as go 
import plotly.express as px
import pandas as pd

fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )
import plotly.graph_objects as go 
dfs = px.data.gapminder().query("year==2007")
dffromwb = pd.read_csv('dashboardready1.csv')
dffromwb=dffromwb.rename(columns={"Country Name": "country"})
dffromwbbaddebt=dffromwb.loc[dffromwb['Indicator Name']=="Bank nonperforming loans to total gross loans (%)"]
dffromwbbankcredit=dffromwb.loc[dffromwb['Indicator Name']=="Domestic credit to private sector by banks (% of GDP)"]
dffromwbbaddebt=dffromwbbaddebt.fillna(0)
dffromwbbankcredit=dffromwbbankcredit.fillna(0)
dffromwbbaddebt=dffromwbbaddebt.rename(columns={"Value": "Bank nonperforming loans to total gross loans (%)"})
dffromwbbankcredit=dffromwbbankcredit.rename(columns={"Value": "Domestic credit to private sector by banks (% of GDP)"})
dfjoin = pd.merge(dfs, dffromwbbaddebt, on=['country'])


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.H1('Banking Industry Bad Debt Heatmap', style={'textAlign': 'center'}),
    dcc.RadioItems(id='mapyear',
    options=[
        {'label': '2007', 'value': '2007'},
        {'label': '2008', 'value': '2008'},
        {'label': '2009', 'value': '2009'}
    ],
    value='2007',
    labelStyle={'display': 'inline-block'}),  
    dcc.Graph(id="heatmap")
],style={'width': '100%', 'float': 'right', 'display': 'inline-block'})

@app.callback(
    dash.dependencies.Output("heatmap", "figure"), 
    [dash.dependencies.Input("mapyear", "value")])

def display_map(mapyear):
    
    dfjoinyearselected=dfjoin.loc[dfjoin['Year']==int(mapyear)]

    fig = px.choropleth(dfjoinyearselected, locations="iso_alpha",
                    color="Bank nonperforming loans to total gross loans (%)", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.OrRd)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    