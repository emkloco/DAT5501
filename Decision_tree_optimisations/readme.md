# Decision Tree Optimization & Hyperparameter Tuning

## Overview
This project explores the "Goldilocks Problem" in machine learning: finding a model that is neither too simple (underfitting) nor too complex (overfitting). 

Using the UCI Car Evaluation dataset, I trained multiple Decision Tree Classifiers with varying maximum depths to identify the optimal configuration for predicting car acceptability.

## Key Features
- **Hyperparameter Tuning:** Loops through tree depths (1–20) to find the optimal F1-score.
- **Overfitting Visualization:** plots "Training Accuracy" vs "Test Accuracy" to visualize where the model starts memorizing noise rather than learning patterns.
- **Feature Importance:** Extracts and ranks which features (e.g., safety score, buying price) have the biggest impact on the decision.

## Dataset
**UCI Car Evaluation Dataset**  
A collection is fetched from uci repository which contains 1728 records classifying cars into four categories (unacceptable, acceptable, good, very good) based on buying price, maintenance cost, number of doors, etc.

## Usage
Run the script to generate the optimization graph and print the top features to the console:

```bash
python machine_learning_activity.py