# # Cricket Team Prediction

## Overview
This project aims to predict the players who will be part of the final playing XI for the cricket teams India and Australia in an upcoming tournament. The prediction is based on a dataset containing information about players' performances.

## Steps Involved

### 1. Dataset
- The dataset includes information about various players, such as runs scored, batting average, bowling statistics, etc.

### 2. Exploratory Data Analysis (EDA)
- Explored the dataset to understand the distribution of features and identify patterns.

### 3. Data Preprocessing
- Cleaned and prepared the data for modeling.
- Removed missing values and irrelevant columns.
- Engineered a new feature, 'Composite Score,' combining different performance metrics.

### 4. Model Selection
- Chose Logistic Regression as the predictive model.
- Utilized TensorFlow with Grid Search to find the best hyperparameters for the model.

### 5. Ranking Players
- Created a composite score for each player based on their performance metrics.
- Ranked players based on their composite scores.

### 6. Player Types and Selection
- Identified player types: Batsman (Type 1), All-Rounder (Type 2), and Bowler (Type 3).
- Selected the top 5 batsmen, top 2 all-rounders, and top 4 bowlers for each team based on their composite scores.

### 7. Final Playing XI
- Combined the selected players to form the predicted final playing XI for India and Australia.

## Files
- `playerdataoverall.csv`: The original dataset used for prediction.
- `final_playing_xi_india.csv` and `final_playing_xi_australia.csv`: CSV files containing the names of predicted players for India and Australia.

## Requirements
- Python 3.x
- TensorFlow
- Scikit-learn
- Pandas
- Matplotlib




