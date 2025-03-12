import pandas as pd
import streamlit as st
import plotly.express as px
import time  

# Page Configuration
st.set_page_config(page_title="Transaction Data Viewer", layout="wide")

# Load Dataset
dataset = pd.read_csv(r'C:\Users\RAJA\Downloads\transaction_data.csv')

# **Compute Highest Spenders Globally (before selecting tabs)**
highest_spenders = (
    dataset.groupby("customer_id")["amount"]
    .sum()
    .reset_index()
    .sort_values(by="amount", ascending=False)
)

# **Custom Tab Selection Using Radio Buttons**
selected_tab = st.sidebar.radio("Choose a Section", ["📋 Data Validation", "📊 Data Visualization"])

# **Show Sidebar Filter Only in "Data Validation"**
if selected_tab == "📋 Data Validation":
    st.sidebar.header("Filters")
    selected_customer = st.sidebar.selectbox("Select Customer ID", ["All"] + list(dataset["customer_id"].unique()))
else:
    selected_customer = "All"  # Hide filter when "Data Visualization" is selected

# **Tab 1: Data Validation**
if selected_tab == "📋 Data Validation":
    st.title("📋 Data Validation")

    # Show Dataset
    st.subheader("📜 Full Transaction Dataset")
    if selected_customer == "All":
        st.dataframe(dataset, use_container_width=True)
    else:
        st.dataframe(dataset[dataset["customer_id"] == selected_customer], use_container_width=True)

    # Animated Loading for Highest Spenders
    st.subheader("💰 Highest Spenders")
    progress_bar = st.progress(0)
    for percent in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent + 1)
    st.dataframe(highest_spenders.style.format({"amount": "₹{:.2f}"}), use_container_width=True)

    # Unique Customers
    top_customers = dataset["customer_id"].unique()
    st.subheader("🆔 Unique Customer IDs")
    st.write(f"Total Unique Customers: {len(top_customers)}")
    st.dataframe(pd.DataFrame(top_customers, columns=["Customer ID"]), use_container_width=True)

    # Customers Who Didn't Spend
    zero_spender = dataset[dataset["amount"].isna() | (dataset["amount"] == 0)]["customer_id"].unique()
    st.subheader("🚫 Customers Who Did Not Spend Money")
    st.write(f"Total: {len(zero_spender)} customers")
    st.dataframe(pd.DataFrame(zero_spender, columns=["Customer ID"]), use_container_width=True)

# **Tab 2: Data Visualization**
if selected_tab == "📊 Data Visualization":
    st.title("📊 Data Visualization")
    
        # Bar Chart: Highest Spenders
    st.subheader("📊 Top Spenders")
    fig_bar = px.bar(highest_spenders.head(10), x='customer_id', y='amount', 
                     title="Top 10 Highest Spenders", labels={'customer_id': 'Customer ID', 'amount': 'Total Amount Spent'})
    st.plotly_chart(fig_bar, use_container_width=True)

    # Pie Chart: Spending Distribution
    st.subheader("🎉 Spending Distribution")
    fig_pie = px.pie(highest_spenders, values='amount', names='customer_id', title="Spending Distribution by Customer")
    st.plotly_chart(fig_pie, use_container_width=True)
    
    st.write("🔍 No More visualizations yet! This section is under development. 🚧")

# **Animated Footer**
st.markdown(
    """
    <style>
        @keyframes glow {
            0% { color: #000; }
            50% { color: #ff6600; }
            100% { color: #000; }
        }
        .footer-text {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            animation: glow 2s infinite;
        }
    </style>
    <div class='footer-text'>💡 Developed By - SUBHADIP SADHU FROM ALIENITY TECHNOLOGIES 🚀</div>
    """,
    unsafe_allow_html=True
)