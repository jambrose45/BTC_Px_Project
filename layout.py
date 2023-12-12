from dash import Dash,html
import dash_bootstrap_components as dbc
from components import dropdown, hist_price,zoom_graph,short_term_pct_chng,long_term_pct_chng


def create_layout(app,data):
    return dbc.Container(
        [
            dbc.Row(
                [
                    html.Div(html.H1("BTC Price Project")),
                    dropdown.render(app,data),
                 ]
            ),
            dbc.Row(
                [
                    dbc.Col(hist_price.render(app,data),lg=6),
                    dbc.Col(zoom_graph.render(app,data),lg=6),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(html.P(long_term_pct_chng.render(app,data),),lg=6),
                    dbc.Col(html.P(short_term_pct_chng.render(app,data)),lg=6)
                ]
            )
        ]
    )