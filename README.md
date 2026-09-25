# 🍔 Food Delivery Order Analyzer

## Interactive Data Science Application

Food Delivery Order Analyzer is an interactive Data Science application built using Python, Pandas, and Streamlit.

The application analyzes historical food delivery orders based on user-provided order details such as cuisine, location, order amount, restaurant rating, food preparation time, and day type.

It provides historical delivery statistics, similar historical orders, order-value comparisons, visualization, and automatically generated insights.

---

## 🎯 Project Objectives

- Analyze historical food delivery order data.
- Calculate cuisine-level and location-level delivery averages.
- Identify similar historical orders.
- Compare order value with the historical average.
- Categorize orders as Low, Medium, or High Value.
- Provide interactive data analysis through Streamlit.
- Present results using tables, metrics, and charts.

---

## 🛠️ Technologies Used

- **Python** – Core programming and data analysis
- **Pandas** – Data loading, filtering, aggregation, and analysis
- **Streamlit** – Interactive web application
- **CSV** – Dataset storage
- **Jupyter Notebook / Google Colab** – Exploratory data analysis
- **Git & GitHub** – Version control and project hosting

---

## 📊 Dataset

The project uses a synthetic food delivery dataset containing:

- **1,000 order records**
- **12 columns**

### Main Features

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `customer_id` | Customer identifier |
| `restaurant_name` | Restaurant name |
| `cuisine_type` | Cuisine associated with the order |
| `order_date` | Date of the order |
| `location` | Order location |
| `cost_of_the_order` | Order cost in INR |
| `rating` | Restaurant/order rating |
| `food_preparation_time` | Food preparation time in minutes |
| `delivery_time` | Delivery time in minutes |
| `day_type` | Weekday or Weekend |
| `total_delivery_time` | Total delivery-related time |

---

## 🔄 Application Workflow

```text
User Input
    ↓
Historical Dataset
    ↓
Data Filtering
    ↓
Cuisine & Location Analysis
    ↓
Similar Historical Orders
    ↓
Descriptive Statistics
    ↓
Visualization
    ↓
Key Insight