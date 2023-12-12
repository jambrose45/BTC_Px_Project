from dash import Dash,html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd

def render(app,data):
    @app.callback(
            Output("shrt-term-change", "children"),
            Input("dropdown","value")
    )
    def calc_pct_chng(dropdown):  
        start_date = pd.to_datetime(dropdown) - pd.DateOffset(days=10)
        end_date = pd.to_datetime(dropdown) + pd.DateOffset(days=10)
        start_date_px = data[data["Date"] == start_date]["Close"].squeeze()     
        end_date_px = data[data["Date"] == end_date]["Close"].squeeze()      
        short_term_chng = (end_date_px - start_date_px ) / start_date_px * 100 
        if  short_term_chng > 0:
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
        if short_term_chng != 0:
            html.Div("No data selected", id="shrt-term-change")
        return html.Div(
            [
                dbc.Col(html.H1(f"Short Term Pct Change: {short_term_chng:.8}%")),
                dbc.Col(sm_lyout)
            ], id="shrt-term-change")
    return html.Div(id="shrt-term-change")