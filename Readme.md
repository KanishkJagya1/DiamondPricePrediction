# Diamond Price Prediction

An end-to-end machine learning project aimed at predicting diamond prices using various regression techniques. This project includes every step from initial data handling to deploying a user interface for real-time predictions.

## Project Overview

This project follows a structured machine learning pipeline which includes data collection, exploratory data analysis, preprocessing, feature engineering, model building, and evaluation, concluding with the deployment of a model through a user interface.

### Steps followed during the project:

1. **Data Collection**: 
   The dataset was provided as part of a Kaggle competition. It can be downloaded from [this link](#).

2. **Exploratory Data Analysis (EDA)**:
   A detailed EDA is conducted in Jupyter Notebook. The notebook can be accessed and run online via [Google Colab](#).

3. **Data Preprocessing & Feature Engineering**:
   Based on the insights from EDA, appropriate data cleaning and feature engineering techniques were applied.

4. **Model Building**:
   Several models were trained including Linear Regression, Lasso, Ridge, and Elastic Net.

5. **Model Evaluation**:
   Models were evaluated based on RMSE, MAE, and R2 Score to select the best performer.

6. **Code Modularity**:
   The code was modularized into different pipelines for data transformation, preprocessing, and model training, including serialization with pickle for deployment.

7. **User Interface**:
   A user-friendly interface was developed and hosted using Hugging Face Spaces, allowing users to make real-time predictions.

### Model Performance

The following table showcases the performance of different algorithms:

| Algorithm          | RMSE      | MAE      | R2 Score |
|--------------------|-----------|----------|----------|
| Linear Regression  | 1013.904  | 674.025  | 93.68    |
| Lasso              | 1013.878  | 675.071  | 93.68    |
| Ridge              | 1013.905  | 674.055  | 93.68    |
| Elastic Net        | 1533.416  | 1060.736 | 85.564   |

### Tools and Technologies Used

- Python Libraries: pandas, NumPy, matplotlib, seaborn, scikit-learn
- Visual Studio Code
- Hugging Face Spaces (for hosting the application)

### Sample Input Data

Here are some sample values that can be used as input for predictions:

| Carat | Depth | Table | X    | Y    | Z    | Cut        | Color | Clarity | Actual Price |
|-------|-------|-------|------|------|------|------------|-------|---------|--------------|
| 0.71  | 61.4  | 56    | 5.74 | 5.77 | 3.53 | Ideal      | D     | VS2     | 3510         |
| 2     | 59.5  | 57    | 8.08 | 8.15 | 4.89 | Very Good  | G     | SI2     | 14691        |
| 1.52  | 60.8  | 59    | 7.36 | 7.4  | 4.49 | Premium    | G     | SI2     | 9970         |
| 1.5   | 60.1  | 61    | 7.45 | 7.42 | 4.47 | Good       | H     | IF      | 12641        |

## Getting Started

1. Clone the repository.
2. Set up your Python environment with the required libraries (`pip install -r requirements.txt`).
3. Run the Jupyter Notebook for exploratory data analysis and preprocessing.
4. Use the provided scripts to train the models and serialize them.
5. Deploy the user interface using Hugging Face Spaces.

## Contributors

- [Your Name](https://github.com/KanishkJagya1/DiamondPricePrediction)

Feel free to contribute to this project by forking and creating pull requests!

## License

This project is licensed under the [MIT License](LICENSE).
