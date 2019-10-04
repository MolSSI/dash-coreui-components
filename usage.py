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

# dashboard_layout = html.Div([
#     html.H3('Dashboard'),
#     dbc.Card([
#         dbc.CardBody(
#             [
#                 html.H4("Card title", className="card-title"),
#                 html.P(
#                     "Some quick example text to build on the card title and "
#                     "make up the bulk of the card's content.",
#                     className="card-text",
#                 ),
#                 dbc.Button("Go somewhere", color="primary"),
#             ]
#         )    
#     ],
#     style={"width": "18rem"},)
# ])

# charts_layout = html.Div([
#     html.H3('Charts'),
#     dbc.Card([
#         dbc.CardHeader('Random Walk'),
#         dbc.CardBody([
#             core.Graph(id='charts-graph-output', style={'width': '100%'})
#         ], className='p-0')
#     ])
# ])

# other_animals_layout = html.Div([
#     html.H3('Other Animals'),
#     html.P('You are on the page for other animals.'),
#     html.Div(id='other-animals-test-output')
# ])

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
            dcc.appsidebarheader(),
            dcc.appsidebarform(),
            dcc.appsidebarnav(id='current-url', navConfig={
                'items': [
                    {
                        'name': 'Dashboard',
                        'url': '/',
                        'icon': 'cui-speedometer icons',
                        'badge': {'variant': 'info', 'text': 'NEW'}
                    },
                    {'name': 'Components', 'title': True},
                    {
                        'name': 'Base',
                        'url': '/base',
                        'icon': 'cui-puzzle icons',
                        'children': [
                            {
                                'name': 'Card',
                                'url': '/base/card',
                                'icon': 'cui-puzzle icons'
                            }
                        ]
                    },
                    {
                        'name': 'Buttons',
                        'url': '/buttons',
                        'icon': 'cui-arrow-left icons'
                    },
                    {
                        'name': 'Charts',
                        'url': '/charts',
                        'icon': 'cui-chart icons'
                    },
                    {
                        'name': 'Editors',
                        'url': '/editors',
                        'icon': 'cui-brush icons'
                    },
                    {
                        'name': 'Forms',
                        'url': '/forms',
                        'icon': 'cui-ban icons'
                    },
                    {
                        'name': 'Other',
                        'url': '/other',
                        'icon': 'cui-star icons',
                        'children': [
                            {
                                'name': 'Animals',
                                'url': '/other/animals',
                                'icon': 'cui-star icons',
                                'badge': {'variant': 'success', 'text': 'RAD'}
                            }
                        ]
                    },
                    {'name': 'Group Title', 'title': True},
                    {
                        'name': 'Disabled',
                        'url': '/',
                        'icon': 'cui-ban icons',
                        'attributes': {'disabled': True},
                    }
                ]
            }),
            dcc.appsidebarfooter()
            ], fixed=True, display='lg'),
   
        html.Main([
            dcc.appbreadcrumb(appRoutes=[{'path': '/', 'name': 'Dashboard'}]),
            dbc.Container([
                dcc.approuteconditional([
                    dbc.Row([
                        dbc.Col(
                            dcc.appcard([
                                dbc.CardHeader("Card Title"),
                                dbc.CardBody(
                                        [
                                            
                                            html.P(
                                                "Some quick example text to build on the card title and "
                                                "make up the bulk of the card's content.",
                                                className="card-text",
                                            ),
                                        ]
                                    )    
                                ], style={"width": "20rem"})
                            ),
                        dbc.Col(
                            dcc.appcard([
                                dbc.CardBody(
                                        [
                                            html.P(
                                                "Some quick example text to build on the card title and "
                                                "make up the bulk of the card's content.",
                                                className="card-text",
                                            ),
                                        ]
                                    ),
                                dbc.CardFooter("Card Footer"),    
                                ], style={'width': '20rem'})
                            ),
                        dbc.Col(
                            dcc.appcard([
                                dbc.CardBody(
                                        [
                                            html.P(
                                                "Some quick example text to build on the card title and "
                                                "make up the bulk of the card's content.",
                                                className="card-text",
                                            ),
                                            html.H4("Card title", className="card-title"),
                                        ]
                                    )    
                                ], style={'width': '20rem'})
                            )

                    ])

                    ], id='card1', route='/base/card'),

                dcc.approuteconditional([
                    dcc.appcard([
                            dbc.CardHeader("Standard Buttons"),
                            dbc.CardBody(
                                    [
                                       html.Div(
                                            [
                                                dbc.Button("Primary", color="primary", className="mr-1"),
                                                dbc.Button("Secondary", color="secondary", className="mr-1"),
                                                dbc.Button("Success", color="success", className="mr-1"),
                                                dbc.Button("Warning", color="warning", className="mr-1"),
                                                dbc.Button("Danger", color="danger", className="mr-1"),
                                                dbc.Button("Info", color="info", className="mr-1"),
                                                dbc.Button("Light", color="light", className="mr-1"),
                                                dbc.Button("Dark", color="dark", className="mr-1"),
                                                dbc.Button("Link", color="link"),
                                            ]
                                        )  
                                    ]
                                )    
                            ])
                ], id='buttons', route='/buttons'),

                dcc.approuteconditional([
                    dcc.appcard([
                            dbc.CardHeader("Credit Card"),
                            dbc.CardBody(
                                    [
                                        dbc.Row([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Name"),
                                                    dbc.Input(type="text", id="name", placeholder="Enter your name"),
                                                ], className='col-sm-12'),
                                        ]),
                                        dbc.Row([
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label("Credit Card Number"),
                                                    dbc.Input(type="text", id="ccnumber", placeholder="0000 0000 0000 0000"),
                                                ], className='col-sm-12'),
                                        ]), 
                                        dbc.Row([
                                            dbc.FormGroup([
                                                dbc.Label("Month"),
                                                core.Dropdown(

                                                    id="dropdown1",
                                                    options=[
                                                        {"label": "1", "value": 1},
                                                        {"label": "2", "value": 2},
                                                        {"label": "3", "value": 3},
                                                        {"label": "4", "value": 4},
                                                        {"label": "5", "value": 5},
                                                        {"label": "6", "value": 6},
                                                        {"label": "7", "value": 7},
                                                        {"label": "8", "value": 8},
                                                        {"label": "9", "value": 9},
                                                        {"label": "10", "value": 10},
                                                        {"label": "11", "value": 11},
                                                        {"label": "12", "value": 12},
                                                    ],
                                                ),
                                            ], className='col-sm-4'),

                                            dbc.FormGroup([
                                                dbc.Label("Year"),
                                                core.Dropdown(

                                                    id="dropdown2",
                                                    options=[
                                                        {"label": "2014", "value": 1},
                                                        {"label": "2015", "value": 2},
                                                        {"label": "2016", "value": 3},
                                                        {"label": "2017", "value": 4},
                                                        {"label": "2018", "value": 5},
                                                        {"label": "2019", "value": 6},
                                                    ],
                                                ),
                                            ], className='col-sm-4'),

                                            dbc.FormGroup([
                                                dbc.Label("CVV"),
                                                dbc.Input(type="text", id="cvv", placeholder="CVV")
                                            ], className='col-sm-4')                             

                                        ])                                       
                                    ]
                                )    
                            ])
                ], id='forms', route='/forms'),                
                    #dcc.approuteconditional(id='approuteconditional', route='/', children=dashboard_layout)
                    #dcc.approuteconditional(id='approuteconditional', route='/charts', children=charts_layout)
                    #dcc.approuteconditional(route='/other/animals', children=other_animals_layout)
                ], id='page-content', fluid=True)
            ], className='main')
        ], className='app-body'),
 #   html.Div(id='output'),
    dcc.appfooter(
    )
], className='app')



# @app.callback(Output('charts-graph-output', 'figure'),
#               [Input('charts-aside-random-walk-sd-slider', 'value')])
# def charts_graph_output(charts_aside_random_walk_sd_slider):
#     N = 1000
#     x = np.linspace(0, 1, N)
#     y = np.cumsum(np.square(charts_aside_random_walk_sd_slider) * np.random.randn(N))
#     return { 'data': [go.Scatter(x=x, y=y)]} 


if __name__ == '__main__':
    app.run_server(debug=True)
