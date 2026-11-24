# Task 3: Data Visualization & Interactive Dashboard

A Python data visualization repository built with Matplotlib, Seaborn, and Plotly to uncover revenue trends, category performance, demographic distributions, and pricing dynamics.

## Repository Structure
```text
task3-data-visualization-dashboard/
├── data/
│   └── ecommerce_sales_cleaned.csv               # Cleaned dataset ready for Python, Power BI, or Tableau
├── reports/
│   ├── charts/
│   │   ├── 1_bar_category_revenue.png            # Bar chart of gross revenue by product category
│   │   ├── 2_line_monthly_trend.png              # Line chart of monthly revenue trajectory
│   │   ├── 3_pie_region_share.png                # Pie chart of regional revenue distribution
│   │   ├── 4_hist_customer_age.png               # Histogram + KDE of customer age distribution
│   │   └── 5_scatter_price_vs_sales.png          # Scatter plot of unit price vs. total sales by quantity
│   └── task3_interactive_dashboard.html          # Multi-panel interactive Plotly dashboard (Bonus)
├── src/
│   └── task3_visualizations.py                   # Script generating all static charts & interactive HTML dashboard
├── .gitignore
├── requirements.txt
└── README.md
```

## Key Visual Deliverables
1. **Bar Chart (`1_bar_category_revenue.png`):** Compares gross revenue across product categories with direct value annotations.
2. **Line Chart (`2_line_monthly_trend.png`):** Tracks month-over-month sales momentum across 2025.
3. **Pie Chart (`3_pie_region_share.png`):** Illustrates percentage revenue share across North, South, East, and West regions.
4. **Histogram (`4_hist_customer_age.png`):** Displays customer age distribution overlaid with a Kernel Density Estimate (KDE).
5. **Scatter Plot (`5_scatter_price_vs_sales.png`):** Visualizes the linear scaling between unit price, order quantity, and total transaction value.
6. **Interactive Dashboard (`task3_interactive_dashboard.html`):** Browser-ready Plotly dashboard supporting hover tooltips, zooming, and panning. You can also import `data/ecommerce_sales_cleaned.csv` directly into **Power BI** or **Tableau**.

## Quickstart
```bash
pip install -r requirements.txt
python src/task3_visualizations.py
```
