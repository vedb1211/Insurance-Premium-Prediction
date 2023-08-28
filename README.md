<div align="center">
  <img src="Insurance_premium_UI.png" alt="Insurance Premium Predictor">
</div>

# Insurance Premium Predictor

Welcome to the **Insurance Premium Predictor** project! This repository hosts an exciting predictive model designed to estimate insurance premiums based on various factors. Whether you're an insurance professional, a data enthusiast, or just curious about predictive modeling, this project is sure to capture your attention.

## :rocket: Project Overview

In our intricate world, insurance plays a pivotal role in risk mitigation and financial security. One crucial aspect is the determination of **insurance premiums**. These premiums depend on diverse factors such as age, gender, location, medical history, and more. Our project leverages the power of machine learning to predict insurance premiums with greater accuracy and efficiency.

## :gear: How It Works

The Insurance Premium Predictor project is built on a robust foundation of **data analysis**, **preprocessing**, **machine learning**, and **visualization**. Here's an overview of its components:

1. **Data Collection**: We've assembled a comprehensive dataset with anonymized policyholder information and corresponding insurance premiums.

2. **Data Preprocessing**: Raw data rarely suits modeling. Our preprocessing pipeline handles missing values, encodes features, and scales data for optimal training readiness.

3. **Feature Selection**: Not all features hold equal importance. Advanced techniques help us identify influential features, enhancing predictive power.

4. **Model Selection**: We've explored various Linear Regression using OLS and find out the best model within OLS.

5. **Training and Tuning**: Our chosen model is trained on a subset of data and fine-tuned using cross-validation and hyperparameter optimization.

6. **Prediction**: Input potential policyholder attributes, and the model predicts their insurance premium.

7. **Visualization**: Interactive visuals shed light on attribute relationships and their impact on premiums.

## :file_folder: Repository Structure

The repository is organized as follows:

- `insurance.csv/`: Dataset for training and testing the model. Please avoid direct modifications.

- `Insurance_prediction_LRModel.ipynb/`: Jupyter notebooks for data exploration, preprocessing, and model development.

- `app.py/` : Python flask file

- `index.html`: Containg the html file inside Template folder

## :rocket: Getting Started

To dive into the Insurance Premium Predictor project:

1. Clone this repository to your local machine.
   
2. Explore the `Insurance_prediction_LRModel.ipynb/` directory to follow the project's evolution.
   
3. Install required dependencies from `requirements.txt` using `pip`:
