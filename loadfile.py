import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.exceptions import PreventUpdate
import plotly.figure_factory as ff
import plotly.express as px
from scipy import stats
import numpy as np

app = dash.Dash()
my_page_size = 10
options = []
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.layout = html.Div([
	dcc.Upload(
		id='upload-data',
		children=html.Div([
			'Drag and Drop or ',
			html.A('Select Files')
		]),
		style={
			'width': '100%',
			'height': '60px',
			'lineHeight': '60px',
			'borderWidth': '1px',
			'borderStyle': 'dashed',
			'borderRadius': '5px',
			'textAlign': 'center',
			'margin': '10px'
		},
		multiple=False
	),
    html.Br(),
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
    html.Div(id="file_info"),
    html.Br(),
    html.Div(id='mytablefile'),
    html.Div([
        html.Label("Select a feature from drop-down to plot HISTOGRAM"),
        dcc.Dropdown(
            id = 'my_optionsdropdown',
            options= options,
            value='Choose columns'
            ),
    ]),
    html.Label(id='my_label1'),

        # html.Button(
        #     id='submit-button',
        #     n_clicks=0,
        #     children='Submit',
        #     style={'fontSize':24, 'marginLeft':'30px'}
        # ),
    
	html.Div(id='output-data-upload'),
    
    html.Div(id='mydiv')
])

# @app.callback(dash.dependencies.Output('output-data-upload', 'children'),
# 			 [dash.dependencies.Input('upload-data', 'contents'),
# 			  dash.dependencies.Input('upload-data', 'filename')])
# def update_output(contents, filename):
# 	if contents is not None:
# 		df = pd.read_csv(filename, index_col=0, header=1) #, sep='\t'
# 		return html.Div([
# 			dash_table.DataTable(
# 				id='table',
# 				columns=[{"name": i, "id": i} for i in df.columns],
# 				data=df.to_dict("rows"),
# 				style_cell={'width': '300px',
# 				'height': '60px',
# 				'textAlign': 'center'})
# 			])
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
    dash.dependencies.Output('mydiv', 'children'),
    [dash.dependencies.Input('my_optionsdropdown', 'value')])
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
 
    return dcc.Graph(id='my-graph', figure=fig)#'You have selected "{}"'.format(value)
  
@app.callback(dash.dependencies.Output('file_info','children'),
              dash.dependencies.Output('my_optionsdropdown',"options"),
              dash.dependencies.Output('mytablefile', 'children'),
			 [dash.dependencies.Input('upload-data', 'contents'),
			  dash.dependencies.Input('upload-data', 'filename')])
def update_output(contents, filename):
    if contents is not None:
        df = pd.read_csv(filename)
        print(df.shape)
        ## take outliers out with z-score
        df = clean_outliers(df)
        ## make all strings lowercase
        df = lowercase_cat(df)
        ## trim all strings
        df = trimming_cat(df)
        print(df.shape)
        df.to_csv('temp.csv')
        file_info = "File Shape - {}".format(df.shape)
        data = df.to_dict('rows')
        columns =  [{"name": i, "id": i, "deletable": True, "selectable": True} for i in (df.columns)]
        dropdown_options=[]
        for col in df.columns:
            dropdown_options.append({'label':col,'value':col})
        return file_info,dropdown_options,dt.DataTable(data=data, columns=columns,editable=True,filter_action="native",sort_action="native",
                            sort_mode="multi",row_selectable="multi",row_deletable=True,selected_rows=[],style_cell={'textAlign': 'center'},style_table={ 'overflowX': 'auto','height':'300px','overflowY': 'auto'},
                            page_current=0,page_size=my_page_size)
    else:
        raise PreventUpdate
    
if __name__ == "__main__":
    app.run_server()#host="0.0.0.0")