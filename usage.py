import dcc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as core
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)

dashboard_layout = html.Div([
    html.H3('Dashboard'),
    dbc.Card([
        dbc.CardHeader('Text Area'),
        dbc.CardBody([
            core.Textarea(
                id='dashboard-test-textarea',
                placeholder='Enter a value...',
                value='Hello, world!',
                rows=20,
                style={'width': '100%', 'height': 'auto'}
            ),
            html.Div(id='dashboard-test-output')
        ])
    ])
])

app.layout = html.Div([
    dcc.appheader(
        [
            dcc.appsidebartoggler(id='appsidebartogglerlg', className='d-lg-none', display='md', mobile=True),
            dcc.appnavbarbrand(
            full={'src': '/assets/images/logo.svg', 'width': 89, 'height': 25, 'alt': 'CoreUI Logo'},
            minimized={'src': '/assets/images/sygnet.svg', 'width': 30, 'height': 30, 'alt': 'CoreUI Logo'}
            )
        ],        
    	fixed=True
    ),
    html.Div(id='output'),
    dcc.appfooter(
    ),
    dcc.firstapp(   
        id='input',
        value='my-value',
        label='my-label'
    )
], className='app')


# @app.callback(Output('output', 'children'), [Input('input', 'value')])
# def display_output(value):
#     return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
