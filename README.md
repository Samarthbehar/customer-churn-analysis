# Customer Churn Analysis & Prediction

## Project Overview

Customer churn is a major challenge for telecom companies because losing customers directly impacts revenue.  
The goal of this project is to analyze customer behavior and identify factors that lead to churn, and then build a machine learning model that predicts which customers are most likely to leave.

By identifying these customers early, companies can take preventive actions such as better offers, improved service, or customer engagement strategies.

---

## Objectives

The main objectives of this project were:

- Analyze telecom customer data to understand churn patterns
- Identify important factors that influence customer churn
- Build a machine learning model to predict churn
- Improve model performance using proper preprocessing and feature scaling
- Provide business insights that can help reduce churn

---

## Dataset

The dataset used in this project is the **Telco Customer Churn dataset**.

It contains information about telecom customers such as:

- Customer demographics
- Contract type
- Internet services
- Payment methods
- Monthly charges
- Total charges
- Customer tenure
- Churn status

Dataset size: **~7000 customers**

---

## Data Preprocessing

Before training the model, several preprocessing steps were performed:

- Removed unnecessary columns such as geographic information
- Removed data leakage columns such as **Churn Label**
- Converted **Total Charges** column to numeric values
- Handled missing values
- Applied **One-Hot Encoding** to categorical variables
- Split the dataset into training and testing sets

---

## Machine Learning Model

A **Logistic Regression model** was used to predict customer churn.

To improve performance:

- Feature scaling was applied using **StandardScaler**
- `class_weight='balanced'` was used to handle class imbalance
- A **pipeline** was used for cleaner and more professional model training

---

## Model Performance

| Metric | Score |
|------|------|
| Accuracy | 94% |
| Precision (Churn) | 0.92 |
| Recall (Churn) | 0.85 |
| F1 Score | 0.88 |

The model correctly identifies about **85% of customers who are likely to churn**, helping businesses take preventive action.

---

## Key Insights from Analysis

Important churn patterns observed:

- Customers with **month-to-month contracts** churn more frequently
- **New customers with low tenure** are more likely to leave
- Customers paying **higher monthly charges** show higher churn probability
- Certain **payment methods** are associated with higher churn
- **Fiber optic internet users** sometimes churn due to higher expectations

---

## Business Recommendations

Based on the analysis, companies can reduce churn by:

- Offering incentives for long-term contracts
- Improving onboarding experience for new customers
- Monitoring high-value customers for service satisfaction
- Simplifying payment and billing processes

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Project Structure

Customer-Churn-Analysis
│
├── data
│ └── telco_churn.xlsx
│
├── notebooks
│ └── churn_analysis.ipynb
│
├── src
│ └── churn_model.py
│
├── requirements.txt
│
└── README.md


---

## Future Improvements

Possible improvements include:

- Testing advanced models such as Random Forest or XGBoost
- Creating an interactive Power BI dashboard
- Deploying the model as a web application
- Performing customer segmentation for targeted retention strategies

---

## Conclusion

This project demonstrates how data analysis and machine learning can help businesses understand customer behavior and predict churn.  
By identifying customers who are likely to leave, companies can take targeted actions to improve retention and protect revenue.
