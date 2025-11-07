import dash
from dash import Dash, html, dcc, callback
from dash_table import DataTable
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
from datetime import timedelta
from dash.dash_table.Format import Group
from datetime import datetime, timedelta
import json

#%%
product_name = 'withdraw_check_history'

### redis conection


app = dash.Dash(__name__, title = "withdraw_check_history", external_stylesheets=[dbc.themes.BOOTSTRAP], requests_pathname_prefix="/login_page/")
# app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("彩票數據分析平台"),
    dbc.Col([
    html.Label('登入帐号：', style={'font-size': '20px', 'margin-right': '10px', 'fontFamily': 'Arial, sans-serif'}),
    dcc.Input(
        id='input-oggingName',
        type='text',
        value='',  # 默认值为空
        style={'width': '70%', 'height': '40px', 'fontSize': '18px', 'margin-bottom': 0, 'margin-top': 3},
    ),]),
    dbc.Col([
    html.Label('登入密碼：', style={'font-size': '20px', 'margin-right': '10px', 'fontFamily': 'Arial, sans-serif'}),
    dcc.Input(
        id='linput-password',
        type='text',
        value='',  # 默认值为空
        style={'width': '70%', 'height': '40px', 'fontSize': '18px', 'margin-bottom': 0, 'margin-top': 3},
    ),])
    ])