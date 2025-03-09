from src.data_cleaning import load_data, clean_data
from src.data_visualization import (
    plot_revenue_distribution,
    plot_revenue_spread,
    plot_sales_method_distribution,
    plot_revenue_per_method,
    plot_weekly_revenue,
    plot_revenue_pie_chart
)
from src.data_analysis import calculate_avg_revenue_per_customer

def main():
    # Load and clean data
    data_path = 'data/product_sales.csv'
    product_sales = load_data(data_path)
    product_sales = clean_data(product_sales)

    # Visualizations
    plot_revenue_distribution(product_sales)
    plot_revenue_spread(product_sales)
    plot_sales_method_distribution(product_sales)
    plot_revenue_per_method(product_sales)
    plot_weekly_revenue(product_sales)
    plot_revenue_pie_chart(product_sales)

    # Analysis
    avg_revenue = calculate_avg_revenue_per_customer(product_sales)
    print(f"Initial Avg Revenue per Customer: {avg_revenue:.2f}")

if __name__ == "__main__":
    main()
