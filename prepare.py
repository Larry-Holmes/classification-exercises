import pandas as pd
import numpy as np

# import splitting functions
from sklearn.model_selection import train_test_split


def prep_iris(iris):
    iris = iris.drop(columns=['species_id','measurement_id'])
    iris = iris.rename(columns={'species_name':'species'})
    dummy_iris = pd.get_dummies(iris.species, drop_first=True)
    iris = pd.concat([iris, dummy_iris], axis=1)
    return iris


def prep_titanic(titanic):
    titanic = titanic.drop(columns=['embarked','class','deck'])
    dummy_df = pd.get_dummies(data=titanic[['sex','embark_town']], drop_first=True)
    titanic = pd.concat([titanic, dummy_df], axis=1)
    titanic = titanic.drop(columns=['sex', 'embark_town', 'passenger_id'])
    return titanic


def prep_telco(telco):
    telco = telco.drop(columns=['internet_service_type_id', 'contract_type_id', 'payment_type_id'])

    telco['is_female'] = telco.gender.map({'Female': 1, 'Male': 0})
    telco['has_partner'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['has_dependents'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['has_phone_service'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['has_paperless_billing'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['has_churned'] = telco.churn.map({'Yes': 1, 'No': 0})
    
    telco = telco.drop(columns = ['gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', 'churn', 'customer_id'])

    dummy_df = pd.get_dummies(telco[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    telco = pd.concat( [telco, dummy_df], axis=1 )
    
    telco = telco.drop(columns = ['multiple_lines', 'online_security', 'online_backup', \
                             'device_protection', 'tech_support', 'streaming_tv', \
                             'streaming_movies', 'payment_type', 'internet_service_type',\
                             'contract_type', 'online_security_No internet service', \
                             'online_backup_No internet service', 'device_protection_No internet service', \
                             'tech_support_No internet service', 'streaming_tv_No internet service', \
                             'streaming_movies_No internet service', 'multiple_lines_No phone service'])
    telco['total_charges'] = telco.total_charges.replace(' ', 0)
    telco['total_charges'] = telco.total_charges.astype(float)
    return telco


def my_train_test_split(df, target):
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    
    return train, validate, test