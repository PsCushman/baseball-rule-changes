

#                                               Project 4: MLB Starting Pitcher Stats
![action-1850887_1280](https://github.com/PsCushman/baseball-rule-changes/assets/126922261/4a4c10b5-c8fc-490d-b99e-a3e87c152303)

For this project, our team decided solve, analyze, or visualize a problem using machine learning (ML) with the other technologies we’ve learned.  MLB had many impacts on it's players over the recent years from both outside and inside the league.  The pandemic of 2020 caused a major disruption to our national pastime by reducing the normal 162 game regular season to just 60 games.  In 2022, the National League added the DH(Designated Hitter) rule allowing DH not only during interleague and post season games, but also to the regular season after more than 50 resistance to the rule.  In 2023 the Pitch Clock rule was added to shorten the already 3 hour plus games in order to speed things up.  Our goal was to use ML (Machine Learning) along with the usual ETL to analyze a plethora of baseball statistics to see if these major impacts to the game would have any impact whatsoever to individual player statistics.

My portion of this project was to analyze three major pitching statistics, the ERA(Earned Run Average), FIP(Fielding Independent Pitching), and WHIP(Walks and Hits per Inning Pitched).  By applying the techniques learned during the 6 months UC Davis Data Analytics course, we performed ETL first by downloading all 2018 through 2022 pitching statistics for all starting pitchers in the NL and AL.  The data was imported as a CSV, and then preprocessed by importing the necessary libraries. Performed missing data imputation, and data cleanup.  This was followed by training and evaluating Logistic Regression Models for our three specific stats targets.  Targets were converted to binary classes, and SMOTE applied for oversampling to balance the classes.  Then a training and evaluation classification model was implemented using an XGBoost classifier.  Once the the model was trained for the different metrics, the code generated SHAP summary plots for each target column to visualize feature importance and their effects on predictions.  Prediction dataframes were created to hold prediction results, actual values, and correctness for each target column.

Finally, dataframes with the results were transformed into useable data by creating a dashboard, using HTML and CSS, that recalls individual pitcher's predicted statistics along with some entertaining photos of the players themselves.  Now that the work is done, lets PLAY BALL!!!

## ETL and Preprocessing 
* 2018_2023_full_pitcher_stats.ipynb

## Classification and logistic regression using XGBoost algorithm
* mlb_pitcher_class.ipynb (for reference see Modeling Part 1: A Regression Approach, by John Pette: https://towardsdatascience.com/baseball-and-machine-learning-a-data-science-approach-to-2021-hitting-projections-4d6eeed01ede)
* (additional linear regression model see mlb_regression.ipynb)

## Resources used for ETL, and classification and logistic regression
* See Resources folder
  ### ETL, preprocessing, and test and training resources
  * 2018_2023_mlb_sp_stats.csv (Imported from FanGraphs)
  * full_era_learning.csv
  * full_fip_learning.csv
  * full_whip_learning.csv
  ### Dataframes created to generate HTML MLB Starting Pitcher Dashboard
  * merged_data.csv
  * verdict.csv
## Dash Folder
* full_pitcher_data.csv
* pitching_verdict.csv
* pitch_app.py (HTML to MLB Dashboard)
## assets folder
* styles.css
## Images folder
* action-1850887_1280.jpg (photo used on this readme: [https://tsurezure-baseball.com/wp-content/uploads/2016/12/cropped-baseball-1222404_1280.jpg](https://pixabay.com/photos/action-athletes-audience-ballpark-1850887/)https://pixabay.com/photos/action-athletes-audience-ballpark-1850887/)
## Final Presentation/Analysis folder
* index.html (link to final presentation) 
