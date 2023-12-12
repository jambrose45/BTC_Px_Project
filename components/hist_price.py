from dash import html, dcc, Output, Input
import plotly.express as px

def render(app,data):
    @app.callback(
            Output("hist-price", "children"),
            Input("dropdown","value")
    )
    def update_hist_price(dropdown):  
        fig = px.line(
            data,
            x = "Date",
            y = "Close",
            title = "Long Term BTC Price Chart"
            )
        fig.add_vline(x = dropdown, line_dash = "dash", line_color = "red") 
        return html.Div(dcc.Graph(figure=fig), id="hist-price")
    return html.Div(id="hist-price")