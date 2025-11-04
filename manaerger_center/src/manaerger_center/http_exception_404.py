# %%
from dash import Dash, html
app = Dash(__name__, requests_pathname_prefix="/404-NotFound/")
app.layout = html.Div([
    html.Header([
        html.Title("404 - Not Found")
    ]),
    html.Div([
        html.Blockquote(className="container", children=[
            html.Div("404 - Not Found", style={'font-size':'50px', 'fontWeight':'bold', 'color':'#E74C3C'}),
            html.Div([
                html.P("很抱歉，我们无法找到您正在寻找的页面。"),
                html.P("可能的原因："),
                html.Ul([
                    html.Li("您输入的网址有误。"),
                    html.Li("所需的页面已经被移动或删除。"),
                    html.Li("我们的网站正在进行更新，该页面暂时无法访问。")
                ]),
                html.P("您可以尝试以下操作："),
                html.Ul([
                    html.Li("检查您输入的网址是否正确。"),
                    html.Li(html.A("返回首页", href="/")),  # 使用Dash的html.A建立连结
                    html.Li("使用搜索框来寻找您需要的内容。")
                ])
            ], style={'textAlign':'left', 'margin-left': '35%'})
        ])
    ], style={'textAlign':'center'})
])
