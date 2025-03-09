def calculate_avg_revenue_per_customer(df):
    total_revenue = df['revenue'].sum()
    total_customers = df['customer_id'].nunique()
    avg_revenue_per_customer = total_revenue / total_customers
    return avg_revenue_per_customer
