import dcc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as core
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True
app.config.suppress_callback_exceptions = True

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
            dcc.appnavbarbrand(
            full={'src': '/assets/images/logo.svg', 'width': 89, 'height': 25, 'alt': 'CoreUI Logo'},
            minimized={'src': '/assets/images/sygnet.svg', 'width': 30, 'height': 30, 'alt': 'CoreUI Logo'}
            ),
            dcc.appsidebartoggler(id='appsidebartogglermd', className='d-md-down-none', display='lg'),
            dbc.Nav([
                dbc.NavItem(
                    dbc.NavLink([html.I(className='cui-bell icons font-xl d-block'), dbc.Badge('5', pill=True, color='danger')], href='#'),
                    className='d-md-down-none'
                ),
                dbc.NavItem(
                    dbc.NavLink(html.I(className='cui-list icons font-xl d-block'), href='#'),
                    className='d-md-down-none'
                ),
                dbc.NavItem(
                    dbc.NavLink(html.I(className='cui-location-pin icons font-xl d-block'), href='#'),
                    className='d-md-down-none'
                ),
                dcc.appheaderdropdown([
                    dbc.DropdownMenu([
                        dbc.DropdownMenuItem('User Info'),
                        dbc.DropdownMenuItem('Logout Max Mustermann')
                    ], nav=True, label='MM')
                ])
            ], className='ml-auto', navbar=True),
            dcc.appasidetoggler(id='appasidetogglermd', className='d-md-down-none'),
            dcc.appasidetoggler(id='appasidetogglerlg', className='d-lg-none', mobile=True)
        ],        
    	fixed=True
    ),
    html.Div([
        dcc.appsidebar([
            dcc.appsidebarheader()
        ], fixed=True, display='lg')
    ], className='app-body'),
    html.Div(id='output'),
    dcc.appfooter(
    )
], className='app')


# @app.callback(Output('output', 'children'), [Input('input', 'value')])
# def display_output(value):
#     return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
