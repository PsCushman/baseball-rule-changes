import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap',
    {'href': 'https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/fenway-park-boston-seating-chart-vintage-patent-blueprint-design-turnpike.jpg', 'rel': 'stylesheet'}
]
# Set up inline styles
BODY_STYLE = {
    'backgroundColor': '#e1ad01',
    'margin': '0',
    'padding': '0',
    'font-family': 'Alfa Slab One, cursive'
}

BACKGROUND_IMAGE_STYLE = {
    'background-image': 'url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/fenway-park-boston-seating-chart-vintage-patent-blueprint-design-turnpike.jpg")',
    'background-size': 'cover',
    'background-repeat': 'no-repeat',
    'background-position': 'center center',
    'position': 'absolute',
    'top': '0',
    'left': '0',
    'width': '100%',
    'height': '100%',
    'z-index': '-1',  # Place the background below other content
    'opacity': '0.5',  # Adjust the opacity of the background image

}

output_differences_style = (
    "display: flex; justify-content: space-between; margin: 10px 0;"
)

# Define inline styles for the z-score box
z_score_box_style_base = {
    "padding": "2px",
    "font-weight": "bold",
    "font-size": "18",
    "margin-top": "10px",
    "width": "fit-content",
    "color": '#3e363f',  # Text color
}

z_score_box_style_green = {
    **z_score_box_style_base,
    "background-color": "#3f826d",
    "border": "2px solid #3e363f", 
    "padding": "4px", # Green background
}

z_score_box_style_red = {
    **z_score_box_style_base,
    "background-color": "#e2725b",
    "border": "2px solid #3e363f",
    "padding": "4px",  # Red background
}

button_style = {
    "background-color": "#e2725b",
    "border": "2px solid #3e363f",
    "color": "#3e363f",
    "font-family": "Alfa Slab One, cursive",
    "font-weight": "bold",
    "padding": "2px",
    "margin": "2px",
    "cursor": "pointer",
    "text-align": "center",
    "text-decoration": "none",
    "display": "inline-block",
    "border-radius": "5px",
}

H3_style = {
    "font-size": "14px",
    "color": '#3e363f',
}

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div(style=BACKGROUND_IMAGE_STYLE),  # Background image div

    html.Div(style=BODY_STYLE, children=[
    html.Div([
        html.H1("Hitter Performance Dashboard", style={"margin-bottom": "5px"}),  
    ], style={"display": "flex", "align-items": "center"}),
    html.Div([
        html.P("Click the prediction box for feature importance for each metric.", style={"margin-top": "5px", "color": '#3e363f'}), 
    ], style={"display": "flex", "align-items": "center"}),
    # Buttons section
    html.Div([
        html.A(html.Button("Hitter Predictor Analysis", style=button_style), href="https://pscushman.github.io/final-project-analysis/", target="_blank"),
        html.A(html.Button("Predicting WAR for 2023", style=button_style), href="https://public.tableau.com/app/profile/leonardo.pierantoni/viz/MLBPredictions/Story1?publish=yes", target="_blank"),
        html.A(html.Button("Predicting Pitcher Performance", style=button_style), href="http://127.0.0.1:8050/", target="_blank"),
    ], style={"display": "flex", "align-items": "center", "justify-content": "flex-end"}),
    
    html.Div(dcc.Input(id="player-name", type="text", placeholder="Enter player's name")),
    
    html.Div(id="output-container", children=[
        html.Div(id="output-differences", style={
            "display": "flex",
            "justify-content": "space-between",
            "margin": "10px 0",
        }, children=[
            html.Div(id="woba-difference-box", className="z-score-box", style={
                **z_score_box_style_base,
                "flex": "1",
                "margin-right": "10px",
            }),
            html.Div(id="slg-difference-box", className="z-score-box", style={
                **z_score_box_style_base,
                "flex": "1",
                "margin-right": "10px",
            }),
            html.Div(id="babip-difference-box", className="z-score-box", style={
                **z_score_box_style_base,
                "flex": "1",
                "margin-right": "10px",
            }),
            html.Div(id="wrc-difference-box", className="z-score-box", style={
                **z_score_box_style_base,
                "flex": "1",
            }),
        ]),
        # Adding the four verdict boxes
        html.Div(id="verdict-boxes", style={
            "display": "flex",
            "justify-content": "space-between",
            "margin": "10px 0",
        }, children=[
            html.Div(id="woba-verdict-box", className="verdict-box", style={
                **z_score_box_style_base ,
                "flex": "1",
                "margin-right": "10px",
            }),
            html.Div(id="slg-verdict-box", className="verdict-box", style={
                **z_score_box_style_base ,
                "flex": "1",
                "margin-right": "10px",
            }),
            html.Div(id="babip-verdict-box", className="verdict-box", style={
                **z_score_box_style_base ,
                "flex": "1",
                "margin-right": "10px",
            }),
            html.Div(id="wrc-verdict-box", className="verdict-box", style={
                **z_score_box_style_base ,
                "flex": "1",
            }),
        ]),
    html.Div(id="player-info-container", className="player-info-container"),
            
    html.Div(id="output-graphs", style={
                "padding": "20px",   # Add padding to the graphs area
            })
        ])
    ])
])

