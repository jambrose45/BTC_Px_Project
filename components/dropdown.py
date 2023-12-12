from dash import html, dcc

def render(app, data):
    px_dates = data["Date"].unique()
    all_px_dates = [{"label":d, "value":d} for d in px_dates]
    return html.Div(
        [
            html.H6("User Selected Date"),
            dcc.Dropdown(
                options = all_px_dates,
                value = "",
                multi = False,
                id = "dropdown"
            )
        ]
    )
