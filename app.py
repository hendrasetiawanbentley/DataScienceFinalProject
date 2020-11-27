import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

top_markdown_text = '''
This is my first deployed app
'''

df = pd.read_csv('dashboardready1.csv')
df = df.loc[df["Country Name"]!= "Equatorial Guinea"]
df = df.loc[df["Country Name"]!= "Argentina"]
df = df.loc[df["Country Name"]!= "Brazil"]
df = df.loc[df["Country Name"]!= "Bulgaria"]
df = df.loc[df["Country Name"]!= "Zimbabwe"]
df = df.loc[df["Country Name"]!= "Angola"]
df = df.loc[df["Country Name"]!= "Belarus"]
df = df.loc[df["Country Name"]!= "Tajikistan"]
df = df.loc[df["Country Name"]!= "Bahamas, The"]
df = df.loc[df["Country Name"]!= "Mongolia"]
df = df.loc[df["Country Name"]!= "Armenia"]
df = df.loc[df["Country Name"]!= "Uruguay"]
df = df.loc[df["Country Name"]!= "Romania"]
df = df.loc[df["Country Name"]!= "Bolivia"]
df = df.loc[df["Country Name"]!= "Trinidad and Tobago"]
df = df.loc[df["Country Name"]!= "Azerbaijan"]
df = df.loc[df["Country Name"]!= "Ukraine"]
df = df.loc[df["Country Name"]!= 'Kyrgyz Republic']
df = df.loc[df["Country Name"]!= 'Malawi']
df = df.loc[df["Country Name"]!= 'Madagascar']
df = df.loc[df["Country Name"]!= 'Colombia']
dftimeseries=df.loc[(df['Indicator Name']=='Real interest rate (%)') & (df['Value'].isna())]
x=dftimeseries["Country Name"]
available_indicators = df['Indicator Name'].unique()
dftimeseriesfinal = df[~df["Country Name"].isin(x)]
available_country=dftimeseriesfinal["Country Name"].unique()

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





app.layout = html.Div([

    dcc.Markdown(children=top_markdown_text),

])

if __name__ == '__main__':
    app.run_server(debug=True)
