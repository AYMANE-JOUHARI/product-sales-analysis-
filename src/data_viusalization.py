import seaborn as sns
import matplotlib.pyplot as plt

def plot_revenue_distribution(df):
    sns.histplot(df['revenue'], bins=30, kde=True)
    plt.xlabel("Revenue")
    plt.ylabel("Frequency")
    plt.title("Revenue Distribution")
    plt.show()

def plot_revenue_spread(df):
    sns.boxplot(y=df['revenue'], palette='coolwarm')
    plt.ylabel("Revenue")
    plt.title("Revenue Spread")
    plt.show()

def plot_sales_method_distribution(df):
    sns.countplot(df, x='sales_method', hue='sales_method')
    plt.title('Customer per Method')
    plt.ylabel('Number of Customers')
    plt.xlabel('Sales Method')
    plt.show()

def plot_revenue_per_method(df):
    sns.histplot(df, x='revenue', hue='sales_method', binwidth=10, kde=True)
    plt.title('Revenue per Method')
    plt.ylabel('Number of Customers')
    plt.xlabel('Revenue')
    plt.show()

def plot_weekly_revenue(df):
    sns.lineplot(data=df, y='revenue', x='week', hue='sales_method')
    plt.title('Revenue per Week')
    plt.ylabel('Revenue')
    plt.xlabel('Week')
    plt.show()

def plot_revenue_pie_chart(df):
    revenue_per_method = df.groupby('sales_method')['revenue'].sum()
    plt.figure(figsize=(7, 7))
    plt.pie(revenue_per_method, labels=revenue_per_method.index, autopct='%1.1f%%', 
            colors=['#1f77b4', '#ff7f0e', '#2ca02c'])
    plt.title('Revenue Contribution by Sales Method')
    plt.show()
