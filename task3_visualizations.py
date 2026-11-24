import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go

os.makedirs("reports/charts", exist_ok=True)

def run_task3():
    df = pd.read_csv("data/ecommerce_sales_cleaned.csv")
    sns.set_theme(style="whitegrid", palette="viridis")

    # 1. Bar Chart: Total Revenue by Product Category
    plt.figure(figsize=(9, 5))
    cat_sales = df.groupby("Product_Category", as_index=False)["Total_Sales"].sum().sort_values("Total_Sales", ascending=False)
    ax = sns.barplot(data=cat_sales, x="Product_Category", y="Total_Sales", palette="viridis")
    ax.set_title("Total Revenue by Product Category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Sales ($)")
    for container in ax.containers:
        ax.bar_label(container, fmt="$%.0f", padding=3)
    plt.tight_layout()
    plt.savefig("reports/charts/1_bar_category_revenue.png", dpi=300)
    plt.close()

    # 2. Line Chart: Monthly Revenue Trend
    plt.figure(figsize=(10, 5))
    monthly = df.groupby("Order_Month", as_index=False)["Total_Sales"].sum()
    plt.plot(monthly["Order_Month"], monthly["Total_Sales"], marker="o", linewidth=2.5, color="#2b5c8f")
    plt.title("Monthly Revenue Trend (2025)", fontsize=14, fontweight="bold")
    plt.xlabel("Month")
    plt.ylabel("Total Sales ($)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("reports/charts/2_line_monthly_trend.png", dpi=300)
    plt.close()

    # 3. Pie Chart: Revenue Share by Region
    plt.figure(figsize=(7, 7))
    region_sales = df[df["Region"] != "Unknown"].groupby("Region")["Total_Sales"].sum()
    plt.pie(region_sales, labels=region_sales.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("Set2"))
    plt.title("Revenue Distribution by Region", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("reports/charts/3_pie_region_share.png", dpi=300)
    plt.close()

    # 4. Histogram: Customer Age Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Customer_Age"], bins=15, kde=True, color="#1f77b4")
    plt.title("Customer Age Distribution", fontsize=14, fontweight="bold")
    plt.xlabel("Age (Years)")
    plt.ylabel("Transaction Count")
    plt.tight_layout()
    plt.savefig("reports/charts/4_hist_customer_age.png", dpi=300)
    plt.close()

    # 5. Scatter Plot: Unit Price vs. Total Sales (colored by Quantity)
    filtered_df = df[df["Total_Sales"] < 3000]
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=filtered_df, x="Unit_Price", y="Total_Sales", hue="Quantity", palette="coolwarm", alpha=0.75)
    plt.title("Unit Price vs. Total Sales by Order Quantity", fontsize=14, fontweight="bold")
    plt.xlabel("Unit Price ($)")
    plt.ylabel("Total Sales ($)")
    plt.legend(title="Quantity")
    plt.tight_layout()
    plt.savefig("reports/charts/5_scatter_price_vs_sales.png", dpi=300)
    plt.close()

    # Bonus: Interactive Dashboard using Plotly
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=("Revenue by Category", "Monthly Sales Trend", "Regional Share", "Age Distribution"),
        specs=[[{"type": "bar"}, {"type": "scatter"}],
               [{"type": "pie"}, {"type": "histogram"}]]
    )

    fig.add_trace(go.Bar(x=cat_sales["Product_Category"], y=cat_sales["Total_Sales"], name="Category Sales", marker_color="#2a9d8f"), row=1, col=1)
    fig.add_trace(go.Scatter(x=monthly["Order_Month"], y=monthly["Total_Sales"], mode="lines+markers", name="Monthly Trend", line=dict(color="#e76f51")), row=1, col=2)
    fig.add_trace(go.Pie(labels=region_sales.index, values=region_sales.values, name="Region Share"), row=2, col=1)
    fig.add_trace(go.Histogram(x=df["Customer_Age"], nbinsx=15, name="Age Dist", marker_color="#264653"), row=2, col=2)

    fig.update_layout(height=800, title_text="Interactive E-Commerce Sales Dashboard", showlegend=False, template="plotly_white")
    dashboard_path = "reports/task3_interactive_dashboard.html"
    fig.write_html(dashboard_path)
    print(f"[SUCCESS] Saved 5 static charts and interactive dashboard at {dashboard_path}")

if __name__ == "__main__":
    run_task3()
