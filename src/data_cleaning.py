import pandas as pd

def load_data(filepath)
    return pd.read_csv(filepath)

def clean_sales_method(df)
    df['sales_method'] = df['sales_method'].str.lower().str.replace('em +', 'email ')
    return df

def impute_revenue(df)
    df['revenue'].fillna(df['revenue'].median(), inplace=True)
    return df

def clean_years_as_customer(df)
    max_years = 2025 - 1984
    median_years = df.loc[df['years_as_customer'] = max_years, 'years_as_customer'].median()
    df.loc[df['years_as_customer']  max_years, 'years_as_customer'] = median_years
    return df

def clean_data(df)
    df = clean_sales_method(df)
    df = impute_revenue(df)
    df = clean_years_as_customer(df)
    return df
