![Screen Shot 2023-08-31 at 10 51 39 PM](https://github.com/PsCushman/baseball-rule-changes/assets/122395437/64c35c7b-1943-4286-abf9-99ebf88032ab)

# Baseball Final Project
*by David, Payson, Leo*

**Baseball Analysis for a New Game: Predicting Pitching Performance, Hitting Performance, and WAR After the 2023 Rule Changes**

## Deployments and Analysis

For in-depth analysis of each component, please follow the links to the respective sections:

- **David:** [Project Analysis/Predictions for Pitcher Performance](https://dalfonsonash.github.io/mlb_project_4/)
- **Payson:** [Project Analysis/Predictions for Hitter Perforamnce](https://pscushman.github.io/final-project-analysis/)
- **Leo:** [WAR Predictions on Tableau](https://public.tableau.com/app/profile/leonardo.pierantoni/viz/MLBPredictions/Story1?publish=yes)

## Overview

Welcome to our Baseball Analysis project! Our goal is to leverage machine learning algorithms to assist MLB teams in strategic planning, especially in light of the 2023 Rule changes. We're dedicated to providing stakeholders with data-driven insights for making informed decisions about the future.

The Modern Era of baseball (2000s-2020s) has seen an increased emphasis on advanced statistics and analytics that has revolutionized player evaluation and strategic decision-making.

Teams have leveraged data to evaluate players more precisely, influencing strategic decisions. Pitchers excelled as teams shifted to power pitching as well as optimizing matchups with pitching changes and defensive shifts.

To combat these changes, hitters began emphasizing launch angles and power hitting, leading to fewer balls in play.

To maintain pace of play and increase excitement, this season the MLB implemented a pitch clock, limited defensive shifts, and instituted a universal DH, along with a few changes to increase base stealing attempts.

All together, these changes were expected to increase pace of play, increase balls in play, and overall, just make the game more exciting.

We've focused on three fundamental aspects of team building in this new environment:

1. **Predicting Player WAR:** We employ machine learning to predict which players under 30 are likely to experience the most significant increases in Wins Above Replacement (WAR) in 2023. This predictive model serves as a valuable resource for future years.

2. **Pitching Performance Analysis:** We've examined pitching performance leading up to 2023, constructing a model to predict performance changes in 2023. Our model identifies the key features contributing to these predictions.

3. **Hitting Performance Analysis:** Similar to our pitching analysis, we've conducted an in-depth exploration of hitting performance, predicting changes for 2023.

## Dashboards and Tableau

To facilitate interaction with the pitcher and hitter data, we've designed two interactive Plotly Dash dashboards. Follow these steps to run the dashboards on your local host:

- For the **Pitcher Dashboard:** Enter the name of any starting pitcher to view average metrics from 2018-2022 (excluding 2020). The dashboard provides z-score differences for 2023 predictions, along with indications of model accuracy. You'll also find images of the top 30 pitchers for 2023 according to ESPN.

![Screen Shot 2023-08-31 at 8 32 09 PM](https://github.com/PsCushman/baseball-rule-changes/assets/122395437/5c743abd-89d9-470e-983e-2cfa7aebffa9)
![Screen Shot 2023-08-31 at 8 31 34 PM](https://github.com/PsCushman/baseball-rule-changes/assets/122395437/09f3f506-92d2-4eb5-92f6-255121684b01)


- The **Hitter Dashboard:** Functions similarly, offering insights on 256 active position players' metrics and prediction verdicts for the 2023 MLB season. It also showcases a striking background featuring Fenway Park's blueprint.

![Screen Shot 2023-08-31 at 8 23 40 PM](https://github.com/PsCushman/baseball-rule-changes/assets/122395437/856e7aca-38cd-4f50-a122-dec1a1add7da)

To utilize the dashboards, you will need to download the Dash-Pitcher and Dash-Hitter. Once downloaded, you will need to open gitbash or terminal at the directory. 

For the picher dashboard use this command:
    
    python pitch_app.py 

For the hitter dashboard:
    
    python hit_app.py
    
The flask app should run on localhost http://127.0.0.1:8050/ or http://127.0.0.1:8051/.

Additionally, our [Tableau story dashboard](https://public.tableau.com/app/profile/leonardo.pierantoni/viz/MLBPredictions/Story1?publish=yes) delves into 2023 WAR predictions, with a focus on young players. Navigate through interactive graphs and images, and explore predicted WAR for 2023. Take a peek at the team projected to have the highest WAR for 2024 and compare it to the current standings.

![Screen Shot 2023-08-31 at 10 19 56 PM](https://github.com/PsCushman/baseball-rule-changes/assets/122395437/fbc642b0-d668-454f-8bdc-f6fab13ed34a)

## Project Rubric

### Data Model Implementation (25 points)
- A Python script initializes, trains, and evaluates a model **(10 points)**
- Data is cleaned, normalized, and standardized before modeling **(5 points)**
- The model utilizes data retrieved from SQL or Spark **(5 points)**
- The model demonstrates meaningful predictive power: at least 75% classification accuracy or 0.80 R-squared **(5 points)**

### Data Model Optimization (25 points)
- The model optimization and evaluation process is documented using a CSV/Excel table or within the Python script **(15 points)**
- Overall model performance is clearly printed or displayed at the script's conclusion **(10 points)**

### GitHub Documentation (25 points)
- GitHub repository is organized and free of unnecessary files and folders, utilizing an appropriate .gitignore file **(10 points)**
- The README is polished and serves as a comprehensive presentation of the project's content **(15 points)**

### Group Presentation (25 points)
- All group members actively participate in the presentation **(5 points)**
- The presentation content flows smoothly, including transitions and conclusions **(5 points)**
- Content presented is relevant and directly related to the project's goals **(10 points)**
- The presentation effectively maintains audience interest and engagement **(5 points)**

# Resources
- [Cross-validation with Upsampling](https://kiwidamien.github.io/how-to-do-cross-validation-when-upsampling-data.html)
- [PyBaseball GitHub Repository](https://github.com/jldbc/pybaseball)
- [Data Science Approach to 2021 Hitting Projections](https://towardsdatascience.com/baseball-and-machine-learning-a-data-science-approach-to-2021-hitting-projections-4d6eeed01ede)
- [Dash Tips and Tricks](https://www.nelsontang.com/blog/2022-06-02-dash-tips)

