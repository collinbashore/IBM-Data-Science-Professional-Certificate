######################## SpaceX Launch Records Dashboard ########################

# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the spacex_launch_data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
launch_sites = []
launch_sites.append({'label': 'ALL Sites', 'value': 'ALL Sites'})
for site in spacex_df["Launch Site"].value_counts().index:
    launch_sites.append({'label': site, 'value': site})

app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # Added a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options=launch_sites,
                                             value='ALL Sites',
                                             placeholder="Select a Launch Site here",
                                             searchable=True),
                                html.Br(),

                                # Added pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # Added a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                value=[min_payload, max_payload],
                                                marks={2500: {'label': '2500 (kg)'}, 5000: {'label': '5000 (kg)'}, 
                                                       7500: {'label': '7500 (kg)'}}),

                                # Added a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))

# Created function to plot a pie chart
def get_pie_chart(entered_site):
    if entered_site == 'ALL Sites':
        launches_df = spacex_df.groupby(['Launch Site'])['class'].sum().to_frame()
        launches_df = launches_df.reset_index()
        fig = px.pie(launches_df, values='class', names='Launch Site', 
                     title='Total Success Launches By Site',
                     color_discrete_sequence = ['blue', 'darkorchid', 'darkorange', 'gold'])
    else:
        launches_df = spacex_df[spacex_df['Launch Site'] == entered_site]['class'].sum().to_frame()
        launches_df['name'] = ['Failure', 'Success']
        fig = px.pie(launches_df, values='class', names='name',
                     title='Total Success Launches for' + entered_site,
                     color_discrete_sequence = ['blue', 'darkorchid'])
    return fig
    
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'),
              Input(component_id='payload-slider', component_property='value'))

def get_scatter_plot(entry1, entry2):
    if entry1 == 'ALL Sites':
        filtered_df = spacex_df
        filtered_df2 = filtered_df[filtered_df["Payload Mass (kg)"] >= entry2[0]]
        filtered_df3 = filtered_df2[filtered_df["Payload Mass (kg)"] <= entry2[1]]
        fig2 = px.scatter(filtered_df3, x="Payload Mass (kg)", y="class", color="Booster Version Category",
                          title = "Correlation Between Payload and Success for ALL Sites",
                          color_discrete_sequence = ['blue', 'darkorchid', 'mediumslateblue','darkorange', 'mediumvioletred'])
    else:
        filtered_df = spacex_df[spacex_df["Launch Site"] == entry1]
        filtered_df2 = filtered_df[filtered_df["Payload Mass (kg)"] >= entry2[0]]
        filtered_df3 = filtered_df2[filtered_df["Payload Mass (kg)"]>= entry2[1]]
        fig2 = px.scatter(filtered_df3, x="Payload Mass (kg)", y="class", color="Booster Version Category",
                          title = "Correlation Between Payload and Success for " + entry1)
    
    return fig2

# Run the app
if __name__ == '__main__':
    app.run_server()