@app.callback(
    [Output("output-graphs", "children"),
     Output("woba-difference-box", "children"),
     Output("woba-difference-box", "className"),
     Output("slg-difference-box", "children"),
     Output("slg-difference-box", "className"),
     Output("babip-difference-box", "children"),
     Output("babip-difference-box", "className"),
     Output("wrc-difference-box", "children"),
     Output("wrc-difference-box", "className"),
     Output("woba-verdict-box", "children"),
     Output("woba-verdict-box", "className"),
     Output("slg-verdict-box", "children"),
     Output("slg-verdict-box", "className"),
     Output("babip-verdict-box", "children"),
     Output("babip-verdict-box", "className"),
     Output("wrc-verdict-box", "children"),
     Output("wrc-verdict-box", "className"),
     Output("player-info-container", "children")],
    [Input("player-name", "value")]
)
def update_graphs(name):
    if not name:
        return (
            [],  # Output "output-graphs.children"
            [],  # Output "woba-difference-box.children"
            "z-score-box",  # Output "woba-difference-box.className"
            [],  # Output "slg-difference-box.children"
            "z-score-box",  # Output "slg-difference-box.className"
            [],  # Output "babip-difference-box.children"
            "z-score-box",  # Output "babip-difference-box.className"
            [],  # Output "wrc-difference-box.children"
            "z-score-box",  # Output "wrc-difference-box.className"
            "",  # Output "woba-verdict-box.children"
            "z-score-box",  # Output "woba-verdict-box.className"
            "",  # Output "slg-verdict-box.children"
            "z-score-box",  # Output "slg-verdict-box.className"
            "",  # Output "babip-verdict-box.children"
            "z-score-box",  # Output "babip-verdict-box.className"
            "",  # Output "wrc-verdict-box.children"
            "z-score-box",  # Output "wrc-verdict-box.className"
            [],  # Output "player-info-container.children"
        )

    player_data = pd.read_csv("dash_full_batter_data.csv")
    verdict_data = pd.read_csv("verdict.csv")
    
    player_info = player_data[player_data["Name"].str.contains(name, case=False)]
    verdict_info = verdict_data[verdict_data["Name"].str.contains(name, case=False)]
    
    if player_info.empty:
        return [html.Div("Player not found")], [], "z-score-box", [], "z-score-box", [], "z-score-box", [], "z-score-box", "", "z-score-box", "", "z-score-box", "", "z-score-box", "", "z-score-box", [html.Div()]

    # Create a 2x2 grid of subplots
    fig = make_subplots(rows=2, cols=2, subplot_titles=["Avg. wOBA  /  wOBA 2023", "Avg. SLG  /  SLG 2023", 
                                                        "Avg. BABIP  /  BAIP 2023", "Avg. wRC+  /  wRC+ 2023"],
                        shared_xaxes=False, horizontal_spacing=0.1)

    # Add the four bar graphs to the subplots
    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["avg_wOBA"], name="avg_wOBA", marker_color='#44cec5'), row=1, col=1)
    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["wOBA_2023"], name="wOBA_2023", marker_color='#321b47'), row=1, col=1)

    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["SLG"], name="SLG", marker_color='#44cec5'), row=1, col=2)
    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["SLG_2023"], name="SLG_2023", marker_color='#321b47'), row=1, col=2)

    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["BABIP"], name="BABIP", marker_color='#44cec5'), row=2, col=1)
    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["BABIP_2023"], name="BABIP_2023", marker_color='#321b47'), row=2, col=1)

    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["wRC+"], name="wRC+", marker_color='#44cec5'), row=2, col=2)
    fig.add_trace(go.Bar(x=player_info["Name"], y=player_info["wRC+_2023"], name="wRC+_2023", marker_color='#321b47'), row=2, col=2)
    
    fig.update_traces(showlegend=False)

    fig.update_layout(
    title={
        'text': "Player: Improvement or Decline",
        'font': {'family': 'Alfa Slab One, cursive', 'size': 20, 'color': '#3e363f'}
    },
    barmode="group"
    )

    # Calculate z-score differences and verdicts
    z_score_difference_woba = player_info["zscore_difference_woba"].values[0]
    z_score_color_class_woba = "z-score-box-green" if z_score_difference_woba > 0 else "z-score-box-red"
    verdict_woba = verdict_info["woba_Correctness"].values[0]
    verdict_box_class_woba = "z-score-box-green" if verdict_woba == "Correct :)" else "z-score-box-red"

    z_score_difference_slg = player_info["zscore_difference_slg"].values[0]
    z_score_color_class_slg = "z-score-box-green" if z_score_difference_slg > 0 else "z-score-box-red"
    verdict_slg = verdict_info["SLG_Correctness"].values[0]
    verdict_box_class_slg = "z-score-box-green" if verdict_slg == "Correct :)" else "z-score-box-red"

    z_score_difference_babip = player_info["zscore_difference_babip"].values[0]
    z_score_color_class_babip = "z-score-box-green" if z_score_difference_babip > 0 else "z-score-box-red"
    verdict_babip = verdict_info["BABIP_Correctness"].values[0]
    verdict_box_class_babip = "z-score-box-green" if verdict_babip == "Correct :)" else "z-score-box-red"

    z_score_difference_wrc = player_info["zscore_difference_wrc+"].values[0]
    z_score_color_class_wrc = "z-score-box-green" if z_score_difference_wrc > 0 else "z-score-box-red"
    verdict_wrc = verdict_info["wRC+_Correctness"].values[0]
    verdict_box_class_wrc= "z-score-box-green" if verdict_wrc == "Correct :)" else "z-score-box-red"
    

    # Apply the appropriate style based on z_score_color_class
    z_score_box_style_woba = z_score_box_style_green if z_score_color_class_woba == "z-score-box-green" else z_score_box_style_red
    z_score_box_woba = html.Div(
        f"wOBA Difference: {z_score_difference_woba:.2f}",
        style=z_score_box_style_woba
    )

    z_score_box_style_slg = z_score_box_style_green if z_score_color_class_slg == "z-score-box-green" else z_score_box_style_red
    z_score_box_slg = html.Div(
        f"SLG Difference: {z_score_difference_slg:.2f}",
        style=z_score_box_style_slg
    )

    z_score_box_style_babip = z_score_box_style_green if z_score_color_class_babip == "z-score-box-green" else z_score_box_style_red
    z_score_box_babip = html.Div(
        f"BABIP Difference: {z_score_difference_babip:.2f}",
        style=z_score_box_style_babip
    )

    z_score_box_style_wrc = z_score_box_style_green if z_score_color_class_wrc == "z-score-box-green" else z_score_box_style_red
    z_score_box_wrc = html.Div(
        f"wRC+ Difference: {z_score_difference_wrc:.2f}",
        style=z_score_box_style_wrc
    )

        # Create the verdict boxes using Div elements with the appropriate styles and classes
    verdict_box_style_woba = z_score_box_style_green if verdict_box_class_woba == "z-score-box-green" else z_score_box_style_red

    verdict_box_woba = html.A(
    href="https://raw.githubusercontent.com/PsCushman/baseball-rule-changes/PSC/Images/shap_woba_class.png",
    target="_blank",  # Open link in a new tab
    style={"text-decoration": "none"}  # Remove underline for the link
    )
    verdict_box_woba_content = html.Div(
        f"wOBA Prediction: {verdict_woba}", style=verdict_box_style_woba)
    verdict_box_woba.children = [verdict_box_woba_content]


    verdict_box_style_slg = z_score_box_style_green if verdict_box_class_slg == "z-score-box-green" else z_score_box_style_red
    
    verdict_box_slg = html.A(
    href="https://raw.githubusercontent.com/PsCushman/baseball-rule-changes/PSC/Images/shap_slg_class.png",
    target="_blank",  # Open link in a new tab
    style={"text-decoration": "none"}  # Remove underline for the link
    )
    verdict_box_slg_content = html.Div(
        f"SLG Prediction: {verdict_slg}", style=verdict_box_style_slg,
    )
    verdict_box_slg.children = [verdict_box_slg_content]

    verdict_box_style_babip = z_score_box_style_green if verdict_box_class_babip == "z-score-box-green" else z_score_box_style_red
    
    verdict_box_babip = html.A(
    href="https://raw.githubusercontent.com/PsCushman/baseball-rule-changes/PSC/Images/shap_babip_class.png",
    target="_blank",  # Open link in a new tab
    style={"text-decoration": "none"}  # Remove underline for the link
    )
    verdict_box_babip_content = html.Div(
        f"BABIP Prediction: {verdict_babip}",
        style=verdict_box_style_babip,
    )
    verdict_box_babip.children = [verdict_box_babip_content]

    verdict_box_style_wrc = z_score_box_style_green if verdict_box_class_wrc == "z-score-box-green" else z_score_box_style_red
        
    verdict_box_wrc = html.A(
    href="https://raw.githubusercontent.com/PsCushman/baseball-rule-changes/PSC/Images/shap_wrc_class.png",
    target="_blank",  # Open link in a new tab
    style={"text-decoration": "none"}  # Remove underline for the link
    )

    verdict_box_wrc_content = html.Div(
        f"wRC+ Prediction: {verdict_wrc}", style=verdict_box_style_wrc,
    )
    verdict_box_wrc.children = [verdict_box_wrc_content]

    selected_columns = [
        "Name", "bat_side", "AB", "H", "SB", "HR", "RBI", "SO", "AVG",
        "SLG", "OPS", "WAR", "Barrel%"
    ]

    # Round numeric values to 3 decimal places
    player_info_rounded = player_info[selected_columns].round(3)

    player_info_table = dash_table.DataTable(
        columns=[{"name": col, "id": col} for col in selected_columns],
        data=player_info_rounded.to_dict("records")
    )

    # Wrap the player info table in a div with a title
    player_info_with_title = html.Div([
        html.H3("Player Information: Returns averages from 2018-2022 (excluding 2020)", style=H3_style),  # Add the title
        player_info_table
    ])

    # Return the updated verdict boxes along with other outputs
    return (
        [dcc.Graph(figure=fig)],  # Output "output-graphs.children"
        z_score_box_woba,  # Output "woba-difference-box.children"
        z_score_color_class_woba,  # Output "woba-difference-box.className"
        z_score_box_slg,  # Output "slg-difference-box.children"
        z_score_color_class_slg,  # Output "slg-difference-box.className"
        z_score_box_babip,  # Output "babip-difference-box.children"
        z_score_color_class_babip,  # Output "babip-difference-box.className"
        z_score_box_wrc,  # Output "wrc-difference-box.children"
        z_score_color_class_wrc,  # Output "wrc-difference-box.className"
        verdict_box_woba,  # Output "woba-verdict-box.children"
        verdict_box_class_woba,  # Output "woba-verdict-box.className"
        verdict_box_slg,  # Output "slg-verdict-box.children"
        verdict_box_class_slg, # Output "slg-verdict-box.className"
        verdict_box_babip,  # Output "babip-verdict-box.children"
        verdict_box_class_babip, # Output "babip-verdict-box.className"
        verdict_box_wrc,  # Output "wrc-verdict-box.children"
        verdict_box_class_wrc,  # Output "wrc-verdict-box.className"
        [player_info_with_title]   # Output "player-info-container.children"
    )
if __name__ == "__main__":
    app.run_server(debug=True, port=8051)