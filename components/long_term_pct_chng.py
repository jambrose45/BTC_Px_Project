from dash import Dash,html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd

def render(app,data):
    @app.callback(
            Output("long-term-change", "children"),
            Input("dropdown","value")
    )
    def calc_pct_chng(dropdown):  
        start_date = pd.to_datetime(dropdown)    
        end_date = data[data["Date"] == data["Date"].max()]
        start_date_px = data[data["Date"] == start_date]["Close"].squeeze()
        end_date_px = end_date["Close"].squeeze()     
        long_term_chng = (end_date_px - start_date_px) / start_date_px * 100     
        if long_term_chng > 0:
            sm_lyout = html.Div([ dbc.Row(
                    [
                        dbc.Col(html.Img(src=Dash.get_asset_url(app,"rocket.gif")),lg=12)
                    ]
                )])
        else:
            sm_lyout = html.Div([ dbc.Row(
                    [
                        dbc.Col(html.Img(src=Dash.get_asset_url(app,"mcd.jpg")),lg=4),
                    ]
                )])
        if long_term_chng != 0:
            html.Div("No data selected", id="long-term-change")
        return html.Div(
            [
                dbc.Col(html.H1(f"Long Term Pct Change: {long_term_chng:.8}%")),
                dbc.Col(sm_lyout)
            ], id="long-term-change")
    return html.Div(id="long-term-change")