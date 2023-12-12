from dash import html, dcc, Output, Input
import pandas as pd
import plotly.express as px

def render(app,data):
    @app.callback(
            Output("zoom-graph", "children"),
            Input("dropdown","value")
    )
    def update_zoom_price(dropdown):  
        start_date = pd.to_datetime(dropdown) - pd.DateOffset(days=10)
        end_date = pd.to_datetime(dropdown) + pd.DateOffset(days=10)
        filtered_data = data.loc[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
        if filtered_data.shape[0]==0:
            html.Div("No data selected", id="zoom-graph")
        fig = px.line(
            filtered_data,
            x = "Date",
            y = "Close",
            title = "Short Term BTC Price Chart"
            )
        fig.add_vline(x = dropdown, line_dash = "dash", line_color = "red") 
        return html.Div(dcc.Graph(figure=fig), id="zoom-graph")
    return html.Div(id="zoom-graph")
