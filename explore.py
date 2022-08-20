import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def dtypes_to_list(df):
    num_type_list , cat_type_list = [], []

    for column in df:
        col_type = df[column].dtype
        if col_type == 'object':
            cat_type_list.append(column)
        if np.issubdtype(df[column], np.number) and \
             ((df[column].max() + 1) / df[column].nunique())  == 1 :
            cat_type_list.append(column)
        if np.issubdtype(df[column], np.number) and \
            ((df[column].max() + 1) / df[column].nunique()) != 1 :
            num_type_list.append(column)
    return num_type_list, cat_type_list


def telco_vis(train, col):
    plt.title('Relationship of churn rate and '+col)
    sns.barplot(x=col, y='has_churned', data=train)
    churn_rate = train.has_churned.mean()
    plt.axhline(churn_rate, label='churn rate')
    plt.legend()
    plt.show()

def telco_test(train, col):
    alpha = 0.05
    null_hyp = col+' and churn rate are independent'
    alt_hyp = 'There is a relationship between churn rate and '+col
    observed = pd.crosstab(train.has_churned, train[col])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    if p < alpha:
        print('We reject the null hypothesis that', null_hyp)
        print(alt_hyp)
    else:
        print('We fail to reject the null hypothesis that', null_hyp)
        print('There appears to be no relationship between churn rate and '+col)

def telco_analysis(train, col):
    telco_vis(train, col)
    telco_test(train, col)