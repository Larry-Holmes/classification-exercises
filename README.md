# Classification Project Summary

## Project Objectives
> - Document code, process, findings, and key takeawys in a Jupyter Notebook Final Report
> - Create modules that make the process repeatable and the report easier to read and follow
> - Construct a model to predict customer churn using classification techniques, and make predictions for a group of customers
> - Refine work with a Report, in the form of a jupyter notebook, that will be walked through in a 5 minute presentation to a group of collegues and managers about the work did, why, goals, what was found, methodologies, and conclusions.
> - Answer panel questions about the code, process, findings and takeaways, and model.

## Business Goals
> - Find drivers for customer churn at Telco.  Why are customers churning?
> - Construct a ML classification model that accurately predicts customer churn.
> - Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?

## Deliverables
> - Readme (.md)
> - Final Report (.ipynb)
> - Acquire and Prepare Modules (.py)
> - Predictions (.csv)
> - A non_final Notebook (.ipynb)

## Data Dictionary

|Target|Datatype|Definition
|:-------|:-------|:----------|
|churn|7043 non-null: int64| 1: customer has churned, 0: customer hasn't churned|

|Feature|Datatype|Definition|
|:-------|:-------|:----------|
|customer_id                        |7043 non-null: object | identifier for each individual customer's account|
|senior_citizen                     |7043 non-null: int64  | 1: is senior citizen, 0: ins't senior citizen|
|tenure                             |7043 non-null: int64  | how long a customer has been utilizing telco services|
|monthly_charges                    |7043 non-null: float64| how much a customer pays per month|
|total_charges                      |7043 non-null: float64| how much a customer has paid since beginning their services with telco|
|is_female                          |7043 non-null: int64  | 1: is a female, 0: is a male|
|has_partner                        |7043 non-null: int64  | 1: has a significant other, 0: is single|
|has_dependents                     |7043 non-null: int64  | 1: has children, 0: doesn't have children|
|has_phone_service                  |7043 non-null: int64  | 1: has phone service with telco, 0: doesn't have phone service through telco|
|multiple_lines_Yes                 |7043 non-null: uint8  | 1: has multiple phone lines, 0: doesn't have multiple phone lines|
|online_security_Yes                |7043 non-null: uint8  | 1: utilizes online security services, 0: doesn't use online security|
|online_backup_Yes                  |7043 non-null: uint8  | 1: has online backup services via telco, 0: doesn't use online backup services|
|device_protection_Yes              |7043 non-null: uint8  | 1: has device protection via telco, 0: doesn't have device protection|
|tech_support_Yes                   |7043 non-null: uint8  | 1: has technical support services with telco, 0: doesn't have technical support services|
|streaming_tv_Yes                   |7043 non-null: uint8  | 1: has tv streaming capabilities with their account, 0: doesn't have tv streaming|
|streaming_movies_Yes               |7043 non-null: uint8  | 1: has movie streaming capabilities with their account, 0: doesn't have movie streaming|
|contract_type_One year             |7043 non-null: uint8  | 1: must renew their contract every year, 0: doesn't renew their contract each year|
|contract_type_Two year             |7043 non-null: uint8  | 1: must renew their contract every two years, 0: doesn't renew their contract every two years|
|internet_service_type_Fiber optic  |7043 non-null: uint8  | 1: has fiber optic internet, 0: doesn't have fiber optic internet|
|internet_service_type_None         |7043 non-null: uint8  | 1: doesn't have internet service via telco, 0: does have internet service with telco|
|payment_type_Credit car (automatic)|7043 non-null: uint8  | 1: makes payments via automatic credit card transfer, 0: doesn't use automatic credit card transfer|
|payment_type_Electronic check      |7043 non-null: uint8  | 1: makes payments via electronic checks, 0: doesn't use electronic checks to make payments|
|payment_type_Mailed check          |7043 non-null: uint8  | 1: makes payments via mailed in checks, 0: doesn't use mailed checks to make payments|

## Initial Hypotheses

## Executive Summary - Key Findings and Recommendations

## Project Plan
### Planning Phase
>
### Acquire Phase
>
### Prepare Phase
>
### Explore Phase
>
### Model Phase
>
### Deliver Phase
>
## How To Reproduce My Project
> 1. Read this README.md
> 2. Download the acquire.py, prepare.py, explore.py and final_report.ipynb files into your directory along with your own env file that contains your user, password, and host variables
> 3. Run my final_report.ipynb notebook
> 4. Congratulations! You can predict future churn at Telco!
