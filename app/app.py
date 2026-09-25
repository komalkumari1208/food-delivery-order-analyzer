import streamlit as st
import pandas as pd

# -------------------------------
# LOAD DATASET
# -------------------------------

df = pd.read_csv("food_delivery.csv")

# Convert date
df["order_date"] = pd.to_datetime(df["order_date"])


# -------------------------------
# PAGE TITLE
# -------------------------------

st.title("🍔 Food Delivery Order Analyzer")

st.write(
    "Enter your order details below to analyze "
    "historical delivery patterns."
)


# -------------------------------
# USER INPUTS
# -------------------------------

cuisine = st.selectbox(
    "Select Cuisine",
    sorted(df["cuisine_type"].unique())
)

location = st.selectbox(
    "Select Location",
    sorted(df["location"].unique())
)

order_cost = st.number_input(
    "Order Amount (₹)",
    min_value=50.0,
    max_value=1000.0,
    value=300.0
)

rating = st.slider(
    "Restaurant Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

prep_time = st.number_input(
    "Food Preparation Time (minutes)",
    min_value=5,
    max_value=60,
    value=20
)

day_type = st.selectbox(
    "Day Type",
    ["Weekday", "Weekend"]
)


# -------------------------------
# ANALYZE ORDER
# -------------------------------

if st.button("Analyze Order"):

    st.subheader("📊 Order Analysis")

    # ---------------------------
    # FILTER HISTORICAL DATA
    # ---------------------------

    cuisine_data = df[
        df["cuisine_type"] == cuisine
    ]

    location_data = df[
        df["location"] == location
    ]
    rating_data = df[
        (df["cuisine_type"] == cuisine) &
        (df["location"] == location)
    ]

    rating_avg_delivery = rating_data[
        "delivery_time"
    ].mean()
    similar_orders = df[
        (df["cuisine_type"] == cuisine) &
        (df["location"] == location) &
        (df["day_type"] == day_type)
    ]


    # ---------------------------
    # HISTORICAL AVERAGES
    # ---------------------------

    cuisine_avg_delivery = cuisine_data[
        "delivery_time"
    ].mean()

    location_avg_delivery = location_data[
        "delivery_time"
    ].mean()

    cuisine_avg_cost = cuisine_data[
        "cost_of_the_order"
    ].mean()


    # ---------------------------
    # SIMILAR ORDER ANALYSIS
    # ---------------------------

    if len(similar_orders) > 0:

        similar_avg_delivery = similar_orders[
            "delivery_time"
        ].mean()

    else:

        similar_avg_delivery = (
            cuisine_avg_delivery +
            location_avg_delivery
        ) / 2


    # ---------------------------
    # DELIVERY PROFILE
    # ---------------------------

    if similar_avg_delivery < 30:

        delivery_status = (
            "Historically faster delivery profile 🚀"
        )

    elif similar_avg_delivery < 40:

        delivery_status = (
            "Historically typical delivery profile 👍"
        )

    else:

        delivery_status = (
            "Historically longer delivery profile ⚠️"
        )


    # ---------------------------
    # ORDER VALUE CATEGORY
    # ---------------------------

    if order_cost < 200:

        order_category = "Low Value Order"

    elif order_cost < 400:

        order_category = "Medium Value Order"

    else:

        order_category = "High Value Order"


    # ---------------------------
    # KEY METRICS
    # ---------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Cuisine Avg. Delivery",
            f"{cuisine_avg_delivery:.0f} min"
        )

    with col2:

        st.metric(
            "Location Avg. Delivery",
            f"{location_avg_delivery:.0f} min"
        )

    with col3:

        st.metric(
            "Similar Orders",
            len(similar_orders)
        )


    # ---------------------------
    # DELIVERY ASSESSMENT
    # ---------------------------

    st.write("### 🚴 Delivery Assessment")

    st.info(delivery_status)


    # ---------------------------
    # ORDER VALUE ANALYSIS
    # ---------------------------

    st.write("### 💰 Order Analysis")

    st.write(
        f"**Your Order Value:** ₹{order_cost:.0f}"
    )

    st.write(
        f"**Average Order Value for {cuisine}:** "
        f"₹{cuisine_avg_cost:.0f}"
    )

    st.write(
        f"**Order Category:** {order_category}"
    )


    # Compare user's order with historical average

    if order_cost < cuisine_avg_cost:

        difference = cuisine_avg_cost - order_cost

        st.info(
            f"Your order is ₹{difference:.0f} below "
            f"the historical average for {cuisine} orders."
        )

    elif order_cost > cuisine_avg_cost:

        difference = order_cost - cuisine_avg_cost

        st.info(
            f"Your order is ₹{difference:.0f} above "
            f"the historical average for {cuisine} orders."
        )

    else:

        st.info(
            f"Your order value is approximately equal "
            f"to the historical average for {cuisine} orders."
        )


    # ---------------------------
    # SIMILAR HISTORICAL ORDERS
    # ---------------------------

    st.write("### 🔎 Similar Historical Orders")

    if len(similar_orders) > 0:

        st.write(
            f"Found **{len(similar_orders)} historical orders** "
            f"with the same cuisine, location and day type."
        )

        similar_display = similar_orders[
            [
                "order_id",
                "restaurant_name",
                "cuisine_type",
                "location",
                "cost_of_the_order",
                "rating",
                "food_preparation_time",
                "delivery_time"
            ]
        ].copy()

        # Show maximum 10 orders
        similar_display = similar_display.head(10)

        st.dataframe(
            similar_display,
            use_container_width=True
        )

    else:

        st.warning(
            "No historical orders matched the selected "
            "cuisine, location and day type."
        )


    # ---------------------------
    # HISTORICAL COMPARISON
    # ---------------------------

    st.write("### 📈 Historical Comparison")

    comparison_data = pd.DataFrame({

       "Category": [
    "Your Preparation Time",
    "Cuisine Avg Delivery",
    "Location Avg Delivery",
    "Similar Orders Avg Delivery",
    "Cuisine + Location Avg Delivery"
],

      "Minutes": [
    prep_time,
    cuisine_avg_delivery,
    location_avg_delivery,
    similar_avg_delivery,
    rating_avg_delivery
]

    })

    st.bar_chart(
        comparison_data.set_index("Category")
    )


    # ---------------------------
    # KEY INSIGHT
    # ---------------------------

    st.write("### 💡 Key Insight")

    st.write(
        f"Based on **{len(similar_orders)} historical orders** "
        f"with the selected cuisine, location and day type, "
        f"the average delivery time was "
        f"**{similar_avg_delivery:.0f} minutes**."
    )