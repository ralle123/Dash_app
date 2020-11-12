import warnings
# Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table as dt
import pandas as pd
from dash.exceptions import PreventUpdate
from server import app
import plotly.figure_factory as ff
import plotly.express as px
from scipy import stats
import numpy as np

warnings.filterwarnings("ignore")
my_page_size = 10
options = []
# Create success layout
layout = html.Div(children=[
    dcc.Location(id='url_login_success', refresh=True),
    html.Div(
        className="container",
        children=[
            html.Div(
                html.Div(
                    className="row",
                    children=[
                        html.Label("Enter a file to work with..."),
                        html.Div(
                            # className="ten columns",
                            children=[
                                html.Br(),
                                # html.Div('Login successfull'),
                                dcc.Upload(
                                    id='upload-data',
                                    children=html.Div([
                                        html.A('Select Files to Upload')]),
                                    style={'width': '100%',
                                           'height': '60px',
                                           'lineHeight': '60px',
                                           'borderWidth': '1px',
                                           'borderStyle': 'dashed',
                                           'borderRadius': '5px',
                                           'textAlign': 'center',
                                           'margin': '10px'},
                                    multiple=False),
                            ]
                        ),
                        html.Div([
                            html.Label('Select below how to clean Columns before loading the file'),
                            html.Table([
                                # header
                                html.Tr([html.Th('Categorical'),html.Th('Numerical')]),
                                # body
                                html.Tr([html.Td([
                                    dcc.Checklist(options=[
                                        {'label': 'lower', 'value': 'lower'},
                                        {'label': 'trim', 'value': 'trim'},
                                        {'label': 'one-hot enc', 'value': 'one-hot'}
                                    ],id='string_col')
                                    ]),html.Td([
                                        dcc.Checklist(options=[
                                            {'label': 'Nulls', 'value': 'lower'},
                                            {'label': 'Outliers', 'value': 'trim'},
                                        ],id='num_col')
                                    ])],style={"border": "1px solid black"})
                            ])
                            ]),
                        html.Br(),
                        html.Div(id="file_info"),
                        html.Div([
                            html.Div(id='mytablefile'),
                            ],className="twelve columns"),
                        html.Div([
                            html.Label("Select a feature from drop-down to plot a distribution"),
                            dcc.Dropdown(
                                id = 'my_optionsdropdown',
                                options= options,
                                value='Choose columns'),
                            ],id='my_dropdown',style={"display":"none"}),
                        html.Div(id='mydiv'),
                        html.Div(
                            className="two columns",
                            # children=html.A(html.Button('LogOut'), href='/')
                            children=[
                                html.Br(),
                                html.Button(id='back-button', children='Go back', n_clicks=0)
                            ]
                        )
                    ]
                )
            )
        ]
    )
])

def clean_outliers(data):
    num_df = data.select_dtypes(exclude=['object'])
    z_scr = stats.zscore(num_df)
    abs_z_scr = np.abs(z_scr)
    fltrd_ent = (abs_z_scr < 3).all(axis=1)
    return data[fltrd_ent]

def lowercase_cat(data):
    ob_df = data.select_dtypes(exclude=['int','float'])
    for col in ob_df.columns:
        data[col] = data[col].str.lower()
    return data

def trimming_cat(data):
    ob_df = data.select_dtypes(exclude=['int','float'])
    for col in ob_df.columns:
        data[col] = data[col].str.strip()
    return data

@app.callback(
    Output('mydiv', 'children'),
    [Input('my_optionsdropdown', 'value')])
def dropDown_selection(value):
    if value == 'Choose columns':
        raise PreventUpdate
    temp_df = pd.read_csv("temp.csv")
    category = temp_df[value].dtype
    
    if (category == 'int' or category == 'float') and (len(temp_df[value].unique())>5):
        x = temp_df[value].tolist() 
        hist_data = [x]
        group_labels = [value]
        fig = ff.create_distplot(hist_data, group_labels)
    else:
         fig = px.histogram(temp_df,x=value)     
 
    return dcc.Graph(id='my-graph', figure=fig)

@app.callback(Output('file_info','children'),
              Output('my_optionsdropdown',"options"),
              Output('mytablefile', 'children'),
              Output('my_dropdown','style'),
			 [Input('upload-data', 'contents'),
			  Input('upload-data', 'filename')])
def update_output(contents, filename):
    if contents is not None:
        dropdown_style = {"display":"inline"}
        df = pd.read_csv(filename)
        ## ***need to see checkboxes to see what functions to call**
        ## take outliers out with z-score
        df = clean_outliers(df)
        ## make all strings lowercase
        df = lowercase_cat(df)
        ## trim all strings
        df = trimming_cat(df)
        df.to_csv('temp.csv')
        file_info = "File Shape - {}".format(df.shape)
        data = df.to_dict('rows')
        columns =  [{"name": i, "id": i, "deletable": True, "selectable": True} for i in (df.columns)]
        dropdown_options=[]
        for col in df.columns:
            dropdown_options.append({'label':col,'value':col})
        return file_info,dropdown_options,dt.DataTable(data=data, columns=columns,editable=True,filter_action="native",sort_action="native",
                            sort_mode="multi",row_selectable="multi",row_deletable=True,selected_rows=[],style_cell={'textAlign': 'center'},style_table={ 'overflowX': 'auto','height':'550px','overflowY': 'auto'},
                            page_current=0,page_size=my_page_size),dropdown_style
    else:
        raise PreventUpdate
@app.callback(Output('url_login_success', 'pathname'),
              [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'
