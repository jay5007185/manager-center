# %%
from dash import Dash, html
app = Dash(__name__, requests_pathname_prefix="/403-Forbidden/")
app.layout = html.Div([
    html.Header([
        html.Title("403 - Forbidden")
    ]),
    html.Div([
        html.Blockquote(className="container", children=[
            html.Div("403 - Forbidden", style={'font-size':'50px', 'fontWeight':'bold', 'color':'#E74C3C'}),
            html.Div([
                html.P("很抱歉，您目前没有访问此页面或执行此操作的权限。"),
                html.P("可能的原因："),
                html.Ul([
                    html.Li("您需要使用Tableau的特定入口来访问此内容。"),
                    html.Li("此页面或功能可能仅对特定用户或群组开放。"),
                    html.Li("您必须获得授权才能执行此操作。")
                ]),
                html.P("您可以尝试以下操作："),
                html.Ul([
                    html.Li("请使用Tableau仪表板或应用程式来访问此内容。"),
                    html.Li("检查是否需要特殊权限以访问此内容或执行操作"),
                    html.Li("如果您认为这是一个错误，请联系我们的支援团队以获得协助。")
                ])
            ], style={'textAlign':'left', 'margin-left': '35%'})
        ])
    ], style={'textAlign':'center'})
])
