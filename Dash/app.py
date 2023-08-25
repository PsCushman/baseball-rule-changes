import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = [('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap')]

# Set up inline styles
BODY_STYLE = {
    'backgroundColor': '#e1ad01',
    'margin': '0',
    'padding': '0',
    'font-family': 'Alfa Slab One, cursive'
}

# Define inline styles for the z-score box
z_score_box_style_base = {
    "padding": "2px",
    "border": "2px solid #3e363f",
    "font-weight": "bold",
    "margin-top": "4px",
    "margin-bottom": "4px",
    "width": "fit-content",
    "color": '#333333'  # Text color
}

z_score_box_style_green = {
    **z_score_box_style_base,
    "background-color": "#3f826d"  # Green background color
}

z_score_box_style_red = {
    **z_score_box_style_base,
    "background-color": "#e2725b"  # Red background color
}

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style=BODY_STYLE, children=[
    html.H1("Baseball Player Dashboard"),
    dcc.Input(id="player-name", type="text", placeholder="Enter player's name"),
    html.Div(id="output-container", children=[
        html.Div(id="z-score-box", className="z-score-box", style=z_score_box_style_base),
        html.Div(id="output-graphs"),
        html.Div(id="player-info-container", className="player-info-container")
    ])
])

@app.callback(
    [Output("output-graphs", "children"),
     Output("z-score-box", "children"),
     Output("z-score-box", "className"),
     Output("player-info-container", "children")],
    [Input("player-name", "value")]
)

def update_graphs(name):
    if not name:
        return [], [], "z-score-box", []

    player_data = pd.read_csv("dash_full_batter_data.csv")

    # Use case-insensitive search for player name
    player_info = player_data[player_data["Name"].str.contains(name, case=False)]

    if player_info.empty:
        return [html.Div("Player not found")], [], "z-score-box", []

    fig = px.bar(player_info, x="Name", y=["avg_wOBA", "wOBA_2023"], 
                 labels={"value": "wOBA"}, title="Average wOBA for Player {}".format(name),
                 barmode="group")

    z_score_difference_woba = player_info["z_scores_avg_woba"].values[0]
    z_score_color_class = "z-score-box-green" if z_score_difference_woba > 0 else "z-score-box-red"

# Apply the appropriate style based on z_score_color_class
    if z_score_color_class == "z-score-box-green":
        z_score_box_style = z_score_box_style_green
    else:
        z_score_box_style = z_score_box_style_red

    z_score_box = html.Div(
        f"wOBA Difference: {z_score_difference_woba:.2f}",
        style=z_score_box_style
        )

    selected_columns = [
        "Name", "AB", "H", "SB", "HR", "RBI", "SO", "AVG",
        "SLG", "OPS", "WAR", "Barrel%"
    ]

    # Round numeric values to 3 decimal places
    player_info_rounded = player_info[selected_columns].round(3)
    
    player_info_table = dash_table.DataTable(
        columns=[{"name": col, "id": col} for col in selected_columns],
        data=player_info_rounded.to_dict("records")
    )

    return [dcc.Graph(figure=fig)], z_score_box, z_score_color_class, [player_info_table]

if __name__ == "__main__":
    app.run_server(debug=True)
