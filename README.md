# baseball-rule-changes
Predicting Success following MLBs Rule Changes 

The provided code demonstrates the usage of a supervised machine learning model, specifically a Random Forest Regressor, to predict career Wins Above Replacement (WAR) for baseball players. Let's break down the key components:

Supervised Learning: In supervised learning, the algorithm is trained on a labeled dataset, meaning it learns from input-output pairs. In this case, the inputs are various player statistics (features like Batting, Base Running, etc.), and the output is the player's WAR.

Random Forest Regressor: The Random Forest Regressor is a machine learning algorithm that belongs to the ensemble learning category. It uses multiple decision trees to make predictions and then averages their outputs to improve accuracy and reduce overfitting.

Training Data: The dataset contains historical player data from 1990 to 2023, including player statistics and their corresponding WAR values.

Feature Selection: The selected features for training the model include Batting, Base Running, Fielding, Positional, Offense, and Defense metrics.

Model Training: The model is trained using the RandomForestRegressor class from the scikit-learn library. It uses 100 decision trees with a maximum depth of 10 for each tree. This ensemble approach helps capture complex relationships within the data.

Model Evaluation: The model's performance is evaluated using various metrics like Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared (R2). These metrics quantify the difference between predicted and actual WAR values and measure the model's accuracy.

Predictions: The trained model is used to predict career WAR for the same dataset (data from 1990 to 2023) and compare these predictions to the actual WAR values.

Top 10 Players: The code sorts the data by predicted WAR values and selects the top 10 players with the highest predicted WAR values. It also prints the top 10 players based on their original WAR values.
